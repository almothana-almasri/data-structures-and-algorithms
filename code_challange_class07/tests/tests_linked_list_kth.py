import pytest
from code_challange_class07.linked_list_kth.linked_list_kth import LinkedList


@pytest.fixture
def linked_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    return ll

def test_k_greater_than_length(linked_list):
    with pytest.raises(Exception):
        linked_list.kthFromEnd(5)

def test_k_same_as_length(linked_list):
    with pytest.raises(Exception):
        linked_list.kthFromEnd(4)

def test_k_not_positive_integer(linked_list):
    with pytest.raises(Exception):
        linked_list.kthFromEnd(-1)

def test_linked_list_of_size_1():
    ll = LinkedList()
    ll.append(1)
    assert ll.kthFromEnd(0) == 1

def test_happy_path(linked_list):
    assert linked_list.kthFromEnd(0) == 2
    assert linked_list.kthFromEnd(2) == 3
