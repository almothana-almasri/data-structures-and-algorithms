from code_challange_class26.insertion_sort.insertion_sort import *

def test_insertion_sort():
    # Test case 1: Sample array [8,4,23,42,16,15]
    arr1 = [8, 4, 23, 42, 16, 15]
    assert insertion_sort(arr1) == [4, 8, 15, 16, 23, 42]

    # Test case 2: Reverse-sorted array [20,18,12,8,5,-2]
    arr2 = [20, 18, 12, 8, 5, -2]
    assert insertion_sort(arr2) == [-2, 5, 8, 12, 18, 20]

    # Test case 3: Few uniques array [5,12,7,5,5,7]
    arr3 = [5, 12, 7, 5, 5, 7]
    assert insertion_sort(arr3) == [5, 5, 5, 7, 7, 12]

    # Test case 4: Nearly-sorted array [2,3,5,7,13,11]
    arr4 = [2, 3, 5, 7, 13, 11]
    assert insertion_sort(arr4) == [2, 3, 5, 7, 11, 13]

    # Test case 5: Empty array []
    arr5 = []
    assert insertion_sort(arr5) == []

    # Test case 6: Array with a single element [5]
    arr6 = [5]
    assert insertion_sort(arr6) == [5]

    # Test case 7: Array with all elements being the same [10, 10, 10, 10, 10]
    arr7 = [10, 10, 10, 10, 10]
    assert insertion_sort(arr7) == [10, 10, 10, 10, 10]