# Union-Find 木クラス
class UnionFind:
    def __init__(self, n):
        self.__leader = [-1] * n
        self.__group_size = [1] * n # 各連結成分（グループ）のサイズ
        self.__group_count = n # 連結成分（グループ）の個数

    # O(log N): v の根を返すメソッド
    def root(self, v):
        while self.__leader[v] != -1:
            v = self.__leader[v]
        return v

    # O(log N): x と y が属するグループを併合するメソッド
    def union(self, x, y):
        lx = self.root(x)
        ly = self.root(y)
        if lx == ly:
            return

        if self.__group_size[lx] < self.__group_size[ly]:
            lx, ly = ly, lx

        self.__leader[ly] = lx
        self.__group_size[lx] += self.__group_size[ly]
        self.__group_count -= 1

    # O(log N): x と y が同じグループに属するかを返すメソッド
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    # O(log N): v が属するグループのサイズを返すメソッド
    def get_group_size(self, v):
        return self.__group_size[self.root(v)]

    # O(1): 連結成分の個数を返すメソッド
    def get_group_count(self):
        return self.__group_count