// Shunta の自作ライブラリ
// https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/data_structure/Union-Find/java/UnionFind.java

// Union-Find 木クラス
class UnionFind {
    private int[] leader;
    private int[] groupSize;
    private int groupCount;

    UnionFind(int n) {
        leader = new int[n];
        groupSize = new int[n];
        for (int i = 0; i < n; i++) {
            leader[i] = -1;
            groupSize[i] = 1;
            groupCount = n;
        }
    }

    // O(log N): v の根を返すメソッド
    // 経路圧縮ありなら、ならし計算量 O(α(N)): v の根を返すメソッド
    int root(int v) {
        if (this.leader[v] == -1) {
            return v;
        } else {
            // 経路圧縮を行わない場合：UnionFind の各操作は O(log N)
            // return this.root(this.leader[v]);

            // 経路圧縮を行う場合：UnionFind の各操作は、ならし計算量で O(α(N)) ここで α はアッカーマン関数の逆関数
            return this.leader[v] = this.root(this.leader[v]);
        }
    }

    // O(log N): x と y が属するグループを併合するメソッド
    // 経路圧縮ありなら、ならし計算量 O(α(N)): x と y が属するグループを併合するメソッド
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
        this.groupCount -= 1;
    }

    // O(log N): x と y が同じグループに属するかを返すメソッド
    // 経路圧縮ありなら、ならし計算量 O(α(N)): x と y が同じグループに属するかを返すメソッド
    boolean isSame(int x, int y) {
        return this.root(x) == this.root(y);
    }

    // O(log N): v が属するグループのサイズを返すメソッド
    // 経路圧縮ありなら、ならし計算量 O(α(N)): v が属するグループのサイズを返すメソッド
    int getGroupSize(int v) {
        return this.groupSize[this.root(v)];
    }

    // O(1): 連結成分の個数を返すメソッド
    int getGroupCount() {
        return this.groupCount;
    }
}
