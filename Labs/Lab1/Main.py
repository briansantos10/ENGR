def selection_sort(arr):
    for i in range(len(arr) - 1):
        minIndex = i 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
    return arr

print(selection_sort([1,5,4,10,3,2]))
# Output: [1, 2, 3, 4, 5, 10]
