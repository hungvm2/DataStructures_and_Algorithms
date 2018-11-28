def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        left = []
        equal = []
        right = []
        pivot = arr[0]
        for val in arr:
            if val < pivot:
                left.append(val)
            elif val == pivot:
                equal.append(val)
            else:
                right.append(val)
    return quicksort(left) + equal + quicksort(right)
        
print(quicksort([2,5,1,3,8,6,9,4,3]))