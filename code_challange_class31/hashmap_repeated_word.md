[&leftarrow; Back to Home](../README.md)

Author: **Almothana Almasri**

## Code Challenge: Class 31: Find the first repeated word in a book.

Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string

## Whiteboard

![whiteboardd](../assets/CC_31.png)

## [Code is here](hashmap_repeated_word/hashmap_repeated_word.py)

## Approach

1. Convert the input string to lowercase to make the word comparisons case-insensitive.
2. Remove punctuation marks (commas and periods) from the input string.
3. Split the input string into individual words using whitespace as the delimiter.
4. Create an empty dictionary `word_freq` to store word frequencies.
5. Iterate through each word in the list of words:
   - If the word is already present in the `word_freq` dictionary, it means it's a repeated word, so return it as the first repeated word.
   - If the word is not present in the `word_freq` dictionary, add it with a frequency of 1.
6. If no repeated word is found during the iteration, return `None` to indicate that there are no repeated words in the input string.

## Efficiency

- Time Complexity: O(n)
  - Converting the input string to lowercase: O(n)
  - Removing punctuation marks (commas and periods): O(n)
  - Splitting the input string into words: O(n)
  - Iterating through each word and dictionary lookup/insertion: O(n)
  - In the worst case, the entire process takes O(n) time, where n is the length of the input string.

- Space Complexity: O(n)
  - The `words` list to store individual words: O(n)
  - The `word_freq` dictionary to store word frequencies: O(n)
  - In the worst case, both the list and dictionary combined take O(n) space, where n is the number of words in the input string.

## Tests

[They are linked here](tests/test_hashmap_repeated_word.py)

```bash
pytest -v code_challange_class31/tests/test_hashmap_repeated_word.py
```