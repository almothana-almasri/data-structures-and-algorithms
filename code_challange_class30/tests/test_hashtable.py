import pytest
from code_challange_class30.hashtable.hashtable import HashTable

# Test set and get methods
def test_set_and_get():
    hashtable = HashTable()
    hashtable.set("apple", 5)
    assert hashtable.get("apple") == 5

# Test key existence
def test_has():
    hashtable = HashTable()
    hashtable.set("apple", 5)
    assert hashtable.has("apple") == True
    assert hashtable.has("banana") == False

# Test collision handling
def test_collision_handling():
    hashtable = HashTable()
    hashtable.set("lemon", 10)
    hashtable.set("melon", 15)
    assert hashtable.get("lemon") == 10
    assert hashtable.get("melon") == 15

# Test keys method
def test_keys():
    hashtable = HashTable()
    hashtable.set("apple", 5)
    hashtable.set("lemon", 10)
    hashtable.set("melon", 15)
    assert set(hashtable.keys()) == set(["apple", "lemon", "melon"])

# Test non-existing key
def test_non_existing_key():
    hashtable = HashTable()
    hashtable.set("apple", 5)
    assert hashtable.get("banana") is None

# Test hashing to an in-range value
def test_hashing_in_range():
    hashtable = HashTable()
    key = "hello"
    index = hashtable._HashTable__hash(key)
    assert 0 <= index < hashtable._HashTable__size

if __name__ == "__main__":
    pytest.main()
