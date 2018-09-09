def mergeSort(arr):
    mergeSortAdv(arr, 0, len(arr) - 1)
    return arr


def mergeSortAdv(arr, first, last):
    if first < last:
        middle = (first + last) // 2
        mergeSortAdv(arr, first, middle)
        mergeSortAdv(arr, middle + 1, last)
        merge(arr, first, middle + 1, last)


def merge(arr, first, middle, last):
    L = arr[first:middle]
    R = arr[middle:last + 1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0

    for k in range(first, last + 1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


print(mergeSort([2, 3, 4, 1, 5, 4, 67, 4, 3, 4, 1]))
