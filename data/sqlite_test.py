import unittest
from .sqlite import SQLiteDriver

class _TestGoods:

    def __init__(self, name, _type, comment = None):
        self.name = name
        self.goods_type = _type
        self.comment = comment

class _TestJK:

    def __init__(self, goods_id, serial_number, size_code, length, total):
        self.goods_id = goods_id
        self.serial_number = serial_number
        self.size_code = size_code
        self.length = length
        self.total = total


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

    def test_insert_and_read_jk(self):
        driver = SQLiteDriver(":memory:")
        goods = _TestGoods('', 1)
        goods_id = driver.insert_goods(goods)

        jk = _TestJK(goods_id, '1111', 1, 2, 3)
        id = driver.insert_jk(jk)

        self.assertEqual(id, 1)

        jks = driver.all_jk()[0]
        self.assertEqual(jks[0], id)  # check id
        self.assertEqual(jks[1], goods_id)  # check goods id
        self.assertEqual(jks[2], '1111')  # check serial number
        self.assertEqual(jks[3], 1)  # check size code
        self.assertEqual(jks[4], 2)  # check length
        self.assertEqual(jks[5], 3)  # check total
