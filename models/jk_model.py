from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models.database import Database


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
            if index.row() == 0 or index.row() == 3:
                return self._jks[index.row()][index.column()]
            else:
                size = self._db.get_jk_size(self._jks[index.row()].size)
                if index.row == 1:
                    return size.size_code
                else:
                    return size.length
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...) -> any:
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ['名称', '尺码', '裙长', '库存'][section]
        else:
            return self._jks[section].id
