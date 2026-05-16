# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/comb/python/test_comb.py

import unittest
from comb import Comb

class TestComb(unittest.TestCase):
    def test_get_comb_invalid_cases_returns_zero(self) -> None:
        """不正な数値に対するテスト"""
        n: int = 40
        mod: int = 998244353
        comb: Comb = Comb(n)
        mod_comb: Comb = Comb(n, mod)
        self.assertEqual(0, comb.get_comb(n, -1))
        self.assertEqual(0, mod_comb.get_comb(n, -2))
        self.assertEqual(0, comb.get_comb(-3, -2))
        self.assertEqual(0, mod_comb.get_comb(-5, -7))
        self.assertEqual(0, comb.get_comb(-10, n))
        self.assertEqual(0, mod_comb.get_comb(-8, n))
        self.assertEqual(0, comb.get_comb(-5, 0))
        self.assertEqual(0, mod_comb.get_comb(-38, 0))
        self.assertEqual(0, comb.get_comb(0, -10))
        self.assertEqual(0, mod_comb.get_comb(0, 29))

    def test_calc_comb(self) -> None:
        """組合せの計算テスト"""
        n: int = 40
        comb: Comb = Comb(n)
        self.assertEqual(1, comb.get_comb(0, 0))
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(40, comb.get_comb(n, 1))
        self.assertEqual(131282408400, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(137846528820, comb.get_comb(n, n // 2))
        self.assertEqual(131282408400, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(40, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_998244353(self) -> None:
        """組合せの計算の余りテスト"""
        n: int = 40
        mod: int = 998244353
        comb: Comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(0, 0))
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(40, comb.get_comb(n, 1))
        self.assertEqual(512398157, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(88808106, comb.get_comb(n, n // 2))
        self.assertEqual(512398157, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(40, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_1000000007(self) -> None:
        """組合せの計算の余りテスト"""
        n: int = 40
        mod: int = 10 ** 9 + 7
        comb: Comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(40, comb.get_comb(n, 1))
        self.assertEqual(282407483, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(846527861, comb.get_comb(n, n // 2))
        self.assertEqual(282407483, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(40, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_998244353_large(self) -> None:
        """大きい数に対する組合せの計算の余りテスト"""
        n: int = 10 ** 6
        mod: int = 998244353
        comb: Comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(10 ** 6, comb.get_comb(n, 1))
        self.assertEqual(779944411, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(666172069, comb.get_comb(n, n // 2))
        self.assertEqual(779944411, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(10 ** 6, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

    def test_calc_comb_with_mod_1000000007_large(self) -> None:
        """大きい数に対する組合せの計算の余りテスト"""
        n: int = 10 ** 6
        mod: int = 10 ** 9 + 7
        comb: Comb = Comb(n, mod)
        self.assertEqual(1, comb.get_comb(n, 0))
        self.assertEqual(10 ** 6, comb.get_comb(n, 1))
        self.assertEqual(782751210, comb.get_comb(n, n // 2 - 1))
        self.assertEqual(996692777, comb.get_comb(n, n // 2))
        self.assertEqual(782751210, comb.get_comb(n, n // 2 + 1))
        self.assertEqual(10 ** 6, comb.get_comb(n, n - 1))
        self.assertEqual(1, comb.get_comb(n, n))

if __name__ == '__main__':
    unittest.main()
