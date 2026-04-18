# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/python/prime.py

# O(√n): 素数判定
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    _SKIP_EVEN: int = 2
    div: int = 3
    while div * div <= n:
        if n % div == 0:
            return False
        div += _SKIP_EVEN
    return True
