import pytest
from code_challange_class16.trees.trees_max import BinarySearchTree

def test_find_maximum_empty():
    bst = BinarySearchTree()
    assert bst.find_maximum() is None

def test_find_maximum_Max_is_the_root():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(2)
    bst.add(1)
    assert bst.find_maximum() == 5

def test_find_maximum_binary_search_tree():
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(4)
    bst.add(6)
    bst.add(8)
    bst.add(1)
    assert bst.find_maximum() == 8
