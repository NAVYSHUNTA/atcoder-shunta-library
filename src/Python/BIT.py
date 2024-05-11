# フェニック木 (binary indexed tree: BIT) クラス
class BIT:
    def __init__(self, n):
        self.size = n
        self.bit = [0 for _ in range(n + 1)]

    # O(logN): インデックス 1 ~ i の和を求めるメソッド
    def get_sum(self, i):
        result = 0
        while i > 0:
            result += self.bit[i]
            i -= i & -i
        return result

    # O(logN): インデックス i の値に x を加算するメソッド
    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x
            i += i & -i
