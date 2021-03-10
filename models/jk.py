class JKSize(object):

    _max_dress_length = 70  # 最大裙长，单位厘米
    _min_dress_length = 20  # 最小裙长，单位厘米

    def __init__(self, size_code: str, length: int, _id=-1):
        self.size_code: str = size_code
        self.length = length
        self._id = _id

    @property
    def size_code(self) -> str:
        return self._size_code.upper()

    @size_code.setter
    def size_code(self, code):
        if code.lower() not in ('xs', 's', 'm', 'l', 'xl'):
            raise ValueError("not support size code" + code)
        self._size_code = code

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, dl):
        if not self._min_dress_length < dl < self._max_dress_length:
            raise ValueError("dress too short or too long")
        self._length = dl

    @property
    def id(self):
        return self._id


class JK(object):

    def __init__(self, name: str, size: JKSize, count: int, _id=-1):
        self.name = name
        self.size = size
        self.count = count
        self._id = _id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        if _name == '':
            raise ValueError('jk name should be specified')
        self._name = _name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, _size):
        if not isinstance(_size, JKSize):
            raise TypeError('size should be a JKSize')
        if _size.id == -1:
            raise ValueError('size not exists, add new size first')
        self._size = _size

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, _count):
        if _count < 0:
            raise ValueError('count should greater then 0')
        self._count = _count

    @property
    def id(self):
        return self._id
