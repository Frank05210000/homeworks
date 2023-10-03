arr = [8, 2, 5, 7, 3, 1, 9, 0]
print(arr)  # original array

for i in range(len(arr)-1):
    minIndex = i
    for j in range(i+1, len(arr)):
        if (arr[j] < arr[minIndex]):
            minIndex = j
    if (minIndex != i):
        arr[minIndex], arr[i] = arr[i], arr[minIndex]
    print(arr)
