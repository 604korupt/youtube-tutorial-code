import unittest
from main import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list_test = LinkedList(3)

    def test_insert_front(self):
        self.list_test.insert_front(2)
        self.assertEqual(self.list_test.head.data, 2)
        self.list_test.insert_front(1)
        self.assertEqual(self.list_test.head.next.data, 2)

    def test_insert_last(self):
        self.list_test.insert_last(5)
        self.assertEqual(self.list_test.head.next.data, 5)
        self.list_test.insert_last(6)
        self.assertEqual(self.list_test.head.next.next.data, 6)

    def test_delete_node(self):
        self.list_test.insert_last(5)
        self.list_test.insert_last(6)
        self.list_test.insert_last(7)
        self.list_test.insert_last(8)
        self.list_test.delete_node(0)
        self.assertEqual(self.list_test.head.data, 5)
        self.list_test.delete_node(1)
        self.assertEqual(self.list_test.head.next.data, 7)

    def test_search_node(self):
        self.list_test.insert_last(5)
        self.list_test.insert_last(6)
        self.assertEqual(self.list_test.search(5), True)
        self.assertEqual(self.list_test.search(7), False)

    def test_insert_position(self):
        self.list_test.insert_last(5)
        self.list_test.insert_last(6)
        self.list_test.insert_last(9)
        self.list_test.insert_position(7, 1)
        self.list_test.insert_position(10, 2)
        self.assertEqual(self.list_test.head.next.data, 7)
        self.assertEqual(self.list_test.head.next.next.data, 10)
