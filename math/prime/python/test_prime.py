# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/python/test_prime.py

import unittest
from prime import is_prime

class TestPrime(unittest.TestCase):
    def test_is_prime(self) -> None:
        """素数に対する素数判定テスト"""
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_is_not_prime(self) -> None:
        """合成数に対する素数判定テスト"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-6))

    def test_is_prime_large(self) -> None:
        """大きな素数に対する素数判定テスト"""
        self.assertTrue(is_prime(200560490131))
        self.assertTrue(is_prime(92709568269121))
        self.assertTrue(is_prime(99999999999973))

    def test_is_not_prime_large(self) -> None:
        """大きな合成数に対する素数判定テスト"""
        self.assertFalse(is_prime(200560490113))
        self.assertFalse(is_prime(2005604910109))
        self.assertFalse(is_prime(92709568269119))

if __name__ == '__main__':
    unittest.main()
