use rust::*;

#[test]
fn test_is_prime() {
    // 素数に対する素数判定テスト
    assert_eq!(true, is_prime(2_i8));
    assert_eq!(true, is_prime(3_i32));
    assert_eq!(true, is_prime(5_i64));
    assert_eq!(true, is_prime(7_i128));
}

#[test]
fn test_is_not_prime() {
    // 合成数に対する素数判定テスト
    assert_eq!(false, is_prime(0_i8));
    assert_eq!(false, is_prime(1_i32));
    assert_eq!(false, is_prime(4_i64));
    assert_eq!(false, is_prime(-1_i128));
    assert_eq!(false, is_prime(-6_i128));
}

#[test]
fn test_is_prime_large() {
    // 大きな素数に対する素数判定テスト
    assert_eq!(true, is_prime(200560490131_i64));
    assert_eq!(true, is_prime(92709568269121_i128));
    assert_eq!(true, is_prime(99999999999973_i128));
}

#[test]
fn test_is_not_prime_large() {
    // 大きな合成数に対する素数判定テスト
    assert_eq!(false, is_prime(200560490113_i64));
    assert_eq!(false, is_prime(2005604910109_i128));
    assert_eq!(false, is_prime(92709568269119_i128));
}