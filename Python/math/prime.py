# O(√n): 素数判定
def is_prime(n):
    if n < 2:
        return False
    div = 2
    while div ** 2 <= n:
        if n % div == 0:
            return False
        div += 1
    return True