from datetime import datetime

class GoodsType(object):

    def __init__(self, index, name):
        self._index = index
        self._name = name

    @property
    def index(self):
        return self._index

    @property
    def name(self):
        return self._name


class Goods(object):
    
    TYPES = [
        GoodsType(1, 'JK'),
        GoodsType(2, '小物')
    ]

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

    def all(self):
        results = []
        for row in self._driver.all_goods():
            g = self._goods_maker()
            g._id = row[0]
            g.name = row[1]
            g.goods_type = [x for x in self.TYPES if x.index == row[2]][0]
            g.create_time = row[3]
            g.comment = row[4]
            results.append(g)
        return results

    def _save_goods_data(self):
        def func(gd):
            # driver写入的数据只能使用基本类型，gd中的goods_type是GoodsType类型driver不支持
            # 需要使用一个空对象将基本数据类型传进去
            g = self._goods_maker()
            g.name = gd.name
            g.goods_type = gd.goods_type._index
            g.comment = gd.comment
            
            gd._id = self._driver.insert_goods(g)
        return func