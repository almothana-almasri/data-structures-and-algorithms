class Node:
    def __init__(self, value):
        """
        Initialize a node with the given value.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        """Initialize an empty binary tree."""
        self.root = None

    def preorder_traversal(self, node):
        """
        Perform a preorder traversal of the binary tree starting from the given node.

        Args:
            node: The starting node for the traversal.

        Returns:
            A list containing the values of the nodes visited during the traversal, following the preorder sequence.
        """
        res = []
        if node:
            res.append(node.value)
            res = res + self.preorder_traversal(node.left)
            res = res + self.preorder_traversal(node.right)
        return res

    def inorder_traversal(self, node):
        """
        Perform an inorder traversal of the binary tree starting from the given node.

        Args:
            node: The starting node for the traversal.

        Returns:
            A list containing the values of the nodes visited during the traversal, following the inorder sequence.
        """
        res = []
        if node:
            res = self.inorder_traversal(node.left)
            res.append(node.value)
            res = res + self.inorder_traversal(node.right)
        return res

    def postorder_traversal(self, node):
        """
        Perform a postorder traversal of the binary tree starting from the given node.

        Args:
            node: The starting node for the traversal.

        Returns:
            A list containing the values of the nodes visited during the traversal, following the postorder sequence.
        """
        res = []
        if node:
            res = self.postorder_traversal(node.left)
            res = res + self.postorder_traversal(node.right)
            res.append(node.value)
        return res
    
    def find_maximum(self):
        """
        Find the maximum value stored in the tree.

        Returns:
            The maximum value stored in the tree.
        """
        if self.root is None:
            return None

        node = self.root
        while node.right is not None:
            node = node.right

        return node.value

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Add a node with the given value to the binary search tree.

        If the value already exists in the tree, do nothing.

        Args:
            value: The value to be added to the tree.
        """
        if self.root is None:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                else:
                    node = node.left
            elif value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    return
                else:
                    node = node.right
            else:
                return

    def contains(self, value):
        """
        Check if the binary search tree contains a node with the given value.

        Args:
            value: The value to search for in the tree.

        Returns:
            True if the value is found in the tree, False otherwise.
        """
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False


bst = BinarySearchTree()

bst.add(5)
bst.add(3)
bst.add(7)
bst.add(2)
bst.add(4)
bst.add(6)
bst.add(8)
bst.add(9)

print(bst.contains(4)) 
print(bst.contains(9))

print(bst.preorder_traversal(bst.root))
print(bst.inorder_traversal(bst.root))
print(bst.postorder_traversal(bst.root))

maximum_value = bst.find_maximum()
print("Maximum value:", maximum_value)
