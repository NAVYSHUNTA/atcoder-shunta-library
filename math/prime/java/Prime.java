// 素数クラス
class Prime {
    // O(√n): 素数判定を行うメソッド
    public static boolean isPrime(long n) {
        if (n < 2L) {
            return false;
        }
        long div = 2L;
        while (div * div <= n) {
            if (n % div == 0L) {
                return false;
            }
            div += 1L;
        }
        return true;
    }
}
