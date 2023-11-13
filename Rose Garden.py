from typing import List


def roseGarden(arr: List[int], r: int, b: int):
    low = 1
    high = 1000000000
    answer = -1

    def canPickRoses(days: int) -> bool:
        roses = 0
        bouq = 0

        for rose in arr:
            if rose <= days:
                roses += 1
                if roses == r:
                    bouq += 1
                    roses = 0
                    if bouq == b:
                        return True
            else:
                roses = 0
        return bouq >= b

    while low <= high:
        mid = low + (high-low)//2

        if canPickRoses(mid):
            high = mid - 1
            answer = mid
        else:
            low = mid + 1


    return answer
