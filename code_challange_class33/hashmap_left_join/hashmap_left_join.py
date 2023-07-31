def left_join(synonyms, antonyms):
    result = []

    for key in synonyms:
        synonym_value = synonyms[key]

        if key in antonyms:
            antonym_value = antonyms[key]
        else:
            antonym_value = None

        result.append([key, synonym_value, antonym_value])

    return result