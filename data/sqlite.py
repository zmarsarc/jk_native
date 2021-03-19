import sqlite3
from datetime import datetime
from .abc import *

class SQLiteDriver(GoodsDataDriver, JKInventoryDataDriver):

    def __init__(self, dbname:str):
        self._conn = sqlite3.connect(dbname)
        with open('data/tables.sql', encoding='utf-8') as script:
            self._conn.executescript(script.read())

        # 打开sqlite的外键检查，会降低一些数据库性能不过我们是本地应用不差钱
        self._conn.execute('PRAGMA foreign_keys = ON')
    
    def add_goods(self, goods: GoodsModel) -> int:
        cur = self._conn.cursor()
        if hasattr(goods, 'comment') and goods.comment is not None:
            cur.execute('insert into goods (name, goods_type, comment) values (?, ?, ?)',
            (goods.name, goods.type, goods.comment))
        else:
            cur.execute('insert into goods (name, goods_type) values (?, ?)',
            (goods.name, goods.type))
        self._conn.commit()
        return cur.lastrowid

    def all_goods(self) -> List[GoodsModel]:
        cur = self._conn.cursor()
        cur.execute('select id, name, goods_type, create_time, comment from goods')
        goods = []
        for d in cur.fetchall():
            goods.append(self._load_goods_to_model(d))
        return goods

    @staticmethod
    def _load_goods_to_model(d: tuple) -> GoodsModel:
        ID = 0
        NAME = 1
        TYPE_CODE = 2
        CTIME = 3
        COMMENT = 4

        g = GoodsModel()
        g.id = d[ID]
        g.name = d[NAME]
        g.type = d[TYPE_CODE]
        g.create_time = datetime.fromisoformat(d[CTIME])
        g.comment = d[COMMENT]

        return g

    def add_jk_inventory(self, jk: JKInventoryModel):
        cur = self._conn.cursor()
        sql = 'insert into jk_inventory (goods_id, serial_number, size_code, length, total) \
            values (?, ?, ?, ?, ?)'
        cur.execute(sql, (jk.goods_id, jk.serial_number, jk.size_code, jk.length, jk.total))
        self._conn.commit()
        return cur.lastrowid

    def all_jk_inventory(self) -> List[JKInventoryModel]:
        cur = self._conn.cursor()
        cur.execute('select id, goods_id, serial_number, size_code, length, total from jk_inventory')
        jks = []
        for d in cur.fetchall():
            jks.append(self._load_data_to_jk_inventory_model(d))
        return jks

    def jk_inventory_by_goods_id(self, goods_id: int) -> List[JKInventoryModel]:
        cur = self._conn.cursor()
        cur.execute('select id, goods_id, serial_number, size_code, length, total from jk_inventory where goods_id = ?',
            (goods_id,))
        jks = []
        for d in cur.fetchall():
            jks.append(self._load_data_to_jk_inventory_model(d))
        return jks

    @staticmethod
    def _load_data_to_jk_inventory_model(d):
        ID = 0
        GOODS_ID = 1
        SERIAL = 2
        SIZE = 3
        LEN = 4
        COUNT = 5

        j = JKInventoryModel()
        j.id = d[ID]
        j.goods_id = d[GOODS_ID]
        j.serial_number = d[SERIAL]
        j.size_code = d[SIZE]
        j.length = d[LEN]
        j.total = d[COUNT]

        return j
