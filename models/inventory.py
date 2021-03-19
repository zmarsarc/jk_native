from typing import List
from data import JKInventoryDataDriver, JKInventoryModel
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from . import goods

class JKSize:

    class Size:

        """
        JK尺码

        描述JK的尺码，将机器表示和人类表示组合在一起。

        字段code表示机器表示，用来写入存储器，
        字段name是人类可读的表示，用于ui，
        index是用来给尺码排序的键。
        """

        def __init__(self, code: int, name: str, index: int):
            self._code = code
            self._name = name
            self._index = index

        @property
        def code(self):
            return self._code

        @property
        def name(self):
            return self._name

        @property
        def index(self):
            return self._index
    
    XS = Size(1, 'XS', 1)
    S = Size(2, 'S', 2)
    M = Size(3, 'M', 3)
    L = Size(4, 'L', 4)
    XL = Size(5, 'XL', 5)

    Sizes = [XS, S, M, L, XL]

    # 通过code查尺码
    CodeToSize = {
        XS.code: XS,
        S.code: S,
        M.code: M,
        L.code: L,
        XL.code: XL
    }


class Record:
    
    def __init__(self, driver: JKInventoryDataDriver, model: JKInventoryModel = None):
        self._driver = driver
        self._data = model
        if self._data is None:
            self._data = JKInventoryModel()

    @property
    def id(self):
        return self._data.id

    @property
    def goods_id(self):
        return self._data.goods_id

    @property
    def serial_number(self):
        return self._data.serial_number

    @property
    def size(self):
        return JKSize.CodeToSize[self._data.size_code]

    @property
    def length(self):
        return self._data.length

    @property
    def total(self):
        return self._data.total


class JK(QAbstractTableModel):

    def __init__(self, driver: JKInventoryDataDriver, parent=None):
        super(JK, self).__init__(parent)
        self._driver = driver
        self._inventory = None
        self._h_header, self._v_header, self._table = self._update_table()
    
    def rowCount(self, parent=QModelIndex()):
        return len(self._v_header)

    def columnCount(self, parent=QModelIndex()):
        return len(self._h_header)

    def data(self, index: QModelIndex, role=...):
        if not index.isValid():
            return None
        if index.row() >= self.rowCount() or index.column() >= self.columnCount():
            return None
        if role == Qt.DisplayRole:
            return self._table[index.row()][index.column()]

    def headerData(self, section: int, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            if 0 <= section < len(self._h_header):
                return self._h_header[section]
        else:
            if 0 <= section < len(self._v_header):
                return self._v_header[section].name
        return None

    def _load(self) -> List[Record]:
        return [Record(self._driver, x) for x in self._driver.all_jk_inventory()]

    def _update_table(self):
        self._inventory = self._load()

        # 计算列的标头，列标识裙长
        h_header = list(set([x.length for x in self._inventory]))
        h_header.sort()

        # 计算行的标头，行标识尺码
        v_header = list(set([x.size for x in self._inventory]))
        v_header.sort(key=lambda x: x.index)

        # 创建表
        table = [[0 for x in h_header] for x in v_header]
        for i in self._inventory:
            row = v_header.index(i.size)
            col = h_header.index(i.length)
            table[row][col] += i.total
        
        return (h_header, v_header, table)


class JKForGoods(JK):

    def __init__(self, driver: JKInventoryDataDriver, record: goods.Record, parent=None):
        self._goods_record = record
        super(JKForGoods, self).__init__(driver, parent)

    def _load(self):
        return [Record(self._driver, x) for x in self._driver.jk_inventory_by_goods_id(self._goods_record.id)]
