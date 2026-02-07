// Shunta の自作ライブラリ
// https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/data_structure/BIT/java/BITTest.java

import static org.junit.Assert.*;
import org.junit.Test;

public class BITTest {
    @Test
    public void testGetSum() {
        // 区間和のテスト
        final int SIZE = 5;
        BIT bit = new BIT(SIZE);
        bit.add(0, 3);
        bit.add(1, 2);
        bit.add(2, 5);
        bit.add(3, 1);
        bit.add(4, 5);

        assertEquals(3, bit.getSum(0));
        assertEquals(5, bit.getSum(1));
        assertEquals(10, bit.getSum(2));
        assertEquals(11, bit.getSum(3));
        assertEquals(16, bit.getSum(4));

        assertEquals(16, bit.getSum(0, 4));
        assertEquals(8, bit.getSum(1, 3));
        assertEquals(5, bit.getSum(2, 2));
    }

    @Test
    public void testGetSumWithNegativeValues() {
        // 負数を含む区間和のテスト
        final int SIZE = 4;
        BIT bit = new BIT(SIZE);
        bit.add(3, 16);
        bit.add(0, 4);
        bit.add(2, -2);
        bit.add(1, -8);

        assertEquals(4, bit.getSum(0));
        assertEquals(-4, bit.getSum(1));
        assertEquals(-6, bit.getSum(2));
        assertEquals(10, bit.getSum(3));

        assertEquals(-6, bit.getSum(0, 2));
        assertEquals(6, bit.getSum(1, 3));
        assertEquals(-2, bit.getSum(2, 2));
    }
}
