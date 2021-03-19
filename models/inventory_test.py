import unittest
from unittest.mock import MagicMock
from PySide6.QtCore import Qt
from .inventory import JK, JKSize, JKInventoryModel

class _FakeGoods:

    def __init__(self):
        a = JKInventoryModel()
        a.size_code = JKSize.S.code
        a.length = 1
        a.total = 1

        b = JKInventoryModel()
        b.size_code = JKSize.M.code
        b.length = 2
        b.total = 1

        c = JKInventoryModel()
        c.size_code = JKSize.L.code
        c.length = 3
        c.total = 1

        d = JKInventoryModel()
        d.size_code = c.size_code
        d.length = 4
        d.total = 1

        self.all_jk_inventory = MagicMock(return_value=[a, b, c, d])


class TestJK(unittest.TestCase):

    def test_rowCount(self):
        fake = _FakeGoods()
        jk = JK(fake)
        self.assertEqual(jk.rowCount(), 3)

    def test_columnCount(self):
        fake = _FakeGoods()
        jk = JK(fake)
        self.assertEqual(jk.columnCount(), 4)

    def test_date(self):
        #   1  2  3  4
        # S 1
        # M    1
        # L       1  1
        fake = _FakeGoods()
        jk = JK(fake)

        index = jk.createIndex(0, 0, jk)
        self.assertEqual(jk.data(index, Qt.DisplayRole), 1)

        index = jk.createIndex(1, 1, jk)
        self.assertEqual(jk.data(index, Qt.DisplayRole), 1)

        index = jk.createIndex(2, 1, jk)
        self.assertEqual(jk.data(index, Qt.DisplayRole), 0)

    def test_headerData(self):
        fake = _FakeGoods()
        jk = JK(fake)

        self.assertEqual(jk.headerData(0, Qt.Horizontal, Qt.DisplayRole), 1)
        self.assertEqual(jk.headerData(1, Qt.Vertical, Qt.DisplayRole), 'M')
        self.assertEqual(jk.headerData(3, Qt.Vertical, Qt.DisplayRole), None)
        self.assertEqual(jk.headerData(2, Qt.Vertical, Qt.EditRole), None)