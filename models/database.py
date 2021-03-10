from typing import List
import sqlite3
from models.jk import JK, JKSize


class NameExistsError(ValueError):
    def __init__(self, msg):
        super(NameExistsError, self).__init__(msg)


class Database(object):

    _jk_size_scheme = "CREATE TABLE if not EXISTS jk_size(id integer primary key AUTOINCREMENT," \
                      "size varchar(5) not NULL," \
                      "length integer not NULL DEFAULT(42)," \
                      "CHECK(size IN ('xs', 's', 'm', 'l', 'xl')));"

    _jk_scheme = 'CREATE TABLE if not EXISTS jk(id integer primary key AUTOINCREMENT,' \
                 'name VARCHAR(50) NOT NULL UNIQUE,' \
                 'size integer not NULL,' \
                 'total integer not NULL DEFAULT(0),' \
                 'foreign KEY(size) REFERENCES jk_size(id));'

    def __init__(self, db_name):
        self._conn = sqlite3.connect(db_name)
        self._make_sure_table_exists()

    def __del__(self):
        self._conn.close()

    def _make_sure_table_exists(self):
        self._conn.execute(self._jk_size_scheme)
        self._conn.execute(self._jk_scheme)

    def add_new_jk_size(self, size: JKSize) -> JKSize:
        rows = self.find_jk_size(size.size_code, size.length)
        if len(rows) != 0:
            return rows[0]

        cur = self._conn.cursor()
        _id = cur.execute('INSERT INTO jk_size(size, length) VALUES (?, ?);',
                          (size.size_code.lower(), size.length)).lastrowid
        return JKSize(size.size_code, size.length, _id)

    no_matter_how_long = -1
    no_matter_what_size = ''

    def find_jk_size(self, size_code=no_matter_what_size, length=no_matter_how_long) -> List[JKSize]:
        cur = self._conn.cursor()
        sql = 'SELECT id, size, length FROM jk_size'
        cond = ' WHERE 1=1'
        args = []
        if size_code != self.no_matter_what_size:
            cond += ' AND size = ?'
            args.append(size_code)
        if length != self.no_matter_how_long:
            cond += ' AND length = ?'
            args.append(length)

        result = []
        for row in cur.execute(sql + cond, args):
            result.append(JKSize(row[1], row[2], row[0]))

        return result

    def get_jk_size(self, size_id: int) -> JKSize:
        cur = self._conn.cursor()
        sql = 'SELECT id, size, length FROM jk_size WHERE id = ?'
        result = []
        for row in cur.execute(sql, (size_id,)):
            result.append(JKSize(row[1], row[2], row[0]))
        return result[0]

    def add_new_jk(self, jk: JK) -> JK:
        cur = self._conn.cursor()
        if len(self.find_jk(jk.name)) != 0:
            raise NameExistsError(f'name {jk.name} already exists')
        _id = cur.execute('INSERT INTO jk(name, size, total) VALUES(?, ?, ?)',
                          (jk.name, jk.size.id, jk.count)).lastrowid
        self._conn.commit()
        return JK(jk.name, jk.size, jk.count, _id)

    no_matter_what_jk_name = ''
    no_matter_what_jk_size = None

    def find_jk(self, name: str = no_matter_what_jk_name) -> list:
        sql = 'SELECT a.id, a.name, a.size, a.total, b.size, b.length FROM jk as a, jk_size as b ' \
              'WHERE a.size = b.id'
        cond = ''
        args = []
        if name != self.no_matter_what_jk_name:
            cond += " AND a.name LIKE ?"
            args.append('%{0}%'.format(name))

        cur = self._conn.cursor()
        result = []
        for row in cur.execute(sql + cond, args):
            result.append(JK(row[1], JKSize(row[4], row[5], row[2]), row[3], row[0]))

        return result

    def update_jk(self, jk: JK):
        cur = self._conn.cursor()
        sql = 'UPDATE jk SET name = ?, size = ?, total = ? WHERE id = ?'
        cur.execute(sql, (jk.name, jk.size.id, jk.count, jk.id))
        self._conn.commit()

    def remove_jk(self, jk: JK):
        if jk.id == -1:
            return
        cur = self._conn.cursor()
        sql = 'DELETE FROM jk WHERE id = ?'
        cur.execute(sql, (jk.id,))
        self._conn.commit()

    def remove_jks(self, jks: List[JK]):
        cur = self._conn.cursor()
        sql = 'DELETE FROM jk WHERE id IN ({0})'.format(' ?' * len(jks))
        cur.execute(sql, [x.id for x in jks])
        self._conn.commit()


if __name__ == '__main__':
    db = Database(':memory:')
