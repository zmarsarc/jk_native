from typing import Dict
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
import data


class GoodsType(object):

    """
    商品类型类

    两个字段，是商品类型的两种表示。
    
    code是数据表示，每种商品类型都有不重复的类型码，name是人类可读的表示，例如 JK Lo 小物等等。
    """

    def __init__(self, code: int, name: str):
        self._type_code: int = code
        self._type_name: str = name

    @property
    def code(self):
        return self._type_code

    @property
    def name(self):
        return self._type_name


# 下面定义商品类型
GoodsTypeJK: GoodsType = GoodsType(1, u'JK')
GoodsTypeAccessoires: GoodsType = GoodsType(2, u'小物')

# 定义两个辅助索引用于查询类型
NameToGoodsType: Dict[str, GoodsType] = {
    GoodsTypeJK.name: GoodsTypeJK,
    GoodsTypeAccessoires.name: GoodsTypeAccessoires
}
CodeToGoodsType: Dict[int, GoodsType] = {
    GoodsTypeJK.code: GoodsTypeJK,
    GoodsTypeAccessoires.code: GoodsTypeAccessoires
}


class Goods(QAbstractTableModel):

    _header_data = ('名称', '类型', '创建时间', '备注')

    def __init__(self, goodsdata: data.Goods, parent=None):
        super(Goods, self).__init__(parent)
        self._goods_data = goodsdata
        self._goods = None
        
    def rowCount(self, parent=QModelIndex()):
        if self._goods is None:
            self._goods = self._goods_data.all()
        return len(self._goods)

    def columnCount(self, parent=QModelIndex()):
        return len(self._header_data)

    def data(self, index: QModelIndex, role=...):
        if not index.isValid():
            return None
        if index.row() >= self.rowCount() or index.column() >= len(self._header_data):
            return None
        if role == Qt.DisplayRole:
            g = self._goods[index.row()]
            if index.column() == 0:
                return g.name
            elif index.column() == 1:
                return g.goods_type.name
            elif index.column() == 2:
                return g.create_time
            else:
                return g.comment if g.comment is not None else ''
        if role == Qt.EditRole:
            return self._goods[index.row()]
    
    def headerData(self, section, orientation, role=...):
        if orientation == Qt.Vertical:
            return None
        if role == Qt.DisplayRole and section < len(self._header_data):
            return self._header_data[section]
        return None

    def add_new_goods(self, gd):
        self.beginInsertRows(QModelIndex(), self.rowCount()+1, self.rowCount()+1)
        g = self._goods_data.new()
        g.name = gd['name']
        g.goods_type = gd['goods_type']
        g.comment = gd['comment']
        g.save()

        self._goods = self._goods_data.all()

        self.endInsertRows()
    
    def types(self):
        return data.Goods.TYPES