use rust::*;

#[test]
fn test_is_prime() {
    // 素数に対する素数判定テスト
    assert_eq!(is_prime(2i8), true);
    assert_eq!(is_prime(3i32), true);
    assert_eq!(is_prime(5i64), true);
    assert_eq!(is_prime(7i128), true);
}

#[test]
fn test_is_not_prime() {
    // 合成数に対する素数判定テスト
    assert_eq!(is_prime(0i8), false);
    assert_eq!(is_prime(1i32), false);
    assert_eq!(is_prime(4i64), false);
    assert_eq!(is_prime(-1i128), false);
    assert_eq!(is_prime(-6i128), false);
}

#[test]
fn test_is_prime_large() {
    // 大きな素数に対する素数判定テスト
    assert_eq!(is_prime(200560490131i64), true);
    assert_eq!(is_prime(92709568269121i128), true);
    assert_eq!(is_prime(99999999999973i128), true);
}

#[test]
fn test_is_not_prime_large() {
    // 大きな合成数に対する素数判定テスト
    assert_eq!(is_prime(200560490113i64), false);
    assert_eq!(is_prime(2005604910109i128), false);
    assert_eq!(is_prime(92709568269119i128), false);
}