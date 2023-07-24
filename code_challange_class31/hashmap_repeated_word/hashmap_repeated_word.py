def repeated_word(input_string):
    words = input_string.lower().replace(",", "").replace(".", "").split()

    word_freq = {}

    for word in words:
        if word in word_freq:
            return word
        else:
            word_freq[word] = 1

    return None