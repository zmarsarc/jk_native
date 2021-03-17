import sqlite3

class SQLiteDriver(object):

    def __init__(self, dbname:str):
        self._conn = sqlite3.connect(dbname)
        with open('data/tables.sql', encoding='utf-8') as script:
            self._conn.executescript(script.read())

        # 打开sqlite的外键检查，会降低一些数据库性能不过我们是本地应用不差钱
        self._conn.execute('PRAGMA foreign_keys = ON')
    
    def insert_goods(self, goods):
        cur = self._conn.cursor()
        if hasattr(goods, 'comment') and goods.comment is not None:
            cur.execute('insert into goods (name, goods_type, comment) values (?, ?, ?)',
            (goods.name, goods.goods_type, goods.comment))
        else:
            cur.execute('insert into goods (name, goods_type) values (?, ?)',
            (goods.name, goods.goods_type))
        self._conn.commit()
        return cur.lastrowid

    def all_goods(self):
        cur = self._conn.cursor()
        cur.execute('select id, name, goods_type, create_time, comment from goods')
        return cur.fetchall()

    def insert_jk(self, jk):
        cur = self._conn.cursor()
        sql = 'insert into jk_inventory (goods_id, serial_number, size_code, length, total) \
            values (?, ?, ?, ?, ?)'
        cur.execute(sql, (jk.goods_id, jk.serial_number, jk.size_code, jk.length, jk.total))
        self._conn.commit()
        return cur.lastrowid

    def all_jk(self):
        cur = self._conn.cursor()
        cur.execute('select id, goods_id, serial_number, size_code, length, total from jk_inventory')
        return cur.fetchall()