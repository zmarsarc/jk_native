import unittest
from .sqlite import SQLiteDriver

class _TestGoods:

    def __init__(self, name, _type, comment = None):
        self.name = name
        self.goods_type = _type
        self.comment = comment

class TestSQLiteDriver(unittest.TestCase):

    def test_init_database(self):
        SQLiteDriver(':memory:')

    def test_insert_goods(self):
        driver = SQLiteDriver(":memory:")
        goods = _TestGoods('anderson', 1, 'some comment')
        driver.insert_goods(goods)

        result = driver._conn.execute('select * from goods').fetchone()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 'anderson')
        self.assertEqual(result[4], 'some comment')

    def test_insert_goods_no_comment(self):
        driver = SQLiteDriver(":memory:")
        goods = _TestGoods('anderson', 1)
        driver.insert_goods(goods)

        result = driver._conn.execute('select * from goods').fetchone()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 'anderson')
        self.assertIsNone(result[4])
    
    def test_insert_goods_return_id(self):
        driver = SQLiteDriver(":memory:")
        goods = _TestGoods('', 1)
        id = driver.insert_goods(goods)
        self.assertEqual(id, 1)