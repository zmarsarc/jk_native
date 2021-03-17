class JKSize(object):

    def __init__(self, code: int, name: str, order: int):
        self._code = code
        self._name = name
        self._order = order

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def order(self):
        return self._order

    def __str__(self):
        return self._name


class JK(object):

    Sizes = [
        JKSize(1, 'XS', 0),
        JKSize(2, 'S', 1),
        JKSize(3, 'M', 2),
        JKSize(4, 'L', 3),
        JKSize(5, 'XL', 4),
        JKSize(6, 'XXL', 5)
    ]

    class _JKModel(object):

        def __init__(self, jk):
            self.goods_id = jk.goods_id
            self.serial_number = jk.serial_number
            self.size_code = jk.size.code
            self.length = jk.length
            self.total = jk.count

    def __init__(self, driver):
        self._driver = driver
        jk_data_attrs = {
            '_id': None,
            'goods_id': None,
            'serial_number': None,
            'size': None,
            'length': None,
            'count': None,
            'save': self._save_jk_data()
        }
        self._jk_data_maker = type('JKData', (object,), jk_data_attrs)
    
    def new(self):
        return self._jk_data_maker()

    def all(self):
        data = self._driver.all_jk()
        result = []
        for d in data:
            j = self._jk_data_maker()
            j._id = d[0]
            j.goods_id = d[1]
            j.serial_number = d[2]
            j.size = [x for x in self.Sizes if x.code == d[3]][0]
            j.length = d[4]
            j.count = d[5]
            
            result.append(j)

        return result

    def _save_jk_data(self):
        def func(jk):
            model = self._JKModel(jk)
            jk._id = self._driver.insert_jk(model)
        return func