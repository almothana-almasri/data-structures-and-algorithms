from code_challange_class27.merge_sort.merge_sort import *

def test_merge_sort():
    # Test Case 1 (Sample Array)
    arr = [8, 4, 23, 42, 16, 15]
    merge_sort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

    # Test Case 2 (Reverse-sorted)
    arr = [20, 18, 12, 8, 5, -2]
    merge_sort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

    # Test Case 3 (Few uniques)
    arr = [5, 12, 7, 5, 5, 7]
    merge_sort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

    # Test Case 4 (Nearly-sorted)
    arr = [2, 3, 5, 7, 13, 11]
    merge_sort(arr)
    assert arr == [2, 3, 5, 7, 11, 13]

    # Test Case 5 (Empty array)
    arr = []
    merge_sort(arr)
    assert arr == []

    # Test Case 6 (Array with a single element)
    arr = [42]
    merge_sort(arr)
    assert arr == [42]
