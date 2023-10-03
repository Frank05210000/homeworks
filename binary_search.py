def binarySearch(minIndex, maxIndex):
    if (minIndex <= maxIndex):
        medium = (minIndex+maxIndex)//2
        if (target > arr[medium]):
            minIndex = medium+1
            binarySearch(minIndex, maxIndex)
        elif (target < arr[medium]):
            maxIndex = medium-1
            binarySearch(minIndex, maxIndex)
        elif (target == arr[medium]):
            print("at index "+str(medium))
        else:
            print("not found in the array.")


arr = [12, 23, 34, 46, 54, 68, 78, 84, 92]
target = 23
binarySearch(1, len(arr)-1)
