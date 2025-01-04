import unittest
from comb import *

class TestPrime(unittest.TestCase):
    def test_calc_comb(self):
        """組合せの計算テスト"""
        n = 40
        comb = Comb(n)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(40, comb.get_comb(n, 1))
        self.assertEqual(131282408400, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(137846528820, comb.get_comb(n, n // 2))
        self.assertEqual(131282408400, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(40, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_998244353(self):
        """組合せの計算の余りテスト"""
        n = 40
        mod = 998244353
        comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(40, comb.get_comb(n, 1))
        self.assertEqual(512398157, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(88808106, comb.get_comb(n, n // 2))
        self.assertEqual(512398157, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(40, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_1000000007(self):
        """組合せの計算の余りテスト"""
        n = 40
        mod = 10 ** 9 + 7
        comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(40, comb.get_comb(n, 1))
        self.assertEqual(282407483, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(846527861, comb.get_comb(n, n // 2))
        self.assertEqual(282407483, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(40, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_998244353_large(self):
        """大きい数の組合せの計算の余りテスト"""
        n = 10 ** 6
        mod = 998244353
        comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(10 ** 6, comb.get_comb(n, 1))
        self.assertEqual(779944411, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(666172069, comb.get_comb(n, n // 2))
        self.assertEqual(779944411, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(10 ** 6, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_1000000007_large(self):
        """大きい数の組合せの計算の余りテスト"""
        n = 10 ** 6
        mod = 10 ** 9 + 7
        comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(10 ** 6, comb.get_comb(n, 1))
        self.assertEqual(782751210, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(996692777, comb.get_comb(n, n // 2))
        self.assertEqual(782751210, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(10 ** 6, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

if __name__ == '__main__':
    unittest.main()