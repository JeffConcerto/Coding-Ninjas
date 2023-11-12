def findPeakElement(arr: [int]) -> int:
    low = 1
    high = len(arr)-2

    if arr[0] > arr[1]:
        return 0
    elif arr[-1] > arr[-2]:
        return len(arr)-1

    while low <= high:
        mid = low + (high-low)//2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:
            low = mid+1
        else:
            high = mid-1
    
    return low
