from code_challange_class33.hashmap_left_join.hashtable import HashTable

def left_join(synonyms_hash, antonyms_hash):
    result = []
    for key, value in synonyms_hash.items():
        synonym = value
        antonym = antonyms_hash.get(key, None)
        result.append([key, synonym, antonym])
    return result
