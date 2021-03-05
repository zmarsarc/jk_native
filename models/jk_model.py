from PySide6.QtCore import *

from models.database import Database
from models.jk import JK, JKSize
import time


class JKModel(QAbstractTableModel):

    _JK_NAME = 0
    _JK_SIZE_CODE = 1
    _JK_LENGTH = 2
    _JK_COUNT = 3
    _column_header = {
        _JK_NAME: '名字',
        _JK_SIZE_CODE: '尺码',
        _JK_LENGTH: '裙长',
        _JK_COUNT: '库存'
    }

    def __init__(self, db: Database, parent=None):
        super(JKModel, self).__init__(parent)
        self._db = db
        self._jks = None

    def rowCount(self, parent=...) -> int:
        if self._jks is None:
            self._jks = self._db.find_jk()
        return len(self._jks)

    def columnCount(self, parent=...) -> int:
        return len(self._column_header)

    def data(self, index: QModelIndex, role: int = ...) -> any:
        if not index.isValid():
            return None
        if index.row() >= len(self._jks):
            return None
        if index.column() >= len(self._column_header):
            return None
        if role == Qt.DisplayRole:
            # 第一列是名称，最后一列是库存，中间两列的数据通过jk_size查
            if index.column() == self._JK_NAME:
                return self._jks[index.row()].name
            if index.column() == self._JK_SIZE_CODE:
                return self._jks[index.row()].size.size_code
            if index.column() == self._JK_LENGTH:
                return self._jks[index.row()].size.length
            if index.column() == self._JK_COUNT:
                return self._jks[index.row()].count
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> any:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return self._column_header[section]
        else:
            if section >= len(self._jks):
                return None
            return self._jks[section].id

    def insertRows(self, row: int, count: int, parent: QModelIndex = ...) -> bool:
        return True

    def removeRow(self, row: int, parent: QModelIndex = ...) -> bool:
        return True

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return Qt.NoItemFlags
        if index.row() >= len(self._jks) or index.column() >= len(self._column_header):
            return Qt.NoItemFlags
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def setData(self, index: QModelIndex, value, role: int = ...) -> bool:
        if not index.isValid():
            return False
        if index.row() >= len(self._jks) or index.column() >= len(self._column_header):
            return False

        jk = self._jks[index.row()]
        if index.column() == self._JK_NAME:
            jk.name = str(value)
        elif index.column() == self._JK_SIZE_CODE:
            jk.size.size_code = str(value)
        elif index.column() == self._JK_LENGTH:
            jk.size.length = int(value)
        else:
            jk.count = int(value)

        self._edit_jk(jk)
        self.dataChanged.emit(index, index)
        return True

    def create_new_jk(self):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())

        new_size = JKSize('m', 42)
        new_size = self._db.add_new_jk_size(new_size)

        jk = JK('新JK'+str(time.time()), new_size, 0)
        jk = self._db.add_new_jk(jk)

        self._jks.append(jk)

        self.endInsertRows()

    def _edit_jk(self, jk: JK):
        # 如果设定了新的尺码，首先检查是否是权限全新尺码
        sizes = self._db.find_jk_size(jk.size.size_code, jk.size.length)
        if len(sizes) == 0:
            # 首先添加新尺码
            new_size = self._db.add_new_jk_size(JKSize(jk.size.size_code, jk.size.length))
            jk.size = new_size

        # 然后更新裙子信息
        self._db.update_jk(jk)
