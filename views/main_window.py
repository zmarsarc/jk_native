from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6.QtCore import Slot
from .ui_mainwindow import Ui_DressShopWindow
from .add_new_goods import AddNewGoodsDialog
from .add_jk_stock import AddJKStock
from models import goods, inventory
import data


class DressShopMainWindow(QMainWindow):

    def __init__(self, driver):
        super(DressShopMainWindow, self).__init__()

        self._current_goods: goods.Record = None
        self._data_driver = driver

        self.ui = Ui_DressShopWindow()
        self.ui.setupUi(self)

        self.ui.btn_add_new_goods.clicked.connect(self.add_new_goods)
        self.ui.btn_new_stock.clicked.connect(self.add_stock)
        self._goods_model = goods.Goods(self._data_driver, self)
        self.ui.goods_view.setModel(self._goods_model)
        self.ui.goods_view.selectedGoodsChanged.connect(self.selected_goods_changed)

    @Slot()
    def add_new_goods(self):
        """添加新商品"""

        dialog = AddNewGoodsDialog(goods.GoodsType.Types, self)
        result = dialog.exec_()
        if result == QDialog.Accepted:
            name, gtype, comment = dialog.goods_data()
            self._goods_model.add_new_goods(name, gtype, comment)

    @Slot()
    def add_stock(self):
        if self._current_goods is None:
            return #  todo: show usage hit
        
        #  todo: select dialog depend on different types of goods
        if self._current_goods.type == goods.GoodsType.JK:
            dialog = AddJKStock(inventory.JKSize.Sizes)
            if QDialog.Accepted == dialog.exec_():
                jk = inventory.JKForGoods(self._data_driver, self._current_goods).new()
                jk.size, jk.length, jk.total = dialog.jk_data()
                jk.save()

    @Slot(object)
    def selected_goods_changed(self, goods):
        self._current_goods = goods
        self.ui.dock_goods_detail.setWindowTitle(f'{goods.type.name}-{goods.name}的库存')
        jk = inventory.JKForGoods(self._data_driver, goods)
        self.ui.inventory_view.setModel(jk)
