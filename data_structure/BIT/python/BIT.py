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

    # O(log N): 区間 [0, idx] の区間和を求める計算用のメソッド
    def __sum(self, idx: int) -> int:
        idx += 1
        result: int = 0
        while idx > 0:
            result += self.__bit[idx]
            idx -= idx & -idx
        return result

    # O(log N): 区間 [0, idx1] または 区間 [idx1, idx2] の区間和を求めるメソッド
    def get_sum(self, idx1: int, idx2: int | None = None) -> int:
        if idx2 is None:
            return self.__sum(idx1)
        return self.__sum(idx2) - self.__sum(idx1 - 1)
