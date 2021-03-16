import unittest
from .sqlite import SQLiteDriver

class TestSQLiteDriver(unittest.TestCase):

    def test_init_database(self):
        SQLiteDriver(':memory:')

    def test_insert_goods(self):
        driver = SQLiteDriver(":memory:")
        goods = type('g', (object,), {
            'name': 'anderson',
            'goods_type': 1,
            'comment': 'some comment'
        })()
        driver.insert_goods(goods)

        result = driver._conn.execute('select * from goods').fetchone()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 'anderson')
        self.assertEqual(result[4], 'some comment')

    def test_insert_goods_no_comment(self):
        driver = SQLiteDriver(":memory:")
        goods = type('g', (object,), {
            'name': 'anderson',
            'goods_type': 1,
        })()
        driver.insert_goods(goods)

        result = driver._conn.execute('select * from goods').fetchone()
        self.assertEqual(result[0], 1)
        self.assertEqual(result[1], 'anderson')
        self.assertIsNone(result[4])