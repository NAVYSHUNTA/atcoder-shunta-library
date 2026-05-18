# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/comb/ruby/comb.rb

# 組合せクラス
class Comb
  # O(n): コンストラクタ
  def initialize(n, mod = nil)
    @mod = mod
    @fac = Array.new(n + 1, 1)
    @fac_inv = Array.new(n + 1, 1)
    @inv = Array.new(n + 1, 1)

    if mod.nil?
      (2..n).each do |i|
        @fac[i] = @fac[i - 1] * i
      end
    else
      (2..n).each do |i|
        @fac[i] = (@fac[i - 1] * i) % mod
        @inv[i] = (-@inv[mod % i] * (mod / i)) % mod
        @fac_inv[i] = (@fac_inv[i - 1] * @inv[i]) % mod
      end
    end
  end

  # nCr の値を求めるメソッド
  # O(1): コンストラクタで mod を指定していないかつ n が小さい場合
  # O(1): コンストラクタで mod を指定している場合（n の値によらない）
  def get_comb(n, r)
    return 0 if n < r || [n, r].min < 0

    if @mod.nil?
      @fac[n] / (@fac[r] * @fac[n - r])
    else
      (@fac[n] * @fac_inv[r] % @mod) * @fac_inv[n - r] % @mod
    end
  end
end
