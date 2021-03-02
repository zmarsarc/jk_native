class JKSize(object):

    _max_dress_length = 70  # 最大裙长，单位厘米
    _min_dress_length = 20  # 最小裙长，单位厘米

    def __init__(self, size_code: str, length: int, _id=-1):
        self.size_code = size_code
        self.length = length
        self._id = _id

    @property
    def size_code(self):
        return self._size_code

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

    def __init__(self, name: str, size: JKSize, count: int):
        self._name = name
        self._size = size
        self._count = count
