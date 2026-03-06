import unittest

from src.func_to_test import test_func_1, test_func_2

class test_test_1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(test_func_1(2,3), 5)

    def test_2(self):
        self.assertEqual(test_func_2(5), 7)

if __name__ == '__main__':
    unittest.main(verbosity = 2)
