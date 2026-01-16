# O(√n): 素数判定
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    div: int = 2
    while div * div <= n:
        if n % div == 0:
            return False
        div += 1
    return True
