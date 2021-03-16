import sqlite3

class SQLiteDriver(object):

    def __init__(self, dbname:str):
        self._conn = sqlite3.connect(dbname)
        with open('data/tables.sql', encoding='utf-8') as script:
            self._conn.executescript(script.read())
        self._conn.commit()
    
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