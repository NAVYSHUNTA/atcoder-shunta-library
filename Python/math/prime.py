# O(√n): 素数判定
def is_prime(n):
    if n < 2:
        return False
    val = 2
    while val ** 2 <= n:
        if n % val == 0:
            return False
        val += 1
    return True