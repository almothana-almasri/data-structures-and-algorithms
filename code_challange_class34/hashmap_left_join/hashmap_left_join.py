from hashtable import HashTable

def most_common_word(book):
    word_count = HashTable()
    words = book.split()
    
    for word in words:
        word = word.strip(".,!?\"':;-").lower()
        
        if word_count.has(word):
            word_count.set(word, word_count.get(word) + 1)
        else:
            word_count.set(word, 1)

    all_keys = word_count.keys()
    most_common_word = max(all_keys, key=word_count.get)
    most_common_count = word_count.get(most_common_word)
    
    return most_common_word, most_common_count