import pytest
from code_challange_class31.hashmap_repeated_word.hashmap_repeated_word import repeated_word

def test_repeated_word():
    input1 = "Once upon a time, there was a brave princess who..."
    assert repeated_word(input1) == "a"

    input2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert repeated_word(input2) == "it"

    input3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert repeated_word(input3) == "summer"

if __name__ == "__main__":
    pytest.main()
