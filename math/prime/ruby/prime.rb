# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/ruby/prime.rb

# O(√n): 素数判定
def prime?(n)
  return false if n < 2
  return true if n == 2
  return false if n.even?

  _skip_even = 2
  div = 3
  while div * div <= n
    if n % div == 0
      return false
    end
    div += _skip_even
  end

  true
end
