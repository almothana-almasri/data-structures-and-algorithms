class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

class HashTable:
    def __init__(self, size=1024):
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        if isinstance(key, int):
            return key * 283 % self.__size
        elif isinstance(key, str):
            return sum([ord(char) for char in key]) * 283 % self.__size
        else:
            raise ValueError("Unsupported key type. Only integers and strings are supported.")

    def set(self, key, value):
        index = self.__hash(key)
        if self.__buckets[index] is None:
            self.__buckets[index] = LinkedList()

        self.__buckets[index].insert((key, value))

    def get(self, key):
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
        return self.get(key) is not None

    def keys(self):
        keys = []
        for bucket in self.__buckets:
            curr = bucket.head if bucket else None
            while curr:
                keys.append(curr.value[0])
                curr = curr.next
        return keys