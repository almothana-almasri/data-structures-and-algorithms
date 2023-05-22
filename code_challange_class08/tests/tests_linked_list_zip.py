import pytest
from code_challange_class08.linked_list_zip.linked_list_zip import zipLists, LinkedList, Node

def create_linked_list(nodes):
    linked_list = LinkedList()
    for node_value in nodes:
        linked_list.append(node_value)
    return linked_list

def test_zipLists():
    # Test case 1: Both lists have the same length
    list1 = create_linked_list([1, 3, 2])
    list2 = create_linked_list([5, 9, 4])
    expected_output = [1, 5, 3, 9, 2, 4]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 2: First list is shorter than the second list
    list1 = create_linked_list([1, 3])
    list2 = create_linked_list([5, 9, 4])
    expected_output = [1, 5, 3, 9, 4]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 3: First list is longer than the second list
    list1 = create_linked_list([1, 3, 2])
    list2 = create_linked_list([5, 9])
    expected_output = [1, 5, 3, 9, 2]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 4: First list is empty
    list1 = LinkedList()
    list2 = create_linked_list([5, 9, 4])
    expected_output = [5, 9, 4]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 5: Second list is empty
    list1 = create_linked_list([1, 3, 2])
    list2 = LinkedList()
    expected_output = [1, 3, 2]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 6: Both lists are empty
    list1 = LinkedList()
    list2 = LinkedList()
    expected_output = []
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 7: Single node in each list
    list1 = create_linked_list([1])
    list2 = create_linked_list([5])
    expected_output = [1, 5]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 8: Single node in the first list, multiple nodes in the second list
    list1 = create_linked_list([1])
    list2 = create_linked_list([5, 9, 4])
    expected_output = [1, 5, 9, 4]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 9: Single node in the second list, multiple nodes in the first list
    list1 = create_linked_list([1, 3, 2])
    list2 = create_linked_list([5])
    expected_output = [1, 5, 3, 2]
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

    # Test case 10: Large lists
    list1 = create_linked_list(range(1, 1001, 2))
    list2 = create_linked_list(range(2, 1001, 2))
    expected_output = list(range(1, 1001))
    zipped_list = zipLists(list1, list2)
    assert zipped_list.to_list() == expected_output

pytest.main()
