class Node:
    '''
    A class representing a node in a linked list or other data structures.
    Each node has two main components: value of the node and reference to the next node.
    Args: value
    '''
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    '''
    A class representing a singly linked list data structure
    '''
    def __init__(self):
        self.head = None

    def insert(self, value):
        '''
        Insert a new node with the given value at the beginning of the linked list.
        Args: value
        Output: None
        '''
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


class HashTable:
    '''
    A data structure that stores key-value pairs of data using buckets to increase data accessing efficiency.
    '''

    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        '''
        A method to return the hash code of the given key.
        Args: key
        Output: hash code of the key (index)
        '''
        if isinstance(key, int):  # Handle integer keys separately
            return key * 283 % self.__size
        elif isinstance(key, str):  # Handle string keys
            return sum([ord(char) for char in key]) * 283 % self.__size
        else:
            raise ValueError("Unsupported key type. Only integers and strings are supported.")

    def set(self, key, value):
        '''
        Set a key-value pair in the bucket, handling collisions as needed.
        Arguments:
        key : The key to be hashed and used as the identifier for the value.
        value : the value that is associated with the key
        Returns: None
        '''
        index = self.__hash(key)
        if self.__buckets[index] is None:
            self.__buckets[index] = LinkedList()

        self.__buckets[index].insert((key, value))

    def get(self, key):
        '''
        Retrieve the value with the given key from the hashtable.
        Args: key
        Return: value or None
        '''
        index = self.__hash(key)
        bucket = self.__buckets[index]
        if bucket is not None:
            curr = bucket.head
            while curr:
                if curr.value[0] == key:
                    return curr.value[1]
                curr = curr.next
        return None

    def has(self, key):
        '''
        A method to check if the given key exists in the hashtable.
        Args: key
        Output: boolean
        '''
        return self.get(key) is not None

    def keys(self):
        '''
        Args: none
        Returns a list of all the keys present in the Hashtable.
        '''
        keys = []
        for bucket in self.__buckets:
            curr = bucket.head if bucket else None
            while curr:
                keys.append(curr.value[0])
                curr = curr.next
        return keys