import unittest
from BIT import *

class TestBIT(unittest.TestCase):
    def test_get_sum(self):
        """区間和のテスト"""
        SIZE = 5
        bit = BIT(SIZE)
        bit.add(1, 3)
        bit.add(2, 2)
        bit.add(3, 5)
        bit.add(4, 1)
        bit.add(5, 5)

        self.assertEqual(bit.get_sum(1), 3)
        self.assertEqual(bit.get_sum(2), 5)
        self.assertEqual(bit.get_sum(3), 10)
        self.assertEqual(bit.get_sum(4), 11)
        self.assertEqual(bit.get_sum(5), 16)

        self.assertEqual(bit.get_sum(1, 5), 16)
        self.assertEqual(bit.get_sum(2, 4), 8)
        self.assertEqual(bit.get_sum(3, 3), 5)

if __name__ == "__main__":
    unittest.main()