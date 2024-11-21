// Union-Find 木クラス
class UnionFind {
    private int[] leader;
    protected int[] groupSize;

    UnionFind(int n) {
        leader = new int[n];
        groupSize = new int[n];
        for (int i = 0; i < n; i++) {
            leader[i] = -1;
            groupSize[i] = 1;
        }
    }

    // O(log N): v の根を返すメソッド
    int root(int v) {
        while (this.leader[v] != -1) {
            v = this.leader[v];
        }
        return v;
    }

    // O(log N): x と y が属するグループを併合するメソッド
    void union(int x, int y) {
        int lx = this.root(x);
        int ly = this.root(y);
        if (lx == ly) {
            return;
        }

        if (this.groupSize[lx] < this.groupSize[ly]) {
            int tmp = lx;
            lx = ly;
            ly = tmp;
        }

        this.leader[ly] = lx;
        this.groupSize[lx] += this.groupSize[ly];
    }

    // O(log N): x と y が同じグループに属するかを返すメソッド
    boolean isSame(int x, int y) {
        return this.root(x) == this.root(y);
    }
}