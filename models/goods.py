from typing import Dict, Optional, List
from abc import abstractmethod
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from datetime import datetime
import data

class GoodsType:

    class _Type:
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
    JK = _Type(1, u'JK')
    Accessories = _Type(2, u'小物')

    # 两个辅助查询的字典
    NameToType: Dict[str, _Type] = {
        JK.name: JK,
        Accessories.name: Accessories
    }
    CodeToType: Dict[int, _Type] = {
        JK.code: JK,
        Accessories.code: Accessories
    }


class DataDriver(data.GoodsDataDriver, data.JKInventoryDataDriver):
    pass


class GoodsItem:
    
    def __init__(self, model: data.GoodsModel = None):
        if model is not None:
            self._data = model
        else:
            self._data = data.GoodsModel()
        
    @property
    def id(self) -> int:
        return self._data.id
    
    @property
    def name(self) -> str:
        return self._data.name
    
    @name.setter
    def name(self, n: str):
        self._data.name = n

    @property
    def type(self) -> GoodsType._Type:
        return GoodsType.CodeToType[self._data.type]
    
    @type.setter
    def type(self, t: GoodsType):
        #  todo: 如果商品已经创建了，就不能再修改其类型了
        pass

    @property
    def create_time(self) -> datetime:
        return self._data.create_time

    @property
    def comment(self) -> Optional[str]:
        return self._data.comment

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def remove(self):
        pass


class JKItem(GoodsItem):

    def __init__(self, driver: data.JKInventoryDataDriver, model: data.GoodsModel=None):
        super(JKItem, self).__init__(model)
        self._driver = driver

    def save(self):
        pass

    def remove(self):
        pass


class AccessoiresItem(GoodsItem):

    def __init__(self, model: data.GoodsModel=None):
        super(AccessoiresItem, self).__init__(model)

    def save(self):
        pass

    def remove(self):
        pass


class Goods(QAbstractTableModel):

    _header_data = ('名称', '类型', '创建时间', '备注')

    def __init__(self, driver: DataDriver, parent=None):
        super(Goods, self).__init__(parent)
        self._data = driver
        self._goods = self._load()

    def _load(self) -> List[GoodsItem]:
        goods: List[GoodsItem] = []
        for g in self._data.all_goods():
            if g.type == GoodsType.JK.code:
                goods.append(JKItem(self._data, g))
            if g.type == GoodsType.Accessories.code:
                goods.append(AccessoiresItem(g))
        return goods
        
    def rowCount(self, parent=QModelIndex()):
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
                return g.type.name
            elif index.column() == 2:
                return str(g.create_time)
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
        g = self._data.new()
        g.name = gd['name']
        g.goods_type = gd['goods_type']
        g.comment = gd['comment']
        g.save()

        self._goods = self._data.all()

        self.endInsertRows()
