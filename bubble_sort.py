arr = [8, 2, 5, 7, 3, 1, 9, 0]
for i in range(len(arr)-1):
    flag = False
    for j in range(1, len(arr)-i):
        if (arr[j-1] > arr[j]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            flag = True
    if (flag == False):
        break
print(arr)
