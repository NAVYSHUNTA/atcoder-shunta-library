# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/comb/ruby/test_comb.rb

require 'minitest/autorun'
require_relative 'comb'

class TestComb < Minitest::Test
  def test_get_comb_invalid_cases_returns_zero
    # 不正な数値に対するテスト
    n = 40
    mod = 998244353
    comb = Comb.new(n)
    mod_comb = Comb.new(n, mod)
    assert_equal 0, comb.get_comb(n, -1)
    assert_equal 0, mod_comb.get_comb(n, -2)
    assert_equal 0, comb.get_comb(-3, -2)
    assert_equal 0, mod_comb.get_comb(-5, -7)
    assert_equal 0, comb.get_comb(-10, n)
    assert_equal 0, mod_comb.get_comb(-8, n)
    assert_equal 0, comb.get_comb(-5, 0)
    assert_equal 0, mod_comb.get_comb(-38, 0)
    assert_equal 0, comb.get_comb(0, -10)
    assert_equal 0, mod_comb.get_comb(0, 29)
  end

  def test_calc_comb
    # 組合せの計算テスト
    n = 40
    comb = Comb.new(n)
    assert_equal 1, comb.get_comb(0, 0)
    assert_equal 1, comb.get_comb(n, 0)
    assert_equal 40, comb.get_comb(n, 1)
    assert_equal 131282408400, comb.get_comb(n, n / 2 - 1)
    assert_equal 137846528820, comb.get_comb(n, n / 2)
    assert_equal 131282408400, comb.get_comb(n, n / 2 + 1)
    assert_equal 40, comb.get_comb(n, n - 1)
    assert_equal 1, comb.get_comb(n, n)
  end

  def test_calc_comb_with_mod_998244353
    # 組合せの計算の余りテスト
    n = 40
    mod = 998244353
    comb = Comb.new(n, mod)
    assert_equal 1, comb.get_comb(0, 0)
    assert_equal 1, comb.get_comb(n, 0)
    assert_equal 40, comb.get_comb(n, 1)
    assert_equal 512398157, comb.get_comb(n, n / 2 - 1)
    assert_equal 88808106, comb.get_comb(n, n / 2)
    assert_equal 512398157, comb.get_comb(n, n / 2 + 1)
    assert_equal 40, comb.get_comb(n, n - 1)
    assert_equal 1, comb.get_comb(n, n)
  end

  def test_calc_comb_with_mod_1000000007
    # 組合せの計算の余りテスト
    n = 40
    mod = 10 ** 9 + 7
    comb = Comb.new(n, mod)
    assert_equal 1, comb.get_comb(n, 0)
    assert_equal 40, comb.get_comb(n, 1)
    assert_equal 282407483, comb.get_comb(n, n / 2 - 1)
    assert_equal 846527861, comb.get_comb(n, n / 2)
    assert_equal 282407483, comb.get_comb(n, n / 2 + 1)
    assert_equal 40, comb.get_comb(n, n - 1)
    assert_equal 1, comb.get_comb(n, n)
  end

  def test_calc_comb_with_mod_998244353_large
    # 大きい数に対する組合せの計算の余りテスト
    n = 10 ** 6
    mod = 998244353
    comb = Comb.new(n, mod)
    assert_equal 1, comb.get_comb(n, 0)
    assert_equal 10 ** 6, comb.get_comb(n, 1)
    assert_equal 779944411, comb.get_comb(n, n / 2 - 1)
    assert_equal 666172069, comb.get_comb(n, n / 2)
    assert_equal 779944411, comb.get_comb(n, n / 2 + 1)
    assert_equal 10 ** 6, comb.get_comb(n, n - 1)
    assert_equal 1, comb.get_comb(n, n)
  end

  def test_calc_comb_with_mod_1000000007_large
    # 大きい数に対する組合せの計算の余りテスト
    n = 10 ** 6
    mod = 10 ** 9 + 7
    comb = Comb.new(n, mod)
    assert_equal 1, comb.get_comb(n, 0)
    assert_equal 10 ** 6, comb.get_comb(n, 1)
    assert_equal 782751210, comb.get_comb(n, n / 2 - 1)
    assert_equal 996692777, comb.get_comb(n, n / 2)
    assert_equal 782751210, comb.get_comb(n, n / 2 + 1)
    assert_equal 10 ** 6, comb.get_comb(n, n - 1)
    assert_equal 1, comb.get_comb(n, n)
  end
end
