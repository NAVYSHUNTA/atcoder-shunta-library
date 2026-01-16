from typing import Optional

# 組合せクラス
class Comb:
    __fac: list[int]
    __fac_inv: list[int]
    __inv: list[int]
    __mod: Optional[int]

    # O(n): コンストラクタ
    def __init__(self, n: int, mod: Optional[int] = None) -> None:
        self.__mod = mod

        if mod is None:
            self.__fac = [1] * (n + 1)
            for i in range(2, n + 1):
                self.__fac[i] = self.__fac[i - 1] * i
        else:
            self.__fac = [1] * (n + 1)
            self.__fac_inv = [1] * (n + 1)
            self.__inv = [1] * (n + 1)

            for i in range(2, n + 1):
                self.__fac[i] = (self.__fac[i - 1] * i) % mod
                self.__inv[i] = (-self.__inv[mod % i] * (mod // i)) % mod
                self.__fac_inv[i] = (self.__fac_inv[i - 1] * self.__inv[i]) % mod

    # nCr の値を求めるメソッド
    # O(1): コンストラクタで mod を指定していないかつ n が小さい場合
    # O(1): コンストラクタで mod を指定している場合（n の値によらない）
    def get_comb(self, n: int, r: int) -> int:
        if self.__mod is None:
            return self.__fac[n] // (self.__fac[r] * self.__fac[n - r])
        else:
            return (self.__fac[n] * self.__fac_inv[r] * self.__fac_inv[n - r]) % self.__mod
