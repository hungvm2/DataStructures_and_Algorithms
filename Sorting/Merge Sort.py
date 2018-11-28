def mergesort(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        mid = n//2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        result = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+= 1
            else:
                result.append(right[j])
                j+= 1
        result += left[i:] + right[j:]
        return result

print(mergesort([2,4,1,8,6,3,9]))