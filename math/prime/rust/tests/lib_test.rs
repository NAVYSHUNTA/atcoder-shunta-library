use rust::*;

#[test]
fn test_is_prime() {
    // 素数に対する素数判定テスト
    assert_eq!(true, is_prime(2i8));
    assert_eq!(true, is_prime(3i32));
    assert_eq!(true, is_prime(5i64));
    assert_eq!(true, is_prime(7i128));
}

#[test]
fn test_is_not_prime() {
    // 合成数に対する素数判定テスト
    assert_eq!(false, is_prime(0i8));
    assert_eq!(false, is_prime(1i32));
    assert_eq!(false, is_prime(4i64));
    assert_eq!(false, is_prime(-1i128));
    assert_eq!(false, is_prime(-6i128));
}

#[test]
fn test_is_prime_large() {
    // 大きな素数に対する素数判定テスト
    assert_eq!(true, is_prime(200560490131i64));
    assert_eq!(true, is_prime(92709568269121i128));
    assert_eq!(true, is_prime(99999999999973i128));
}

#[test]
fn test_is_not_prime_large() {
    // 大きな合成数に対する素数判定テスト
    assert_eq!(false, is_prime(200560490113i64));
    assert_eq!(false, is_prime(2005604910109i128));
    assert_eq!(false, is_prime(92709568269119i128));
}