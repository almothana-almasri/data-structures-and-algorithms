from code_challange_class33.hashmap_left_join.hashmap_left_join import left_join
from code_challange_class33.hashmap_left_join.hashtable import HashTable

def test_left_join_basic():
    synonyms_hashmap = {
        'diligent': 'employed',
        'fond': 'enamored',
        'guide': 'usher',
        'outfit': 'garb',
        'wrath': 'anger'
    }

    antonyms_hashmap = {
        'diligent': 'idle',
        'fond': 'averse',
        'guide': 'follow',
        'flow': 'jam',
        'wrath': 'delight'
    }

    result = left_join(synonyms_hashmap, antonyms_hashmap)
    assert result == [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"]
    ]

def test_left_join_empty():
    result = left_join({}, {})
    assert result == []

def test_left_join_missing_antonyms():
    synonyms_hashmap = {
        'diligent': 'employed',
        'fond': 'enamored',
        'guide': 'usher'
    }

    antonyms_hashmap = {
        'flow': 'jam',
        'wrath': 'delight'
    }

    result = left_join(synonyms_hashmap, antonyms_hashmap)
    assert result == [
        ["diligent", "employed", None],
        ["fond", "enamored", None],
        ["guide", "usher", None]
    ]
