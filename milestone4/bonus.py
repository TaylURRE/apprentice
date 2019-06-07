#
# Hint: You might need to add more methods to help with traversing the tree
#

import unittest

class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    def get_children(self):
        children = []
        if self.left_child:
            children.append(self.left_child.get_val())
        if self.right_child:
            children.append(self.right_child.get_val())
        return children

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def set_root(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.set_root(val)
        elif self.root == self.find(val):
            return False
        else:
            self.insert_node(self.root, val)

    def insert_node(self, node, val):
        if val < node.val:
            if node.left_child:
                self.insert_node(node.left_child, val)
            else:
                node.left_child = Node(val)
        elif val > node.val:
            if node.right_child:
                self.insert_node(node.right_child, val)
            else:
                node.right_child = Node(val)
        else:
            return False

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, node, val):
        if node is None:
            return None
        elif val == node.val:
            return node
        elif val < node.val:
            return self.find_node(node.left_child, val)
        else:
            return self.find_node(node.right_child, val)

    def print_root_tree_children(self):
        tree = []
        if self.root:
            tree.append(self.root.get_val())
            tree.append(self.root.get_children())
        return tree
