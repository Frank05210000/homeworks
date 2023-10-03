arr = [8, 2, 5, 7, 3, 1, 9, 0]
target = 7
check = False
for i in range(len(arr)-1):
    if (arr[i] == target):
        print('at index '+str(i))
        check = True

if (check == False):
    print("not found in the array.")
