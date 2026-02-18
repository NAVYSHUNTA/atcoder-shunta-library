# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/data_structure/BIT/python/BIT.py

# フェニック木 (binary indexed tree: BIT) クラス
class BIT:
    __size: int
    __bit: list[int]

    def __init__(self, size: int) -> None:
        self.__size = size
        self.__bit = [0] * (size + 1)

    # O(log N): インデックス idx の値に val を加算するメソッド
    def add(self, idx: int, val: int) -> None:
        idx += 1
        while idx <= self.__size:
            self.__bit[idx] += val
            idx += idx & -idx

    # O(log N): 半開区間 [0, right) の区間和を求める計算用のメソッド
    def __sum(self, right: int) -> int:
        result: int = 0
        while right > 0:
            result += self.__bit[right]
            right -= right & -right
        return result

    # O(log N): 半開区間 [0, right) または 半開区間 [left, right) の区間和を求めるメソッド
    def get_sum(self, left: int, right: int = -1) -> int:
        if right == -1:
            left, right = 0, left
        return self.__sum(right) - self.__sum(left)
