// O(√n): 素数判定
pub fn is_prime<T>(n: T) -> bool
where T: Copy
    + num::Integer
    + num::NumCast
{
    if n < T::from(2).unwrap() {
        return false;
    }
    let mut div = T::from(2).unwrap();
    while div * div <= n {
        if n % div == T::from(0).unwrap() {
            return false;
        }
        div = div + T::from(1).unwrap();
    }

    true
}
