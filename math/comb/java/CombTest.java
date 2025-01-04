import static org.junit.Assert.*;
import org.junit.Test;

public class CombTest {
    @Test
    public void testCalcComb() {
        // 組合せの計算テスト
        int n = 40;
        Comb comb = new Comb(n);
        assertEquals(1L, comb.getComb(n, 0));
        assertEquals(40L, comb.getComb(n, 1));
        assertEquals(131282408400L, comb.getComb(n, n / 2 - 1));
        assertEquals(137846528820L, comb.getComb(n, n / 2));
        assertEquals(131282408400L, comb.getComb(n, n / 2 + 1));
        assertEquals(40L, comb.getComb(n, n - 1));
        assertEquals(1L, comb.getComb(n, n));
    }

    @Test
    public void testCalcCombWithMod998244353() {
        // 組合せの計算の余りテスト
        int n = 40;
        int mod = 998244353;
        Comb comb = new Comb(n, mod);
        assertEquals(1L, comb.getComb(n, 0));
        assertEquals(40L, comb.getComb(n, 1));
        assertEquals(512398157L, comb.getComb(n, n / 2 - 1));
        assertEquals(88808106L, comb.getComb(n, n / 2));
        assertEquals(512398157L, comb.getComb(n, n / 2 + 1));
        assertEquals(40L, comb.getComb(n, n - 1));
        assertEquals(1L, comb.getComb(n, n));
    }

    @Test
    public void testCalcCombWithMod1000000007() {
        // 組合せの計算の余りテスト
        int n = 40;
        int mod = 1000000007;
        Comb comb = new Comb(n, mod);
        assertEquals(1L, comb.getComb(n, 0));
        assertEquals(40L, comb.getComb(n, 1));
        assertEquals(282407483L, comb.getComb(n, n / 2 - 1));
        assertEquals(846527861L, comb.getComb(n, n / 2));
        assertEquals(282407483L, comb.getComb(n, n / 2 + 1));
        assertEquals(40L, comb.getComb(n, n - 1));
        assertEquals(1L, comb.getComb(n, n));
    }

    @Test
    public void testCalcCombWithMod998244353Large() {
        int n = 1000000;
        int mod = 998244353;
        Comb comb = new Comb(n, mod);
        assertEquals(1L, comb.getComb(n, 0));
        assertEquals(1000000L, comb.getComb(n, 1));
        assertEquals(779944411L, comb.getComb(n, n / 2 - 1));
        assertEquals(666172069L, comb.getComb(n, n / 2));
        assertEquals(779944411L, comb.getComb(n, n / 2 + 1));
        assertEquals(1000000L, comb.getComb(n, n - 1));
        assertEquals(1L, comb.getComb(n, n));
    }

    @Test
    public void testCalcCombWithMod1000000007Large() {
        int n = 1000000;
        int mod = 1000000007;
        Comb comb = new Comb(n, mod);
        assertEquals(1L, comb.getComb(n, 0));
        assertEquals(1000000L, comb.getComb(n, 1));
        assertEquals(782751210L, comb.getComb(n, n / 2 - 1));
        assertEquals(996692777L, comb.getComb(n, n / 2));
        assertEquals(782751210L, comb.getComb(n, n / 2 + 1));
        assertEquals(1000000L, comb.getComb(n, n - 1));
        assertEquals(1L, comb.getComb(n, n));
    }
}
