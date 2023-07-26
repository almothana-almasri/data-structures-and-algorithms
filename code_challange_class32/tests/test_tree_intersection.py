import pytest
from code_challange_class32.tree_intersection.tree_intersection import tree_intersection
from code_challange_class32.tree_intersection.trees import BinarySearchTree

# Helper function to create binary trees for testing
def create_binary_search_tree(values):
    bst = BinarySearchTree()
    for value in values:
        bst.add(value)
    return bst

# Test cases for the tree_intersection function
def test_tree_intersection():
    # Test case 1: Test with no common values
    bst1 = create_binary_search_tree([1, 2, 3, 4, 5])
    bst2 = create_binary_search_tree([6, 7, 8, 9, 10])
    result = tree_intersection(bst1, bst2)
    assert len(result) == 0
    assert result == set()

    # Test case 2: Test with some common values
    bst1 = create_binary_search_tree([1, 2, 3, 4, 5, 6])
    bst2 = create_binary_search_tree([4, 5, 6, 7, 8, 9])
    result = tree_intersection(bst1, bst2)
    assert len(result) == 3
    assert result == {4, 5, 6}

    # Test case 3: Test with duplicate values in both trees
    bst1 = create_binary_search_tree([1, 2, 3, 3, 4, 5])
    bst2 = create_binary_search_tree([3, 4, 4, 5, 6, 7])
    result = tree_intersection(bst1, bst2)
    assert len(result) == 2
    assert result == {3, 4}
