import static org.junit.Assert.*;
import org.junit.Test;

public class UnionFindTest {
    @Test
    public void testRoot() {
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);
        assertEquals(uf.root(0), 0);
        assertEquals(uf.root(1), 1);
        assertEquals(uf.root(2), 2);
    }

    @Test
    public void testIsSameFalseCase() {
        final int SIZE = 2;
        UnionFind uf = new UnionFind(SIZE);
        assertFalse(uf.isSame(0, 1));
        assertFalse(uf.isSame(1, 0));
    }

    @Test
    public void testIsSameTrueCase() {
        final int SIZE = 2;
        UnionFind uf = new UnionFind(SIZE);
        uf.union(0, 1);
        assertTrue(uf.isSame(0, 0));
        assertTrue(uf.isSame(0, 1));
        assertTrue(uf.isSame(1, 0));
        assertTrue(uf.isSame(1, 1));
    }

    @Test
    public void testUnion() {
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);
        uf.union(0, 1);
        assertTrue(uf.isSame(0, 1));
        assertFalse(uf.isSame(0, 2));
        assertFalse(uf.isSame(1, 2));
        uf.union(2, 1);
        assertTrue(uf.isSame(0, 1));
        assertTrue(uf.isSame(0, 2));
        assertTrue(uf.isSame(1, 2));
    }

    @Test
    public void testGroupSize() {
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);
        assertEquals(uf.groupSize[uf.root(0)], 1);
        assertEquals(uf.groupSize[uf.root(1)], 1);
        assertEquals(uf.groupSize[uf.root(2)], 1);
        uf.union(0, 1);
        assertEquals(uf.groupSize[uf.root(0)], 2);
        assertEquals(uf.groupSize[uf.root(1)], 2);
        assertEquals(uf.groupSize[uf.root(2)], 1);
        uf.union(2, 1);
        assertEquals(uf.groupSize[uf.root(0)], 3);
        assertEquals(uf.groupSize[uf.root(1)], 3);
        assertEquals(uf.groupSize[uf.root(2)], 3);
    }

    @Test
    public void testAllMethods() {
        final int SIZE = 5;
        UnionFind uf = new UnionFind(SIZE);
        uf.union(0, 1);
        uf.union(2, 3);
        uf.union(1, 2);
        assertTrue(uf.isSame(0, 1));
        assertTrue(uf.isSame(0, 2));
        assertTrue(uf.isSame(0, 3));
        assertFalse(uf.isSame(0, 4));
        assertEquals(uf.groupSize[uf.root(0)], 4);
        assertEquals(uf.groupSize[uf.root(1)], 4);
        assertEquals(uf.groupSize[uf.root(2)], 4);
        assertEquals(uf.groupSize[uf.root(3)], 4);
        assertEquals(uf.groupSize[uf.root(4)], 1);
    }
}
