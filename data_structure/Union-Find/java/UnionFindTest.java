import static org.junit.Assert.*;
import org.junit.Test;

public class UnionFindTest {
    @Test
    public void testRoot() {
        // 根を取得するテスト
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);
        assertEquals(uf.root(0), 0);
        assertEquals(uf.root(1), 1);
        assertEquals(uf.root(2), 2);
    }

    @Test
    public void testIsSameFalseCase() {
        // 異なるグループに属するものに対するテスト
        final int SIZE = 2;
        UnionFind uf = new UnionFind(SIZE);
        assertFalse(uf.isSame(0, 1));
        assertFalse(uf.isSame(1, 0));
    }

    @Test
    public void testIsSameTrueCase() {
        // 同じグループに属するものに対するテスト
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
        // グループの併合テスト
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
    public void testGetGroupSize() {
        // グループのサイズテスト
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);

        assertEquals(uf.getGroupSize(0), 1);
        assertEquals(uf.getGroupSize(1), 1);
        assertEquals(uf.getGroupSize(2), 1);

        uf.union(0, 1);
        assertEquals(uf.getGroupSize(0), 2);
        assertEquals(uf.getGroupSize(1), 2);
        assertEquals(uf.getGroupSize(2), 1);

        uf.union(2, 1);
        assertEquals(uf.getGroupSize(0), 3);
        assertEquals(uf.getGroupSize(1), 3);
        assertEquals(uf.getGroupSize(2), 3);
    }

    @Test
    public void testGetGroupCount() {
        // 連結成分の個数テスト
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);
        assertEquals(uf.getGroupCount(), 3);

        uf.union(0, 1);
        assertEquals(uf.getGroupCount(), 2);
        uf.union(1, 1);
        assertEquals(uf.getGroupCount(), 2);
        uf.union(1, 0);
        assertEquals(uf.getGroupCount(), 2);
        uf.union(2, 1);
        assertEquals(uf.getGroupCount(), 1);
    }

    @Test
    public void testAllMethods() {
        // 全ての操作を試すテスト
        final int SIZE = 5;
        UnionFind uf = new UnionFind(SIZE);
        assertEquals(uf.getGroupCount(), 5);

        uf.union(0, 1);
        assertEquals(uf.getGroupCount(), 4);
        uf.union(2, 3);
        assertEquals(uf.getGroupCount(), 3);
        uf.union(1, 2);
        assertEquals(uf.getGroupCount(), 2);

        assertTrue(uf.isSame(0, 1));
        assertTrue(uf.isSame(0, 2));
        assertTrue(uf.isSame(0, 3));
        assertFalse(uf.isSame(0, 4));

        assertEquals(uf.getGroupSize(0), 4);
        assertEquals(uf.getGroupSize(1), 4);
        assertEquals(uf.getGroupSize(2), 4);
        assertEquals(uf.getGroupSize(3), 4);
        assertEquals(uf.getGroupSize(4), 1);
    }
}
