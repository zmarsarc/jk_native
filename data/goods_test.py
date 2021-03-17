import unittest
from unittest.mock import MagicMock
from .goods import Goods

class _FakeDriver(object):
    
    def __init__(self):
        self.insert_goods = MagicMock(return_value=1)


class TestGoods(unittest.TestCase):

    def test_new_inventory_from_jk_goods(self):
        goods = Goods(_FakeDriver())
        g = goods.new()
        g.name = 'jk'
        g.goods_type = goods.TYPES[0]
        g.save()

        jk = g.new_inventory()
        self.assertEqual(jk.goods_id, 1)
