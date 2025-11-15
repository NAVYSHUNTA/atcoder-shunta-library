# フェニック木 (binary indexed tree: BIT) クラス
class BIT:
    def __init__(self, size):
        self.__size = size
        self.__bit = [0] * (size + 1)

    # O(log N): インデックス idx の値に val を加算するメソッド
    def add(self, idx, val):
        while idx <= self.__size:
            self.__bit[idx] += val
            idx += idx & -idx

    # O(log N): 区間 1 ~ idx の和を求める計算用のメソッド
    def __sum(self, idx):
        result = 0
        while idx > 0:
            result += self.__bit[idx]
            idx -= idx & -idx
        return result

    # O(log N): 区間 1 ~ idx1 または 区間 idx1 ~ idx2 の和を求めるメソッド
    def get_sum(self, idx1, idx2 = None):
        if idx2 is None:
            return self.__sum(idx1)
        return self.__sum(idx2) - self.__sum(idx1 - 1)
