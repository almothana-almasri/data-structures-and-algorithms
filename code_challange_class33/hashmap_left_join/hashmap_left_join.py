from code_challange_class33.hashmap_left_join.hashtable import HashTable

def left_join(synonyms, antonyms):
    result = HashTable()

    for key in synonyms.keys():
        result.set(key, [synonyms.get(key), antonyms.get(key)])

    return result