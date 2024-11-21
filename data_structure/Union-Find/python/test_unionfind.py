import unittest
from unionfind import *

class TestUnionFind(unittest.TestCase):
    def test_root(self):
        """根を取得するテスト"""
        SIZE = 3
        uf = UnionFind(SIZE)
        self.assertEqual(uf.root(0), 0)
        self.assertEqual(uf.root(1), 1)
        self.assertEqual(uf.root(2), 2)

    def test_is_same_false_case(self):
        """異なるグループに属するものに対するテスト"""
        SIZE = 2
        uf = UnionFind(SIZE)
        self.assertFalse(uf.is_same(0, 1))
        self.assertFalse(uf.is_same(1, 0))

    def test_is_same_true_case(self):
        """同じグループに属するものに対するテスト"""
        SIZE = 2
        uf = UnionFind(SIZE)

        uf.union(0, 1)
        self.assertTrue(uf.is_same(0, 0))
        self.assertTrue(uf.is_same(0, 1))
        self.assertTrue(uf.is_same(1, 0))
        self.assertTrue(uf.is_same(1, 1))

    def test_union(self):
        """グループの併合テスト"""
        SIZE = 3
        uf = UnionFind(SIZE)

        uf.union(0, 1)
        self.assertTrue(uf.is_same(0, 1))
        self.assertFalse(uf.is_same(0, 2))
        self.assertFalse(uf.is_same(1, 2))

        uf.union(2, 1)
        self.assertTrue(uf.is_same(0, 1))
        self.assertTrue(uf.is_same(0, 2))
        self.assertTrue(uf.is_same(1, 2))

    def test_group_size(self):
        """グループのサイズテスト"""
        SIZE = 3
        uf = UnionFind(SIZE)

        self.assertEqual(uf.group_size[uf.root(0)], 1)
        self.assertEqual(uf.group_size[uf.root(1)], 1)
        self.assertEqual(uf.group_size[uf.root(2)], 1)

        uf.union(0, 1)
        self.assertEqual(uf.group_size[uf.root(0)], 2)
        self.assertEqual(uf.group_size[uf.root(1)], 2)
        self.assertEqual(uf.group_size[uf.root(2)], 1)

        uf.union(2, 1)
        self.assertEqual(uf.group_size[uf.root(0)], 3)
        self.assertEqual(uf.group_size[uf.root(1)], 3)
        self.assertEqual(uf.group_size[uf.root(2)], 3)

    def test_all_methods(self):
        """全ての操作を試すテスト"""
        SIZE = 5
        uf = UnionFind(SIZE)

        uf.union(0, 1)
        uf.union(2, 3)
        uf.union(1, 2)

        self.assertTrue(uf.is_same(0, 1))
        self.assertTrue(uf.is_same(0, 2))
        self.assertTrue(uf.is_same(0, 3))
        self.assertFalse(uf.is_same(0, 4))

        self.assertEqual(uf.group_size[uf.root(0)], 4)
        self.assertEqual(uf.group_size[uf.root(1)], 4)
        self.assertEqual(uf.group_size[uf.root(2)], 4)
        self.assertEqual(uf.group_size[uf.root(3)], 4)
        self.assertEqual(uf.group_size[uf.root(4)], 1)

if __name__ == '__main__':
    unittest.main()