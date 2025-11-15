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

        self.assertEqual(3, bit.get_sum(1))
        self.assertEqual(5, bit.get_sum(2))
        self.assertEqual(10, bit.get_sum(3))
        self.assertEqual(11, bit.get_sum(4))
        self.assertEqual(16, bit.get_sum(5))

        self.assertEqual(16, bit.get_sum(1, 5))
        self.assertEqual(8, bit.get_sum(2, 4))
        self.assertEqual(5, bit.get_sum(3, 3))

if __name__ == "__main__":
    unittest.main()
