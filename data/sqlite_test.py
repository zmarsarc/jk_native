import unittest
from .sqlite import SQLiteDriver
from .abc import *


class TestSQLiteDriver(unittest.TestCase):

    def test_init_database(self):
        SQLiteDriver(':memory:')

    def test_insert_goods(self):
        driver = SQLiteDriver(":memory:")
        goods = GoodsModel()
        goods.name = 'anderson'
        goods.type = 1
        goods.comment = 'some comment'

        driver.add_goods(goods)

        result = driver._conn.execute('select * from goods').fetchone()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 'anderson')
        self.assertEqual(result[4], 'some comment')

    def test_insert_goods_no_comment(self):
        driver = SQLiteDriver(":memory:")
        goods = GoodsModel()
        goods.name = 'anderson'
        goods.type = 1
        driver.add_goods(goods)

        result = driver._conn.execute('select * from goods').fetchone()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 'anderson')
        self.assertIsNone(result[4])
    
    def test_insert_goods_return_id(self):
        driver = SQLiteDriver(":memory:")
        goods = GoodsModel()
        goods.name = ''
        goods.type = 1
        id = driver.add_goods(goods)
        self.assertEqual(id, 1)

    def test_insert_and_read_jk(self):
        driver = SQLiteDriver(":memory:")
        goods = GoodsModel()
        goods.name = ''
        goods.type = 1
        goods_id = driver.add_goods(goods)

        jk = JKInventoryModel()
        jk.goods_id = goods_id
        jk.serial_number = '1111'
        jk.size_code = 1
        jk.length = 2
        jk.total = 3
        id = driver.add_jk_inventory(jk)

        self.assertEqual(id, 1)

        jks: JKInventoryModel = driver.all_jk_inventory()[0]
        self.assertEqual(jks.id, id)  # check id
        self.assertEqual(jks.goods_id, goods_id)  # check goods id
        self.assertEqual(jks.serial_number, '1111')  # check serial number
        self.assertEqual(jks.size_code, 1)  # check size code
        self.assertEqual(jks.length, 2)  # check length
        self.assertEqual(jks.total, 3)  # check total

    def test_read_goods_should_return_datetime_ctime(self):
        driver = SQLiteDriver(":memory:")
        goods = GoodsModel()
        goods.name = ''
        goods.type = 1
        goods_id = driver.add_goods(goods)

        g = driver.all_goods()[0]
        self.assertIsInstance(g.create_time, datetime)