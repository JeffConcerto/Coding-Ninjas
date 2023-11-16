def aggressiveCows(stalls, k):
    stalls.sort()
    low = 1
    high = stalls[-1]
    answer = -1

    def canPlaceCows(distance: int) -> bool:
        cowsPlaced = 1
        previous = stalls[0]
        for i in range(1,len(stalls)):
            if stalls[i] - previous >= distance:
                cowsPlaced += 1
                previous = stalls[i]
                if cowsPlaced == k:
                    return True
        return cowsPlaced == k
    
    while low <= high:
        mid = low + (high-low)//2

        if canPlaceCows(mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return answer


