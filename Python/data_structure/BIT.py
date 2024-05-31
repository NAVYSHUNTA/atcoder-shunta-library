# フェニック木 (binary indexed tree: BIT) クラス
class BIT:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)

    # O(logN): インデックス idx の値に val を加算するメソッド
    def add(self, idx, val):
        while idx <= self.size:
            self.bit[idx] += val
            idx += idx & -idx

    # O(logN): 区間 1 ~ idx の和を求める計算用のメソッド
    def _sum(self, idx):
        result = 0
        while idx > 0:
            result += self.bit[idx]
            idx -= idx & -idx
        return result

    # O(logN): 区間 1 ~ idx1 または 区間 idx1 ~ idx2 の和を求めるメソッド
    def get_sum(self, idx1, idx2 = None):
        if idx2 is None:
            return self._sum(idx1)
        return self._sum(idx2) - self._sum(idx1 - 1)