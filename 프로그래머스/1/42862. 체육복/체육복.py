def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    duplicate = set(lost)&set(reserve)
    lost = [i for i in lost if i not in duplicate]
    reserve = [i for i in reserve if i not in duplicate]
    answer = n-len(lost)
    l, r = 0, 0
    while l<len(lost) and r<len(reserve):
        lVal, rVal =lost[l], reserve[r]
        if lVal<rVal-1:
            l+=1
        elif rVal-1<=lVal<=rVal+1:
            answer+=1
            l+=1
            r+=1
        else:
            r+=1
    return answer