// Shunta の自作ライブラリ
// https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/rust/src/lib.rs

// O(√n): 素数判定
pub fn is_prime<T>(n: T) -> bool
where T: Copy + num::Integer + std::ops::AddAssign
{
    let one = T::one();
    let two = one + one;

    if n < two {
        return false;
    }
    if n == two {
        return true;
    }
    if n.is_even() {
        return false;
    }

    let _skip_even = two;
    let mut div = two + one;
    while div * div <= n {
        if (n % div).is_zero() {
            return false;
        }
        div += _skip_even;
    }

    true
}
