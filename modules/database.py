import sqlite3
from jk import JKSize


class Database(object):

    _jk_size_scheme = "CREATE TABLE if not EXISTS jk_size(id integer primary key AUTOINCREMENT," \
                      "size varchar(5) not NULL," \
                      "length integer not NULL DEFAULT(42)," \
                      "CHECK(size IN ('xs', 's', 'm', 'l', 'xl')));"

    _jk_scheme = 'CREATE TABLE if not EXISTS jk(id integer primary key AUTOINCREMENT,' \
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
        _id = cur.execute('INSERT INTO jk_size(size, length) VALUES (?, ?);', (size.size_code, size.length)).lastrowid
        return JKSize(size.size_code, size.length, _id)

    no_matter_how_long = -1
    no_matter_what_size = ''

    def find_jk_size(self, size_code=no_matter_what_size, length=no_matter_how_long) -> list:
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


if __name__ == '__main__':
    db = Database(':memory:')
