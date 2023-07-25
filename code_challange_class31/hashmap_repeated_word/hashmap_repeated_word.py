from  code_challange_class31.hashmap_repeated_word.hashtable import HashTable

def repeated_word(string):
    """
    Find the first repeated word in the input string.

    Args:
    string (str): The input string to search for repeated words.

    Returns:
    str or None: The first repeated word found, or None if no repeated word is found.
    """
    hashtable = HashTable()

    words = string.lower().split()

    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if cleaned_word:
            if hashtable.has(cleaned_word):
                return cleaned_word
            else:
                hashtable.set(cleaned_word.lower(), cleaned_word)

    return None
