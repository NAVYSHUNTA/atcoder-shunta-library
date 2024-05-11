// フェニック木 (binary indexed tree: BIT) クラス
class BIT {
    int size;
    long[] bit;
    BIT (int n) {
        this.size = n;
        this.bit = new long[n + 1];
    }

    // O(logN): インデックス 1 ~ i の和を求めるメソッド
    public long getSum(int i) {
        long result = 0L;
        while (i > 0) {
            result += this.bit[i];
            i -= i & -i;
        }
        return result;
    }

    // O(logN): インデックス i の値に x を加算するメソッド
    public void add(int i, long x) {
        while (i <= this.size) {
            this.bit[i] += x;
            i += i & -i;
        }
    }
}
