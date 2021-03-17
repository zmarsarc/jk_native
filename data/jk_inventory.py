class JKSize(object):

    def __init__(self, code: int, name: str):
        self._code = code
        self._name = name

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self._name


class JK(object):

    Sizes = [
        JKSize(1, 'XS'),
        JKSize(2, 'S'),
        JKSize(3, 'M'),
        JKSize(4, 'L'),
        JKSize(5, 'XL'),
        JKSize(6, 'XXL')
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

    def _save_jk_data(self):
        def func(jk):
            model = self._JKModel(jk)
            jk._id = self._driver.insert_jk(model)
        return func