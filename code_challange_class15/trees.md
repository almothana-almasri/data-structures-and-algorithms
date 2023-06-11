[&leftarrow; Back to Home](../README.md)

Author: **Almothana Almasri**

# Code Challenge: Class 15: Binary Tree and BST Implementation

Features
Node

    Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Binary Tree

    Create a Binary Tree class
        Define a method for each of the depth first traversals:
            pre order
            in order
            post order
        Each depth first traversal method should return an array of values, ordered appropriately.

Binary Search Tree

    Create a Binary Search Tree class
        This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
        Add
            Arguments: value
            Return: nothing
            Adds a new node with that value in the correct location in the binary search tree.
        Contains
            Argument: value
            Returns: boolean indicating whether or not the value is in the tree at least once.

---

## Approach & Efficiency:

implement a binary search tree (BST) and provides methods for adding nodes, performing different traversals (preorder, inorder, postorder), and checking if a value exists in the tree.

- The `add` method It compares the value to be added with each node and navigates to the left or right child accordingly until it finds an appropriate spot to add the new node.

- The `preorder_traversal`, `inorder_traversal`, and `postorder_traversal` methods use recursive approaches to traverse the tree and collect the node values in the desired order. They follow the depth-first search (DFS) approach.

- The `contains` method performs a search for the given value in the BST. It starts from the root and compares the value with each node, moving left or right until it finds a matching value or reaches a leaf node.

The time and space complexities are:

- `add`: The time complexity for adding a node to a BST is O(log N). The space complexity is O(1) since it does not require additional space.

    for example performing the following operation:

    ```python
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    tree.add(7)
    tree.add(12)
    tree.add(20)
    ```
    would give the following tree structure:

              10
             /  \
            5    15
           / \   / \
          3   7 12  20



- `preorder_traversal`, `inorder_traversal`, `postorder_traversal`: Each of these traversal methods visits every node in the tree once, so the time complexity is O(N), where N is the number of nodes in the tree. The space complexity is O(N) as well.

- `contains`: The time complexity for searching a value in a BST is O(log N) in the average case and O(N) in the worst case. The space complexity is O(1) since it does not require additional space proportional to the input.
---

## **Solution**

Check attached file ***[Binary Tree and BST Implementation](trees/trees.py)*** to see the Solution

## Setup

1. Create a virtual environment (optional):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

## Tests

```bash
pytest code_challange_class15/tests/test_trees.py
```
For detailed information

```bash
pytest -v code_challange_class15/tests/test_trees.py
```