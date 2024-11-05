# Union-Find 木クラス
class UnionFind:
    def __init__(self, n):
        self.leader = [-1] * n
        self.group_size = [1] * n

    # O(log N): v の根を返すメソッド
    def root(self, v):
        while self.leader[v] != -1:
            v = self.leader[v]
        return v

    # O(log N): x と y が属するグループを併合するメソッド
    def union(self, x, y):
        lx = self.root(x)
        ly = self.root(y)
        if lx == ly:
            return

        if self.group_size[lx] < self.group_size[ly]:
            lx, ly = ly, lx

        self.leader[ly] = lx
        self.group_size[lx] += self.group_size[ly]

    # O(log N): x と y が同じグループに属するかを返すメソッド
    def is_same(self, x, y):
        return self.root(x) == self.root(y)