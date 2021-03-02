import unittest
from database import Database
from jk import JKSize


class DatabasesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.db = Database(':memory:')

    def test_write_read_jk_size(self):
        size = JKSize('s', 42)
        ret = self.db.add_new_jk_size(size)
        self.assertEqual(ret.id, 1)

        sizes = self.db.find_jk_size()
        self.assertEqual(len(sizes), 1)
        self.assertEqual(sizes[0].size_code, 's')
        self.assertEqual(sizes[0].length, 42)


if __name__ == '__main__':
    unittest.main()
