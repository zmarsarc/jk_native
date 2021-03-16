from datetime import datetime

class Goods(object):
    
    def __init__(self, driver):
        self._driver = driver
        _goods_data_attrs = {
            '_id': None,
            'name': None,
            'goods_type': None,
            'create_time': None,
            'comment': None,
            'save': self._save_goods_data()
        }
        self._goods_maker = type('GoodsData', (object,), _goods_data_attrs)

    def new(self):
        return self._goods_maker()

    def _save_goods_data(self):
        def func(gd):
            gd._id = self._driver.insert_goods(gd)
        return func