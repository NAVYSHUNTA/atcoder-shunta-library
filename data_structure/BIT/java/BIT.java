// Shunta の自作ライブラリ
// https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/data_structure/BIT/java/BIT.java

// フェニック木 (binary indexed tree: BIT) クラス
class BIT {
    private int size;
    private long[] bit;

    BIT (int size) {
        this.size = size;
        this.bit = new long[size + 1];
    }

    // O(log N): インデックス idx の値に val を加算するメソッド
    public void add(int idx, long val) {
        idx += 1;
        while (idx <= this.size) {
            this.bit[idx] += val;
            idx += idx & -idx;
        }
    }

    // O(log N): 半開区間 [0, right) の区間和を求める計算用のメソッド
    private long sum(int right) {
        long result = 0L;
        while (right > 0) {
            result += this.bit[right];
            right -= right & -right;
        }
        return result;
    }

    // O(log N): 半開区間 [0, right) の区間和を求めるメソッド
    public long getSum(int right) {
        return this.sum(right);
    }

    // O(log N): 半開区間 [left, right) の区間和を求めるメソッド
    public long getSum(int left, int right) {
        return this.sum(right) - this.sum(left);
    }
}
