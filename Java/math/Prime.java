// 素数クラス
class Prime {
    // O(√n): 素数判定を行うメソッド
    public static boolean isPrime(long n) {
        if (n < 2L) {
            return false;
        }
        long val = 2L;
        while (val * val <= n) {
            if (n % val == 0L) {
                return false;
            }
            val += 1L;
        }
        return true;
    }
}