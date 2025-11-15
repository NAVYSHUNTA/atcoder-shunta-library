import java.math.BigDecimal;

// 組合せクラス
class Comb {
    private boolean isWithMod = false;
    private long mod;
    private BigDecimal[] f;
    private long[] fac;
    private long[] facInv;
    private long[] inv;

    // O(n): コンストラクタ
    Comb(int n) {
        this.f = new BigDecimal[n + 1];
        this.f[0] = BigDecimal.ONE;
        for (int i = 1; i <= n; i++) {
            this.f[i] = this.f[i - 1].multiply(BigDecimal.valueOf(i));
        }
    }

    // O(n): コンストラクタ
    Comb(int n, int mod) {
        this.isWithMod = true;
        this.mod = mod;

        this.fac = new long[n + 1];
        this.facInv = new long[n + 1];
        this.inv = new long[n + 1];

        this.fac[0] = 1L;
        this.fac[1] = 1L;
        this.facInv[0] = 1L;
        this.facInv[1] = 1L;
        this.inv[0] = 1L;
        this.inv[1] = 1L;

        for (int i = 2; i <= n; i++) {
            this.fac[i] = (this.fac[i - 1] * i) % mod;
            this.inv[i] = ((-this.inv[mod % i] * (mod / i)) % mod + mod) % mod;
            this.facInv[i] = ((this.facInv[i - 1] * this.inv[i]) % mod + mod) % mod;
        }
    }

    // nCr の値を求めるメソッド
    // O(1): コンストラクタで mod を指定していないかつ n が小さい場合
    // O(1): コンストラクタで mod を指定している場合（n の値によらない）
    public long getComb(int n, int r) {
        if (this.isWithMod) {
            return (((this.fac[n] * this.facInv[r]) % this.mod) * this.facInv[n - r]) % this.mod;
        } else {
            return this.f[n].divide(this.f[r].multiply(this.f[n - r])).longValue();
        }
    }
}
