import pytest
from code_challange_class05.linked_list.linked_list import LinkedList

def test_instantiate_empty_list():
    ll = LinkedList()
    assert ll.head == None

def test_insert_into_list():
    ll = LinkedList()
    ll.insert(10)
    assert ll.head.value == 10

def test_head_points_to_first_node():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    assert ll.head.value == 20

def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    assert ll.head.value == 30
    assert ll.head.next.value == 20
    assert ll.head.next.next.value == 10

def test_includes_returns_true():
    ll = LinkedList()
    ll.insert(10)
    assert ll.includes(10) == True

def test_includes_returns_false():
    ll = LinkedList()
    ll.insert(10)
    assert ll.includes(20) == False

def test_to_string():
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    assert ll.to_string() == "{ 30 } -> { 20 } -> { 10 } -> NULL"
