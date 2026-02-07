# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/ruby/test_prime.rb

require 'minitest/autorun'
require_relative 'prime'

class TestPrime < Minitest::Test
  def test_is_prime
    # 素数に対する素数判定テスト
    assert prime?(2)
    assert prime?(3)
    assert prime?(5)
    assert prime?(7)
  end

  def test_is_not_prime
    # 合成数に対する素数判定テスト
    refute prime?(0)
    refute prime?(1)
    refute prime?(4)
    refute prime?(-1)
    refute prime?(-6)
  end

  def test_is_prime_large
    # 大きな素数に対する素数判定テスト
    assert prime?(200560490131)
    assert prime?(92709568269121)
    assert prime?(99999999999973)
  end

  def test_is_not_prime_large
    # 大きな合成数に対する素数判定テスト
    refute prime?(200560490113)
    refute prime?(2005604910109)
    refute prime?(92709568269119)
  end
end
