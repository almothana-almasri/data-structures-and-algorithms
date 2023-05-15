import pytest
from code_challange_class06.linked_list_insertions.linked_list_insertions import LinkedList

def test_append_single():
    ll = LinkedList()
    ll.append(1)
    assert ll.to_list() == [1]

def test_append_multiple():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.to_list() == [1, 2]

def test_insert_before_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, 1.5)
    assert ll.to_list() == [1, 1.5, 2, 3]

def test_insert_before_first():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.insert_before(1, 0.5)
    assert ll.to_list() == [0.5, 1, 2]

def test_insert_after_middle():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(2, 2.5)
    assert ll.to_list() == [1, 2, 2.5, 3]

def test_insert_after_last():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3, 4)
    assert ll.to_list() == [1, 2, 3, 4]
