// Shunta の自作ライブラリ
// https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/rust/src/lib.rs

// O(√n): 素数判定
pub fn is_prime<T>(n: T) -> bool
where T: Copy + num::Integer
{
    let two = T::one() + T::one();

    if n < two {
        return false;
    }

    let mut div = two;
    while div * div <= n {
        if n % div == T::zero() {
            return false;
        }
        div = div + T::one();
    }

    true
}
