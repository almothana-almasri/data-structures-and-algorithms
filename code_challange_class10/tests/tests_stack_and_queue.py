import pytest
from code_challange_class10.stack_and_queue.stack_and_queue import Stack, Queue

def test_stack():
    stack = Stack()
    #6. Test instantiation of empty stack
    assert stack.is_empty()

    #1. Test push onto the stack
    stack.push('a')
    assert stack.peek() == 'a'

    #2. Test push multiple values
    stack.push('b')
    stack.push('c')
    assert stack.peek() == 'c'

    #3. Test pop off the stack
    assert stack.pop() == 'c'
    assert stack.peek() == 'b'

    #4. Test empty a stack after multiple pops
    assert stack.pop() == 'b'
    assert stack.pop() == 'a'
    assert stack.is_empty()

    #7. Test pop/peek on empty stack raises exception
    with pytest.raises(Exception):
        stack.pop()
    with pytest.raises(Exception):
        stack.peek()


def test_queue():
    queue = Queue()
    #13. Test instantiation of empty queue
    assert queue.is_empty()

    #8. Test enqueue into a queue
    queue.enqueue('a')
    assert queue.peek() == 'a'

    #9. Test enqueue multiple values
    queue.enqueue('b')
    queue.enqueue('c')
    assert queue.peek() == 'a'

    #10. Test dequeue out of a queue
    assert queue.dequeue() == 'a'
    assert queue.peek() == 'b'

    #12. Test empty a queue after multiple dequeues
    assert queue.dequeue() == 'b'
    assert queue.dequeue() == 'c'
    assert queue.is_empty()

    #14. Test dequeue/peek on empty queue raises exception
    with pytest.raises(Exception):
        queue.dequeue()
    with pytest.raises(Exception):
        queue.peek()
