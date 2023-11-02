def majorityElement(v: [int]) -> int:
    num = v[0]
    count = 1

    for i in range(1,len(v)):
        if v[i] == num:
            count += 1
        else:
            if count == 0:
                num = v[i]
                count = 1
            else:
                count -= 1
    

    return num
