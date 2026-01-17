import unittest
from BIT import BIT

class TestBIT(unittest.TestCase):
    def test_get_sum(self):
        """区間和のテスト"""
        SIZE = 5
        bit = BIT(SIZE)
        bit.add(0, 3)
        bit.add(1, 2)
        bit.add(2, 5)
        bit.add(3, 1)
        bit.add(4, 5)

        self.assertEqual(3, bit.get_sum(0))
        self.assertEqual(5, bit.get_sum(1))
        self.assertEqual(10, bit.get_sum(2))
        self.assertEqual(11, bit.get_sum(3))
        self.assertEqual(16, bit.get_sum(4))

        self.assertEqual(16, bit.get_sum(0, 4))
        self.assertEqual(8, bit.get_sum(1, 3))
        self.assertEqual(5, bit.get_sum(2, 2))

if __name__ == "__main__":
    unittest.main()
