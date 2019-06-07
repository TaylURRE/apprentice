import unittest
from milestone4.bonus import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def test_inserting_new_values_works(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertEqual(bst.root.get_val(), 10)

    def test_duplicates_are_not_inserted_back_to_back(self):
        bst = BinarySearchTree()
        bst.insert(14)
        self.assertFalse(bst.insert(14))

    def test_duplicates_are_not_inserted_in_entire_tree(self):
        bst = BinarySearchTree()
        bst.insert(14)
        bst.insert(13)
        bst.insert(12)
        bst.insert(11)
        self.assertFalse(bst.insert(14))

    def test_insert_node_children(self):
        bst = BinarySearchTree()
        bst.insert(9)
        bst.insert(8)
        bst.insert(11)
        self.assertEqual(bst.print_root_tree_children(), [9, [8, 11]])

    def test_inserted_node_can_be_found(self):
        bst = BinarySearchTree()
        bst.insert(11)
        bst.insert(9)
        bst.insert(8)
        bst.insert(13)
        bst.insert(12)
        bst.insert(14)
        self.assertIsNotNone(bst.find(13))

    def test_find_returns_none_for_non_existing_values(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.find(12))


if __name__ == '__main__':
    unittest.main()
