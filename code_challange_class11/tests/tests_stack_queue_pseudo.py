from code_challange_class11.stack_queue_pseudo.stack_queue_pseudo import Pseudo_queue
import pytest

@pytest.fixture
def empty_queue():
    return Pseudo_queue()

@pytest.fixture
def filled_queue():
    queue = Pseudo_queue()
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    return queue

def test_enqueue(empty_queue):
    empty_queue.enqueue(5)
    assert empty_queue.dequeue() == 5

def test_dequeue(filled_queue):
    assert filled_queue.dequeue() == 10
    assert filled_queue.dequeue() == 15
    assert filled_queue.dequeue() == 20

def test_dequeue_empty(empty_queue):
    assert empty_queue.dequeue() is None

def test_enqueue_dequeue_sequence(empty_queue):
    empty_queue.enqueue(5)
    empty_queue.enqueue(10)
    empty_queue.enqueue(15)
    assert empty_queue.dequeue() == 5
    empty_queue.enqueue(20)
    assert empty_queue.dequeue() == 10
    assert empty_queue.dequeue() == 15
    assert empty_queue.dequeue() == 20
    assert empty_queue.dequeue() is None
