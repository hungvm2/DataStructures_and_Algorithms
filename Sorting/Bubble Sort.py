def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return arr

print(bubblesort([4,1,7,8,4,2,0,0,5]))

