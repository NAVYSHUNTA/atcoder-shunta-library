// Shunta の自作ライブラリ
// https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/comb/rust/tests/lib_test.rs

use rust::Comb;

#[test]
fn test_get_comb_invalid_cases_returns_zero() {
    // 不正な数値に対するテスト
    let n: i64 = 40;
    let mod_val: i64 = 998244353;
    let comb = Comb::new(n as usize);
    let mod_comb = Comb::new_with_mod(n as usize, mod_val);
    assert_eq!(0_i64, comb.get_comb(n, -1));
    assert_eq!(0_i64, mod_comb.get_comb(n, -2));
    assert_eq!(0_i64, comb.get_comb(-3, -2));
    assert_eq!(0_i64, mod_comb.get_comb(-5, -7));
    assert_eq!(0_i64, comb.get_comb(-10, n));
    assert_eq!(0_i64, mod_comb.get_comb(-8, n));
    assert_eq!(0_i64, comb.get_comb(-5, 0));
    assert_eq!(0_i64, mod_comb.get_comb(-38, 0));
    assert_eq!(0_i64, comb.get_comb(0, -10));
    assert_eq!(0_i64, mod_comb.get_comb(0, 29));
}

#[test]
fn test_calc_comb() {
    // 組合せの計算テスト
    let n: i64 = 40;
    let comb = Comb::new(n as usize);
    assert_eq!(1_i64, comb.get_comb(0, 0));
    assert_eq!(1_i64, comb.get_comb(n, 0));
    assert_eq!(40_i64, comb.get_comb(n, 1));
    assert_eq!(131282408400_i64, comb.get_comb(n, n / 2 - 1));
    assert_eq!(137846528820_i64, comb.get_comb(n, n / 2));
    assert_eq!(131282408400_i64, comb.get_comb(n, n / 2 + 1));
    assert_eq!(40_i64, comb.get_comb(n, n - 1));
    assert_eq!(1_i64, comb.get_comb(n, n));
}

#[test]
fn test_calc_comb_with_mod_998244353() {
    // 組合せの計算の余りテスト
    let n: i64 = 40;
    let mod_val: i64 = 998244353;
    let comb = Comb::new_with_mod(n as usize, mod_val);
    assert_eq!(1_i64, comb.get_comb(0, 0));
    assert_eq!(1_i64, comb.get_comb(n, 0));
    assert_eq!(40_i64, comb.get_comb(n, 1));
    assert_eq!(512398157_i64, comb.get_comb(n, n / 2 - 1));
    assert_eq!(88808106_i64, comb.get_comb(n, n / 2));
    assert_eq!(512398157_i64, comb.get_comb(n, n / 2 + 1));
    assert_eq!(40_i64, comb.get_comb(n, n - 1));
    assert_eq!(1_i64, comb.get_comb(n, n));
}

#[test]
fn test_calc_comb_with_mod_1000000007() {
    // 組合せの計算の余りテスト
    let n: i64 = 40;
    let mod_val: i64 = 1000000007;
    let comb = Comb::new_with_mod(n as usize, mod_val);
    assert_eq!(1_i64, comb.get_comb(n, 0));
    assert_eq!(40_i64, comb.get_comb(n, 1));
    assert_eq!(282407483_i64, comb.get_comb(n, n / 2 - 1));
    assert_eq!(846527861_i64, comb.get_comb(n, n / 2));
    assert_eq!(282407483_i64, comb.get_comb(n, n / 2 + 1));
    assert_eq!(40_i64, comb.get_comb(n, n - 1));
    assert_eq!(1_i64, comb.get_comb(n, n));
}

#[test]
fn test_calc_comb_with_mod_998244353_large() {
    // 大きい数に対する組合せの計算の余りテスト
    let n: i64 = 1000000;
    let mod_val: i64 = 998244353;
    let comb = Comb::new_with_mod(n as usize, mod_val);
    assert_eq!(1_i64, comb.get_comb(n, 0));
    assert_eq!(1000000_i64, comb.get_comb(n, 1));
    assert_eq!(779944411_i64, comb.get_comb(n, n / 2 - 1));
    assert_eq!(666172069_i64, comb.get_comb(n, n / 2));
    assert_eq!(779944411_i64, comb.get_comb(n, n / 2 + 1));
    assert_eq!(1000000_i64, comb.get_comb(n, n - 1));
    assert_eq!(1_i64, comb.get_comb(n, n));
}

#[test]
fn test_calc_comb_with_mod_1000000007_large() {
    // 大きい数に対する組合せの計算の余りテスト
    let n: i64 = 1000000;
    let mod_val: i64 = 1000000007;
    let comb = Comb::new_with_mod(n as usize, mod_val);
    assert_eq!(1_i64, comb.get_comb(n, 0));
    assert_eq!(1000000_i64, comb.get_comb(n, 1));
    assert_eq!(782751210_i64, comb.get_comb(n, n / 2 - 1));
    assert_eq!(996692777_i64, comb.get_comb(n, n / 2));
    assert_eq!(782751210_i64, comb.get_comb(n, n / 2 + 1));
    assert_eq!(1000000_i64, comb.get_comb(n, n - 1));
    assert_eq!(1_i64, comb.get_comb(n, n));
}
