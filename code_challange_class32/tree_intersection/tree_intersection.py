from code_challange_class32.tree_intersection.hashtable import HashTable
from code_challange_class32.tree_intersection.trees import BinarySearchTree

def tree_intersection(tree1, tree2):
    # Create a hash table to store values from tree1
    hash_table = HashTable()

    # Helper function to perform preorder traversal and store values in the hash table
    def traverse_and_store(node):
        if node:
            hash_table.set(node.value, True)
            traverse_and_store(node.left)
            traverse_and_store(node.right)

    # Perform preorder traversal and store values in the hash table
    traverse_and_store(tree1.root)

    # Create a set to store the intersection of values
    intersection = set()

    # Helper function to perform inorder traversal and check if the value exists in the hash table
    def traverse_and_check(node):
        if node:
            if hash_table.has(node.value):
                intersection.add(node.value)
            traverse_and_check(node.left)
            traverse_and_check(node.right)

    # Perform inorder traversal and check if the value exists in the hash table
    traverse_and_check(tree2.root)

    return intersection

# Assuming you already have the binary trees bst1 and bst2
# and the HashTable implementation provided in the question

# Create the binary trees bst1 and bst2
bst1 = BinarySearchTree()
bst2 = BinarySearchTree()

# Add nodes to bst1 and bst2 (code from the question)
bst1.add(5)
bst1.add(3)
bst1.add(7)
bst1.add(2)
bst1.add(4)
bst1.add(6)
bst1.add(8)

bst2.add(7)
bst2.add(2)
bst2.add(9)
bst2.add(1)
bst2.add(6)
bst2.add(10)

# Find the intersection of values
intersection_values = tree_intersection(bst1, bst2)

print(intersection_values)  # Print the set of intersection values
