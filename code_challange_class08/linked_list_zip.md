[&leftarrow; Back to Home](../README.md)

Author: **Almothana Almasri**

# Code Challenge: Class 08: Zip two linked lists.

Write a function called `zipLists` that takes two linked lists as arguments and returns a new linked list that is the result of zipping the two lists together. The zipped list should have nodes alternating between the two input lists.

## Whiteboard Process

## Approach & Efficiency

**Approach:**
1. The function first checks if either `list1` or `list2` is empty by checking if their respective `head` nodes are `None`.
2. If either list is empty, the function returns the non-empty list as the result, bypassing the merging process.
3. If both lists are non-empty, the function proceeds to merge the lists by interweaving their nodes.
4. The merging process is done by iterating through the lists simultaneously using two pointers, `current1` and `current2`.
5. At each iteration, the function connects the nodes of `list2` to `list1` by updating the `next` pointers.
6. The iteration continues until either `current1` or `current2` becomes `None`, indicating that one of the lists has reached its end.
7. Finally, the modified `list1` is returned as the merged list.

**Efficiency:**
The time complexity of this approach is O(min(n, m)), where n and m are the lengths of `list1` and `list2`, respectively. This is because the function iterates through the lists once, stopping when either list reaches its end.
The space complexity is O(1) since the function only uses a constant amount of additional memory to store variables for traversal and updating the next pointers.

## **Solution**

Check attached file ***[Zip two linked lists.](linked_list_zip/linked_list_zip.py)*** to see the Solution

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
pytest code_challange_class08/tests/tests_linked_list_zip.py
```
For detailed information

```bash
pytest -v code_challange_class08/tests/tests_linked_list_zip.py
```