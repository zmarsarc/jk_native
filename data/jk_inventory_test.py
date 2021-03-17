import unittest
from unittest.mock import MagicMock
from .jk_inventory import JK

class _FakeDriver(object):

    def __init__(self):
        self.insert_jk = MagicMock(return_value=3)

        all_jk = (
            (1, 1, '1111', 1, 43, 100),
            (2, 1, '1112', 1, 47, 59),
            (3, 2, '1121', 2, 39, 100)
        )
        self.all_jk = MagicMock(return_value=all_jk)


class TestJK(unittest.TestCase):

    def test_new_jk(self):
        jk_data = JK(_FakeDriver())
        jk = jk_data.new()
        jk.goods_id = 1
        jk.serial_number = '1111'
        jk.size = jk_data.Sizes[0]
        jk.length = 42
        jk.count = 100
        jk.save()

        self.assertEqual(jk._id, 3)

    def test_new_jk_arg(self):
        fake = _FakeDriver()

        jk_data = JK(fake)
        jk = jk_data.new()
        jk.goods_id = 1
        jk.serial_number = '111'
        jk.size = jk_data.Sizes[0]
        jk.length = 42
        jk.count = 100
        jk.save()

        arg = fake.insert_jk.call_args[0][0]
        self.assertTrue(hasattr(arg, 'goods_id') and isinstance(arg.goods_id, int))
        self.assertTrue(hasattr(arg, 'serial_number') and isinstance(arg.serial_number, str))
        self.assertTrue(hasattr(arg, 'size_code') and isinstance(arg.size_code, int))
        self.assertTrue(hasattr(arg, 'length') and isinstance(arg.length, int))
        self.assertTrue(hasattr(arg, 'total') and isinstance(arg.total, int))

    def test_all(self):
        fake = _FakeDriver()
        jk_data = JK(fake)

        jks = jk_data.all()
        self.assertEqual(jks[0]._id, 1)
        self.assertEqual(jks[1].size.name, 'XS')
        self.assertEqual(jks[2].count, 100)