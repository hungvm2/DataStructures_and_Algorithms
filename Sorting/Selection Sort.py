def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(i,n,1):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return arr

print(selectionsort([3,5,1,2,8,-2,1,2,0,7]))