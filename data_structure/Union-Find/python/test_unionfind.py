# Shunta の自作ライブラリ
# https://github.com/NAVYSHUNTA/atcoder-shunta-library/blob/main/data_structure/Union-Find/python/test_unionfind.py

import unittest
from unionfind import UnionFind

class TestUnionFind(unittest.TestCase):
    def test_root(self) -> None:
        """根を取得するテスト"""
        SIZE: int = 3
        uf: UnionFind = UnionFind(SIZE)

        self.assertEqual(0, uf.root(0))
        self.assertEqual(1, uf.root(1))
        self.assertEqual(2, uf.root(2))

    def test_is_same_false_case(self) -> None:
        """異なるグループに属するものに対するテスト"""
        SIZE: int = 2
        uf: UnionFind = UnionFind(SIZE)

        self.assertFalse(uf.is_same(0, 1))
        self.assertFalse(uf.is_same(1, 0))

    def test_is_same_true_case(self) -> None:
        """同じグループに属するものに対するテスト"""
        SIZE: int = 2
        uf: UnionFind = UnionFind(SIZE)

        uf.union(0, 1)
        self.assertTrue(uf.is_same(0, 0))
        self.assertTrue(uf.is_same(0, 1))
        self.assertTrue(uf.is_same(1, 0))
        self.assertTrue(uf.is_same(1, 1))

    def test_union(self) -> None:
        """グループの併合テスト"""
        SIZE: int = 3
        uf: UnionFind = UnionFind(SIZE)

        uf.union(0, 1)
        self.assertTrue(uf.is_same(0, 1))
        self.assertFalse(uf.is_same(0, 2))
        self.assertFalse(uf.is_same(1, 2))

        uf.union(2, 1)
        self.assertTrue(uf.is_same(0, 1))
        self.assertTrue(uf.is_same(0, 2))
        self.assertTrue(uf.is_same(1, 2))

    def test_get_group_size(self) -> None:
        """グループのサイズテスト"""
        SIZE: int = 3
        uf: UnionFind = UnionFind(SIZE)

        self.assertEqual(1, uf.get_group_size(0))
        self.assertEqual(1, uf.get_group_size(1))
        self.assertEqual(1, uf.get_group_size(2))

        uf.union(0, 1)
        self.assertEqual(2, uf.get_group_size(0))
        self.assertEqual(2, uf.get_group_size(1))
        self.assertEqual(1, uf.get_group_size(2))

        uf.union(2, 1)
        self.assertEqual(3, uf.get_group_size(0))
        self.assertEqual(3, uf.get_group_size(1))
        self.assertEqual(3, uf.get_group_size(2))

    def test_get_group_count(self) -> None:
        """連結成分の個数テスト"""
        SIZE: int = 3
        uf: UnionFind = UnionFind(SIZE)

        self.assertEqual(3, uf.get_group_count())

        uf.union(0, 1)
        self.assertEqual(2, uf.get_group_count())
        uf.union(1, 1)
        self.assertEqual(2, uf.get_group_count())
        uf.union(1, 0)
        self.assertEqual(2, uf.get_group_count())
        uf.union(2, 1)
        self.assertEqual(1, uf.get_group_count())

    def test_all_methods(self) -> None:
        """全ての操作を試すテスト"""
        SIZE: int = 5
        uf: UnionFind = UnionFind(SIZE)

        self.assertEqual(5, uf.get_group_count())

        uf.union(0, 1)
        self.assertEqual(4, uf.get_group_count())
        uf.union(2, 3)
        self.assertEqual(3, uf.get_group_count())
        uf.union(1, 2)
        self.assertEqual(2, uf.get_group_count())

        self.assertTrue(uf.is_same(0, 1))
        self.assertTrue(uf.is_same(0, 2))
        self.assertTrue(uf.is_same(0, 3))
        self.assertFalse(uf.is_same(0, 4))

        self.assertEqual(4, uf.get_group_size(0))
        self.assertEqual(4, uf.get_group_size(1))
        self.assertEqual(4, uf.get_group_size(2))
        self.assertEqual(4, uf.get_group_size(3))
        self.assertEqual(1, uf.get_group_size(4))

if __name__ == '__main__':
    unittest.main()
