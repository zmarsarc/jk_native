import unittest
from jk import JKSize


class JKSizeTestCase(unittest.TestCase):
    def test_new_jk_size_not_support(self):
        self.assertRaises(ValueError, lambda: JKSize('XXX', 42))

    def test_new_jk_length_not_support(self):
        self.assertRaises(ValueError, lambda: JKSize('x', 10))


if __name__ == '__main__':
    unittest.main()
