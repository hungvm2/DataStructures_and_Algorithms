def insertionsort(arr):
    n = len(arr)
    for i in range(n):
        next_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > next_element:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = next_element
    return arr

print(insertionsort([3,5,1,2,8,-2,1,2,0,7]))