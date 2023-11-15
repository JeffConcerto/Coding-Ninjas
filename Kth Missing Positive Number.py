from typing import *

#Brute Force
def missingK(vec: List[int], n: int, k: int) -> int:
    for num in vec:
        if k < num:
            return k
        k += 1
    return k


#Optimal
def missingK(vec: List[int], n: int, k: int) -> int:
    low = 0
    high = n-1

    while low <= high:
        mid = low + (high-low)//2

        missing = vec[mid] - (mid + 1)

        if missing < k:
            low = mid+1
        else:
            high = mid-1
    
    return low + k
