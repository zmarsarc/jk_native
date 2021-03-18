from typing import Optional, List
from datetime import datetime
from abc import ABC, abstractmethod


class GoodsModel(object):

    """商品信息模型"""

    def __init__(self):
        self.id: int = -1
        self.name: str = None
        self.type: int = None
        self.create_time: datetime = None
        self.comment: Optional[str] = None


class GoodsDataDriver(ABC):

    """商品信息数据接口"""

    @abstractmethod
    def add_goods(self, goods: GoodsModel) -> int:
        pass

    @abstractmethod
    def all_goods(self) -> List[GoodsModel]:
        pass


class JKInventoryModel(object):

    """JK库存模型"""

    def __init__(self):
        self.id: int = -1
        self.goods_id: int = -1
        self.serial_number: str = None
        self.size_code: int = 0
        self.length: int = 0
        self.total: int = 0


class JKInventoryDataDriver(ABC):

    """JK库存信息接口"""

    @abstractmethod
    def add_jk_inventory(self, jk: JKInventoryModel) -> int:
        pass

    @abstractmethod
    def all_jk_inventory(self) -> List[JKInventoryModel]:
        pass
