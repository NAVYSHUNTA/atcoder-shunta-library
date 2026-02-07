# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/ruby/prime.rb

# O(√n): 素数判定
def prime?(n)
  if n < 2
    return false
  end
  div = 2
  while div * div <= n
    if n % div == 0
      return false
    end
    div += 1
  end
  return true
end
