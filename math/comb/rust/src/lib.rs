use num_bigint::BigInt;
use num_traits::{ToPrimitive, One};

// 組合せ構造体
#[allow(dead_code)]
pub struct Comb {
    is_with_mod_val: bool,
    mod_val: Option<i64>,
    f: Vec<BigInt>,
    fac: Vec<i64>,
    fac_inv: Vec<i64>,
    inv: Vec<i64>,
}

impl Comb {
    // O(n): コンストラクタ
    pub fn new(n: usize) -> Self {
        let mut f = vec![BigInt::one(); n + 1];
        for i in 2..=n {
            f[i] = f[i - 1].clone() * i;
        }
        Comb {
            is_with_mod_val: false,
            mod_val: None,
            f,
            fac: vec![],
            fac_inv: vec![],
            inv: vec![],
        }
    }

    // O(n): コンストラクタ
    pub fn new_with_mod(n: usize, mod_val: i64) -> Self {
        let mut fac = vec![1_i64; n + 1];
        let mut fac_inv = vec![1_i64; n + 1];
        let mut inv = vec![1_i64; n + 1];

        for i in 2..=n {
            fac[i] = (fac[i - 1] * i as i64) % mod_val;
            inv[i] = ((-inv[mod_val as usize % i] * (mod_val / i as i64)) % mod_val + mod_val) % mod_val;
            fac_inv[i] = ((fac_inv[i - 1] * inv[i]) % mod_val + mod_val) % mod_val;
        }
        Comb {
            is_with_mod_val: true,
            mod_val: Some(mod_val),
            f: vec![],
            fac,
            fac_inv,
            inv,
        }
    }

    // nCr の値を求める関数
    // O(1): コンストラクタで mod_val を指定していないかつ n が小さい場合
    // O(1): コンストラクタで mod_val を指定している場合（n の値によらない）
    pub fn get_comb(&self, n: usize, r: usize) -> i64 {
        if self.is_with_mod_val {
            (((self.fac[n] * self.fac_inv[r]) % self.mod_val.unwrap()) * self.fac_inv[n - r]) % self.mod_val.unwrap()
        } else {
            (self.f[n].clone() / (self.f[r].clone() * self.f[n - r].clone())).to_i64().unwrap()
        }
    }
}
