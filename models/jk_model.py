from PySide6.QtCore import *

from models.database import Database
from models.jk import JK, JKSize


class JKModel(QAbstractTableModel):

    def __init__(self, db: Database, parent=None):
        super(JKModel, self).__init__(parent)
        self._db = db
        self._jks = None

    def rowCount(self, parent=...) -> int:
        if self._jks is None:
            self._jks = self._db.find_jk()
        return len(self._jks)

    def columnCount(self, parent=...) -> int:
        # 总是4，名称，尺码，裙长和库存
        return 4

    def data(self, index: QModelIndex, role: int = ...) -> any:
        if not index.isValid():
            return None
        if index.row() >= len(self._jks):
            return None
        if index.column() >= 4:
            return None
        if role == Qt.DisplayRole:
            # 第一列是名称，最后一列是库存，中间两列的数据通过jk_size查
            if index.column() == 0:
                return self._jks[index.row()].name
            if index.column() == 1:
                return self._jks[index.row()].size.size_code
            if index.column() == 2:
                return self._jks[index.row()].size.length
            if index.column() == 3:
                return self._jks[index.row()].count
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> any:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ['名称', '尺码', '裙长', '库存'][section]
        else:
            if section >= len(self._jks):
                return None
            return self._jks[section].id

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        self.beginInsertRows(parent, 0, 1)
        self._jks.append(JK('新jk', JKSize('m', 42, 1), 0))
        self.endInsertRows()
        return True

    def insertColumn(self, column: int, parent: QModelIndex = ...) -> bool:
        return True

    def removeRow(self, row: int, parent: QModelIndex = ...) -> bool:
        return True

    def removeColumn(self, column: int, parent: QModelIndex = ...) -> bool:
        return True
