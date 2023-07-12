def insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    sorted_arr = [arr[0]]
    for i in range(1, len(arr)):
        insert(sorted_arr, arr[i])
    return sorted_arr

def insert(sorted_arr, value):
    i = 0
    while value > sorted_arr[i]:
        i += 1
        if i == len(sorted_arr):
            break
    while i < len(sorted_arr):
        temp = sorted_arr[i]
        sorted_arr[i] = value
        value = temp
        i += 1
    sorted_arr.append(value)
