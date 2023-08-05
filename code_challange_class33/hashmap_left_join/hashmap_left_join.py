from code_challange_class33.hashmap_left_join.hashtable import HashTable

def left_join(synonyms, antonyms):
    result = HashTable()

    for key in synonyms:
        synonym_value = synonyms[key]

        if key in antonyms:
            antonym_value = antonyms[key]
        else:
            antonym_value = None

        result.set(key, [synonym_value, antonym_value])

    return result