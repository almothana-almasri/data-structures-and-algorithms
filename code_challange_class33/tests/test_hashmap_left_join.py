from code_challange_class33.hashmap_left_join.hashmap_left_join import left_join
from code_challange_class33.hashmap_left_join.hashtable import HashTable

# Test with both synonym and antonym present
def test_left_join_with_both_present():
    synonyms_hash = HashTable()
    antonyms_hash = HashTable()

    synonyms_hash.set("diligent", "employed")
    antonyms_hash.set("diligent", "idle")

    synonyms_hash.set("fond", "enamored")
    antonyms_hash.set("fond", "averse")

    result = left_join(synonyms_hash, antonyms_hash)
    assert result == [["fond", "enamored", "averse"], ["diligent", "employed", "idle"]]

# Test with only synonym present (antonym is None)
def test_left_join_with_synonym_only():
    synonyms_hash = HashTable()
    antonyms_hash = HashTable()

    synonyms_hash.set("guide", "usher")

    result = left_join(synonyms_hash, antonyms_hash)
    assert result == [["guide", "usher", None]]

# Test with only antonym present (synonym is None)
def test_left_join_with_antonym_only():
    synonyms_hash = HashTable()
    antonyms_hash = HashTable()

    antonyms_hash.set("flow", "jam")

    result = left_join(synonyms_hash, antonyms_hash)
    assert result == [["flow", None, "jam"]]
