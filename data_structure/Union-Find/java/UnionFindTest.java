import static org.junit.Assert.*;
import org.junit.Test;

public class UnionFindTest {
    @Test
    public void testRoot() {
        // 根を取得するテスト
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);

        assertEquals(0, uf.root(0));
        assertEquals(1, uf.root(1));
        assertEquals(2, uf.root(2));
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

        assertEquals(1, uf.getGroupSize(0));
        assertEquals(1, uf.getGroupSize(1));
        assertEquals(1, uf.getGroupSize(2));

        uf.union(0, 1);
        assertEquals(2, uf.getGroupSize(0));
        assertEquals(2, uf.getGroupSize(1));
        assertEquals(1, uf.getGroupSize(2));

        uf.union(2, 1);
        assertEquals(3, uf.getGroupSize(0));
        assertEquals(3, uf.getGroupSize(1));
        assertEquals(3, uf.getGroupSize(2));
    }

    @Test
    public void testGetGroupCount() {
        // 連結成分の個数テスト
        final int SIZE = 3;
        UnionFind uf = new UnionFind(SIZE);

        assertEquals(3, uf.getGroupCount());

        uf.union(0, 1);
        assertEquals(2, uf.getGroupCount());
        uf.union(1, 1);
        assertEquals(2, uf.getGroupCount());
        uf.union(1, 0);
        assertEquals(2, uf.getGroupCount());
        uf.union(2, 1);
        assertEquals(1, uf.getGroupCount());
    }

    @Test
    public void testAllMethods() {
        // 全ての操作を試すテスト
        final int SIZE = 5;
        UnionFind uf = new UnionFind(SIZE);

        assertEquals(5, uf.getGroupCount());

        uf.union(0, 1);
        assertEquals(4, uf.getGroupCount());
        uf.union(2, 3);
        assertEquals(3, uf.getGroupCount());
        uf.union(1, 2);
        assertEquals(2, uf.getGroupCount());

        assertTrue(uf.isSame(0, 1));
        assertTrue(uf.isSame(0, 2));
        assertTrue(uf.isSame(0, 3));
        assertFalse(uf.isSame(0, 4));

        assertEquals(4, uf.getGroupSize(0));
        assertEquals(4, uf.getGroupSize(1));
        assertEquals(4, uf.getGroupSize(2));
        assertEquals(4, uf.getGroupSize(3));
        assertEquals(1, uf.getGroupSize(4));
    }
}
