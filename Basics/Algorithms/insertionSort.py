def insertionSort(arr):
    print(arr)
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            swap = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = swap
            j = j - 1
    print(arr)
    print("-"*len(arr)*3)

insertionSort([3, 2, 3, 1,7])
