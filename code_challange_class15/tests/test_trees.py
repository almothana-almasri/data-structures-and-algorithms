import pytest
from code_challange_class15.trees.trees import BinarySearchTree

# Test 1: Can successfully instantiate an empty tree
def test_instantiating_empty_tree():
    tree = BinarySearchTree()
    assert tree.root is None

# Test 2: Can successfully instantiate a tree with a single root node
def test_instantiating_tree_with_single_root_node():
    tree = BinarySearchTree()
    tree.add(10)
    assert tree.root.value == 10

# Test 3: For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_adding_left_and_right_children_to_node():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.root.left.value == 5
    assert tree.root.right.value == 15

# Test 4: Can successfully return a collection from a pre-order traversal
def test_preorder_traversal():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(20)
    assert tree.preorder_traversal(tree.root) == [10, 5, 3, 7, 15, 12, 20]

# Test 5: Can successfully return a collection from an in-order traversal
def test_inorder_traversal():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(20)
    assert tree.inorder_traversal(tree.root) == [3, 5, 7, 10, 12, 15, 20]

# Test 6: Can successfully return a collection from a post-order traversal
def test_postorder_traversal():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(20)
    assert tree.postorder_traversal(tree.root) == [3, 7, 5, 12, 20, 15, 10]
    
# Test 7: Returns true/false for the contains method, given an existing or non-existing node value
def test_contains_existing_node_value():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.contains(10) is True
    assert tree.contains(5) is True
    assert tree.contains(15) is True

def test_contains_non_existing_node_value():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree.contains(3) is False
    assert tree.contains(20) is False
    assert tree.contains(8) is False
