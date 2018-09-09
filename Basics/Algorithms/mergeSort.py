#   merge 2 sorted arrays

def mergeSort(arr1, arr2):
    result = [0] * (len(arr1) + len(arr2))
    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i = i + 1
            k = k + 1
        else:
            result[k] = arr2[j]
            j = j + 1
            k = k + 1

    while i < len(arr1):
        result[k] = arr1[i]
        i = i + 1
    while j < len(arr2):
        result[k] = arr2[j]
        j = j + 1
    return result


print(mergeSort([3, 7, 12, 18], [2, 5, 16, 21]))
