from code_challange_class33.hashmap_left_join.hashmap_left_join import left_join
from code_challange_class33.hashmap_left_join.hashtable import HashTable
import pytest

# Test when there are matching keys in synonyms and antonyms
def test_left_join_matching_keys():
    synonyms = {'happy': 'joyful', 'sad': 'unhappy', 'fast': 'quick'}
    antonyms = {'happy': 'unhappy', 'tall': 'short', 'fast': 'slow'}

    result = left_join(synonyms, antonyms)

    assert result.get('happy') == ['joyful', 'unhappy']
    assert result.get('fast') == ['quick', 'slow']
    assert result.get('sad') == ['unhappy', None]

# Test when there are only synonyms and no antonyms
def test_left_join_only_synonyms():
    synonyms = {'hot': 'warm', 'cold': 'chilly', 'fast': 'rapid'}
    antonyms = {}

    result = left_join(synonyms, antonyms)

    assert result.get('hot') == ['warm', None]
    assert result.get('cold') == ['chilly', None]
    assert result.get('fast') == ['rapid', None]

# Test when there are only antonyms and no synonyms
def test_left_join_only_antonyms():
    synonyms = {}
    antonyms = {'happy': 'unhappy', 'tall': 'short', 'fast': 'slow'}

    result = left_join(synonyms, antonyms)

    assert result.get('happy') == [None, 'unhappy']
    assert result.get('tall') == [None, 'short']
    assert result.get('fast') == [None, 'slow']

if __name__ == "__main__":
    pytest.main()