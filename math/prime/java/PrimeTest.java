import static org.junit.Assert.*;
import org.junit.Test;

public class PrimeTest {
    @Test
    public void testIsPrime() {
        assertTrue(Prime.isPrime(2));
        assertTrue(Prime.isPrime(3));
        assertTrue(Prime.isPrime(5));
        assertTrue(Prime.isPrime(7));
    }

    @Test
    public void testIsNotPrime() {
        assertFalse(Prime.isPrime(0));
        assertFalse(Prime.isPrime(1));
        assertFalse(Prime.isPrime(4));
        assertFalse(Prime.isPrime(-1));
        assertFalse(Prime.isPrime(-6));
    }

    @Test
    public void testIsPrimeLarge() {
        assertTrue(Prime.isPrime(200560490131L));
        assertTrue(Prime.isPrime(92709568269121L));
        assertTrue(Prime.isPrime(99999999999973L));
    }

    @Test
    public void testIsNotPrimeLarge() {
        assertFalse(Prime.isPrime(200560490113L));
        assertFalse(Prime.isPrime(2005604910109L));
        assertFalse(Prime.isPrime(92709568269119L));
    }
}
