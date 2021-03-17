import unittest
from unittest.mock import MagicMock
from .jk_inventory_model import JKInventory
from data import JK, JKSize
from PySide6.QtCore import Qt


class _FakeGoods(object):

    def __init__(self):
        jk = JK(None)

        a = jk.new()
        a.size = JKSize(1, 'S', 1)
        a.length = 1
        a.count = 1

        b = jk.new()
        b.size = JKSize(2, 'M', 2)
        b.length = 2
        b.count = 1

        c = jk.new()
        c.size = JKSize(3, 'L', 3)
        c.length = 3
        c.count = 1

        d = jk.new()
        d.size = c.size
        d.length = 4
        d.count = 1

        self.inventory = MagicMock(return_value=[a, b, c, d])

class TestJKInventory(unittest.TestCase):

    def test_rowCount(self):
        fake = _FakeGoods()
        jk = JKInventory(fake)
        self.assertEqual(jk.rowCount(), 3)

    def test_columnCount(self):
        fake = _FakeGoods()
        jk = JKInventory(fake)
        self.assertEqual(jk.columnCount(), 4)

    def test_date(self):
        #   1  2  3  4
        # S 1
        # M    1
        # L       1  1
        fake = _FakeGoods()
        jk = JKInventory(fake)

        index = jk.createIndex(0, 0, jk)
        self.assertEqual(jk.data(index, Qt.DisplayRole), 1)

        index = jk.createIndex(1, 1, jk)
        self.assertEqual(jk.data(index, Qt.DisplayRole), 1)

        index = jk.createIndex(2, 1, jk)
        self.assertEqual(jk.data(index, Qt.DisplayRole), 0)

    def test_headerData(self):
        fake = _FakeGoods()
        jk = JKInventory(fake)

        self.assertEqual(jk.headerData(0, Qt.Horizontal, Qt.DisplayRole), 1)
        self.assertEqual(jk.headerData(1, Qt.Vertical, Qt.DisplayRole), 'M')
        self.assertEqual(jk.headerData(3, Qt.Vertical, Qt.DisplayRole), None)
        self.assertEqual(jk.headerData(2, Qt.Vertical, Qt.EditRole), None)