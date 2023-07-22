[&leftarrow; Back to Home](../README.md)

Author: **Almothana Almasri**

# Code Challenge: Class 28: Sorting: Comparisons

When sorting an array, a key step in the algorithm is determining what their order should be. In the insertion sort algorithm, the insertion phase has a while loop that checks for whether the number to insert is less than the number at the iteration index. The first time the number to insert is greater, the algorithm inserts at the previous index. Merge Sort applies the same logic when recombining sub-arrays, as it needs to choose whether to pull from the left or the right array.

## [Code is here](comparisons/comparisons.py)

## Efficiency:

1. `sort_by_year` function:
   - Time Complexity: O(n*log(n)), where n is the number of movies.
   - Space Complexity: O(n), as the `sorted` function creates a new list of the same size as the input.

2. `sort_by_title` function:
   - Time Complexity: O(n * m * log(n)), where n is the number of movies, and m is the average length of the movie titles.
   - Space Complexity: O(n), as the `sorted` function creates a new list of the same size as the input. The extra space used by the `ignore_leading_articles` function is constant and does not depend on the input size.

## Tests

[They are linked here](tests/test_comparisons.py)

```bash
pytest -v code_challange_class28/tests/test_comparisons.py
```