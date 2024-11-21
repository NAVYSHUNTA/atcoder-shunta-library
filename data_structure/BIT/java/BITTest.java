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

        assertEquals(bit.getSum(1), 3);
        assertEquals(bit.getSum(2), 5);
        assertEquals(bit.getSum(3), 10);
        assertEquals(bit.getSum(4), 11);
        assertEquals(bit.getSum(5), 16);

        assertEquals(bit.getSum(1, 5), 16);
        assertEquals(bit.getSum(2, 4), 8);
        assertEquals(bit.getSum(3, 3), 5);
    }
}