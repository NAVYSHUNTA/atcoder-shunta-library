# Union-Find 木クラス
class UnionFind:
    def __init__(self, n):
        self.__leader = [-1] * n
        self.__group_size = [1] * n # 各連結成分（グループ）のサイズ
        self.__group_count = n # 連結成分（グループ）の個数

    # O(log N): v の根を返すメソッド
    # 経路圧縮ありなら、ならし計算量 O(α(N)): v の根を返すメソッド
    def root(self, v):
        if self.__leader[v] == -1:
            return v
        else:
            # 経路圧縮を行わない場合：UnionFind の各操作は O(log N)
            # return self.root(self.__leader[v])

            # 経路圧縮を行う場合：UnionFind の各操作は、ならし計算量で O(α(N)) ここで α はアッカーマン関数の逆関数
            self.__leader[v] = self.root(self.__leader[v])
            return self.root(self.__leader[v])

    # O(log N): x と y が属するグループを併合するメソッド
    # 経路圧縮ありなら、ならし計算量 O(α(N)): x と y が属するグループを併合するメソッド
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
    # 経路圧縮ありなら、ならし計算量 O(α(N)): x と y が同じグループに属するかを返すメソッド
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    # O(log N): v が属するグループのサイズを返すメソッド
    # 経路圧縮ありなら、ならし計算量 O(α(N)): v が属するグループのサイズを返すメソッド
    def get_group_size(self, v):
        return self.__group_size[self.root(v)]

    # O(1): 連結成分の個数を返すメソッド
    def get_group_count(self):
        return self.__group_count