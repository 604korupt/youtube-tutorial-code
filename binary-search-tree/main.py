class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

class BST:
    """
    Time Complexity in the worst case: inserting, searching and deleting is O(n)
    """
    def __init__(self):
        self.root = None

    def search(self, key):
        return self.search_helper(key, self.root)

    def search_helper(self, key, root):
        # if the node equals nothing, then return the root
        if root is None:
            return root
        elif key < root.key:
            # if the key is less than the node key, go left
            return self.search_helper(key, root.left)
        elif key > root.key:
            # if the key is greater than the node key, go right
            return self.search_helper(key, root.right)
        else:
            # if the key is found, return it
            return root.key

    def insert(self, key):
        self.root = self.insert_helper(key, self.root)

    def insert_helper(self, key, root):
        # if the node equals nothing, then make a new node
        if root is None:
            root = Node(key, None, None)
        elif key < root.key:
            # if the key is less than the node key, go left
            root.left = self.insert_helper(key, root.left)
        elif key > root.key:
            # if the key is greater than the node key, go right
            root.right = self.insert_helper(key, root.right)
        # after we put the new key we want to return the tree
        return root

    def delete(self, key):
        self.root = self.delete_helper(key, self.root)

    def delete_helper(self, key, root):
        # if the tree is empty
        if root is None:
            return root
        # find the node to be deleted
        if key < root.key:
            root.left = self.delete_helper(key, root.left)
        elif key > root.key:
            root.right = self.delete_helper(key, root.right)
        else:
            # if node has no children
            if root.left is None and root.right is None:
                root = None
            # if node have one child
            elif root.left is None and root.right is not None:
                root = root.right
            elif root.left is not None and root.right is None:
                root = root.left
            # if node has two children
            else:
                # find the inorder successor
                successor = find_successor(root.right)
                # replace root key with successor key
                root.key = successor.key
                # delete the inorder successor
                root.right = self.delete_helper(root.key, root.right)
        return root

def find_successor(node):
    current = node
    # find the leftmost leaf
    while current.left is not None:
        current = current.left
    return current
