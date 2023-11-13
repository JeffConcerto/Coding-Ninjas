from os import *
from sys import *
from collections import *
from math import *


def smallestDivisor(arr: [int], limit: int) -> int:
    low = 1
    high = 1000000
    answer = -1

    def canDivide(divi: int) -> bool:
        sum = 0

        for num in arr:
            sum += num // divi
            sum += 0 if num % divi == 0 else 1
            if sum > limit: 
                return False
        return sum <= limit

    while low <= high:
        mid = low + (high-low)//2


        if canDivide(mid):
            answer = mid
            high = mid-1
        else:
            low = mid+1
    return answer

