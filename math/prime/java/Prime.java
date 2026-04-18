// Shunta の自作ライブラリ
// https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/math/prime/java/Prime.java

// 素数クラス
class Prime {
    // O(√n): 素数判定を行うメソッド
    public static boolean isPrime(long n) {
        if (n < 2L) {
            return false;
        }
        if (n == 2L) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }

        final long SKIP_EVEN = 2L;
        long div = 3L;
        while (div * div <= n) {
            if (n % div == 0L) {
                return false;
            }
            div += SKIP_EVEN;
        }
        return true;
    }
}
