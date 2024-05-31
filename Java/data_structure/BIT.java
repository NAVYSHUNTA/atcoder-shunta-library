// フェニック木 (binary indexed tree: BIT) クラス
class BIT {
    int size;
    long[] bit;
    BIT (int size) {
        this.size = size;
        this.bit = new long[size + 1];
    }

    // O(logN): インデックス idx の値に val を加算するメソッド
    public void add(int idx, long val) {
        while (idx <= this.size) {
            this.bit[idx] += val;
            idx += idx & -idx;
        }
    }

    // O(logN): 区間 1 ~ idx の和を求める計算用のメソッド
    private long sum(int idx) {
        long result = 0L;
        while (idx > 0) {
            result += this.bit[idx];
            idx -= idx & -idx;
        }
        return result;
    }

    // O(logN): 区間 1 ~ idx の和を求めるメソッド
    public long getSum(int idx) {
        return sum(idx);
    }

    // O(logN): 区間 idx1 ~ idx2 の和を求めるメソッド
    public long getSum(int idx1, int idx2) {
        return sum(idx2) - sum(idx1 - 1);
    }
}