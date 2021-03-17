from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

class JKInventory(QAbstractTableModel):

    def __init__(self, goods, parent=None):
        super(JKInventory, self).__init__(parent)
        self._goods = goods
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

    def _update_table(self):
        self._inventory = self._goods.inventory()

        # 计算列的标头，列标识裙长
        h_header = list(set([x.length for x in self._inventory]))
        h_header.sort()

        # 计算行的标头，行标识尺码
        v_header = list(set([x.size for x in self._inventory]))
        v_header.sort(key=lambda x: x.order)

        # 创建表
        table = [[0 for x in h_header] for x in v_header]
        for i in self._inventory:
            row = v_header.index(i.size)
            col = h_header.index(i.length)
            table[row][col] += i.count
        
        return (h_header, v_header, table)