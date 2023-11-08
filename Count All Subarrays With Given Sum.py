from os import *
from sys import *
from collections import *
from math import *

def findAllSubarraysWithGivenSum(arr, s):
    count = 0
    sum = 0
    left = 0

    for right in range(len(arr)):
        sum += arr[right]

        while left <= right and sum > s:
            sum -= arr[left]
            left += 1
        
        if sum == s:
            count += 1
    
    return count
