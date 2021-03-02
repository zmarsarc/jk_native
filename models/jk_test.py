import unittest
from jk import JKSize, JK


class JKSizeTestCase(unittest.TestCase):
    def test_new_jk_size_not_support(self):
        self.assertRaises(ValueError, lambda: JKSize('XXX', 42))

    def test_new_jk_length_not_support(self):
        self.assertRaises(ValueError, lambda: JKSize('x', 10))


class JKTestCase(unittest.TestCase):
    def test_new_jk(self):
        size = JKSize('s', 42, 1)
        jk = JK('闪光少女', size, 10)
        self.assertEqual(jk.count, 10)


if __name__ == '__main__':
    unittest.main()
