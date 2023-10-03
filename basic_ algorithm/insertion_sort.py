arr = [8, 2, 5, 7, 3, 1, 9, 0]
print(arr)
for i in range(1, len(arr)):
    j = i
    while j >= 1 and arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j = j - 1
        print(arr)
