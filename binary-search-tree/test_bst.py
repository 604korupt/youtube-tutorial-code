import unittest
from main import BST


class TestBST(unittest.TestCase):
    def setUp(self):
        self.tree_test = BST()

    def test_insert(self):
        self.tree_test.insert(8)
        self.assertEqual(self.tree_test.root.key, 8)
        self.tree_test.insert(3)
        self.assertEqual(self.tree_test.root.left.key, 3)
        self.tree_test.insert(10)
        self.assertEqual(self.tree_test.root.right.key, 10)
        self.tree_test.insert(1)
        self.tree_test.insert(6)
        self.tree_test.insert(4)
        self.assertEqual(self.tree_test.search(4), 4)
        self.tree_test.insert(7)
        self.tree_test.insert(14)

    def test_search(self):
        self.tree_test.insert(8)
        self.tree_test.insert(3)
        self.tree_test.insert(10)
        self.tree_test.insert(1)
        self.tree_test.insert(6)
        self.tree_test.insert(4)
        self.tree_test.insert(7)
        self.tree_test.insert(14)
        self.assertEqual(self.tree_test.search(3), 3)
        self.assertEqual(self.tree_test.search(1), 1)
        self.assertEqual(self.tree_test.search(2), None)

    def test_delete(self):
        self.tree_test.insert(8)
        self.tree_test.insert(3)
        self.tree_test.insert(10)
        self.tree_test.insert(1)
        self.tree_test.insert(6)
        self.tree_test.insert(4)
        self.tree_test.insert(7)
        self.tree_test.insert(14)
        self.tree_test.delete(4)
        self.assertNotEqual(self.tree_test.search(4), 4)
        self.assertIsNone(self.tree_test.root.left.right.left)
        self.tree_test.delete(6)
        self.assertNotEqual(self.tree_test.search(6), 6)
        self.assertEqual(self.tree_test.root.left.right.key, 7)
        self.tree_test.delete(1)
        self.tree_test.delete(3)
        self.tree_test.delete(7)
        self.tree_test.delete(10)
        self.tree_test.delete(14)
        self.tree_test.insert(3)
        self.tree_test.insert(10)
        self.tree_test.insert(1)
        self.tree_test.insert(6)
        self.tree_test.insert(4)
        self.tree_test.insert(7)
        self.tree_test.insert(14)
        self.tree_test.delete(3)
        self.assertEqual(self.tree_test.root.left.key, 4)
        self.tree_test.insert(4)
        self.assertEqual(self.tree_test.root.left.key, 4)
        self.assertEqual(self.tree_test.delete(2), None)
