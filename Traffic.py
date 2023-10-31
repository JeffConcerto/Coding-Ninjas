from collections import deque

def traffic(n: int, m: int, vehicle: [int]) -> int:
    maxCount = 0
    count = 0
    used = 0
    usedQueue = deque()

    for (i, num) in enumerate(vehicle):
        if num == 1:
            count += 1
        else:
            if used == m:
                firstIndex = usedQueue.popleft()
                count = i - firstIndex
            else:
                used += 1
                count += 1
            usedQueue.append(i)   
        
        maxCount = max(maxCount, count)
    
    return maxCount

