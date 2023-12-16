from typing import List

def goodNumbers(a: int, b:int, digit:int) -> List[int]:
    if a > b:
        return []
    
    num = b
    sum = None
    isGood = True
    while num > 0:
        dig = num % 10
        if dig == digit:
            isGood = False
            break
        if sum == None:
            sum = dig
        else:
            if dig < sum:
                isGood = False
                break
            sum += dig
        num //= 10
    returnVal = [b] if isGood else []
    return goodNumbers(a,b-1,digit) + returnVal
