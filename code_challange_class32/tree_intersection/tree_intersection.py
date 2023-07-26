from code_challange_class32.tree_intersection.hashtable import HashTable

def tree_intersection(tree1, tree2):
    """
    Find the intersection of values in two binary trees using a hash table.

    Args:
        tree1 (BinaryTree): The first binary tree.
        tree2 (BinaryTree): The second binary tree.

    Returns:
        set: A set containing the values that exist in both binary trees.
    """
    
    hash_table = HashTable()

    # store values in the hash table
    def traverse_and_store(node):
        if node:
            hash_table.set(node.value, True)
            traverse_and_store(node.left)
            traverse_and_store(node.right)
    traverse_and_store(tree1.root)

    # Create a set to store the intersection of values
    intersection = set()

    # check if the value exists in the hash table
    def traverse_and_check(node):
        if node:
            if hash_table.has(node.value):
                intersection.add(node.value)
            traverse_and_check(node.left)
            traverse_and_check(node.right)
    traverse_and_check(tree2.root)

    return intersection