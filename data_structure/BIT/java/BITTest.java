import static org.junit.Assert.*;
import org.junit.Test;

public class BITTest {
    @Test
    public void testGetSum() {
        // 区間和のテスト
        final int SIZE = 5;
        BIT bit = new BIT(SIZE);
        bit.add(1, 3);
        bit.add(2, 2);
        bit.add(3, 5);
        bit.add(4, 1);
        bit.add(5, 5);

        assertEquals(3, bit.getSum(1));
        assertEquals(5, bit.getSum(2));
        assertEquals(10, bit.getSum(3));
        assertEquals(11, bit.getSum(4));
        assertEquals(16, bit.getSum(5));

        assertEquals(16, bit.getSum(1, 5));
        assertEquals(8, bit.getSum(2, 4));
        assertEquals(5, bit.getSum(3, 3));
    }
}
