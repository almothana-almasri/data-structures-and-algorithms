[&leftarrow; Back to Home](../README.md)

Author: **Almothana Almasri**

# Code Challenge: Linked List Implementation

d

---

## **Approach & Efficiency**

For our LinkedList implementation, we have taken an object-oriented approach, defining a Node class and a LinkedList class.

**Approach:**

- The `Node` class has an `__init__` method that accepts a value and a pointer to the next node. The `value` attribute holds the value of the node and `next` attribute holds the reference to the next node in the LinkedList.

- The `LinkedList` class also has an `__init__` method that initializes the `head` of the LinkedList.

- The `insert` method in the `LinkedList` class takes a value and inserts a new Node with that value at the beginning of the list.

- The `includes` method traverses the LinkedList and checks if a value exists in any of the nodes. If the value is found, it returns `True`, else it returns `False`.

- The `to_string` method traverses the LinkedList and returns a string that represents all the Node values in the LinkedList.

**Efficiency:**

- `insert`: The time complexity is O(1), as we are adding the element at the head of the LinkedList. The space complexity is also O(1), as we are only creating one new node.

- `includes`: The worst-case time complexity is O(n), where n is the number of nodes in the LinkedList. This is because in the worst case, we have to traverse the entire list. The space complexity is O(1) as we are not using any additional data structures.

- `to_string`: The time complexity is O(n), as we need to traverse the entire LinkedList to form the string. The space complexity is O(n), as we are creating a new string based on the number of nodes in the LinkedList.

---

## **Solution**

Check attached file ***[linked_list.py](linked_list/linked_list.py)*** to see the Solution

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
pytest code_challange_class05/tests
```
For detailed information

```bash
pytest -v code_challange_class05/tests
```