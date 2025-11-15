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

    // O(log N): 区間 [0, idx] の区間和を求める計算用のメソッド
    private long sum(int idx) {
        long result = 0L;
        idx += 1;
        while (idx > 0) {
            result += this.bit[idx];
            idx -= idx & -idx;
        }
        return result;
    }

    // O(log N): 区間 [0, idx] の区間和を求めるメソッド
    public long getSum(int idx) {
        return this.sum(idx);
    }

    // O(log N): 区間 [idx1, idx2] の区間和を求めるメソッド
    public long getSum(int idx1, int idx2) {
        return this.sum(idx2) - this.sum(idx1 - 1);
    }
}
