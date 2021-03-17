import unittest
from unittest.mock import MagicMock
from .jk_inventory import JK

class _FakeDriver(object):

    def __init__(self):
        self.insert_jk = MagicMock(return_value=3)


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
