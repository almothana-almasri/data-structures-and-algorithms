from code_challange_class33.hashmap_left_join.hashmap_left_join import left_join
from code_challange_class33.hashmap_left_join.hashtable import HashTable
import pytest

# Test when there are matching keys in synonyms and antonyms
def test_left_join_matching_keys():
    synonyms = HashTable()
    synonyms.set('happy', 'joyful')
    synonyms.set('sad', 'unhappy')
    synonyms.set('fast', 'quick')

    antonyms = HashTable()
    antonyms.set('happy', 'unhappy')
    antonyms.set('tall', 'short')
    antonyms.set('fast', 'slow')

    result = left_join(synonyms, antonyms)

    assert result.get('happy') == ['joyful', 'unhappy']
    assert result.get('fast') == ['quick', 'slow']
    assert result.get('sad') == ['unhappy', None]

# Test when there are only synonyms and no antonyms
def test_left_join_only_synonyms():
    synonyms = HashTable()
    synonyms.set('hot', 'warm')
    synonyms.set('cold', 'chilly')
    synonyms.set('fast', 'rapid')

    antonyms = HashTable()

    result = left_join(synonyms, antonyms)

    assert result.get('hot') == ['warm', None]
    assert result.get('cold') == ['chilly', None]
    assert result.get('fast') == ['rapid', None]

# Test when both synonyms and antonyms have the same keys with different values
def test_left_join_conflicting_values():
    synonyms = HashTable()
    synonyms.set('happy', 'joyful')
    synonyms.set('sad', 'unhappy')
    synonyms.set('fast', 'quick')

    antonyms = HashTable()
    antonyms.set('happy', 'unhappy')
    antonyms.set('sad', 'happy')
    antonyms.set('fast', 'slow')

    result = left_join(synonyms, antonyms)

    assert result.get('happy') == ['joyful', 'unhappy']
    assert result.get('sad') == ['unhappy', 'happy']
    assert result.get('fast') == ['quick', 'slow']

if __name__ == "__main__":
    pytest.main()