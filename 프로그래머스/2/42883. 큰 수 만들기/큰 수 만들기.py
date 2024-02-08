def solution(number, k):
    i = 0
    while k:
        curIdx, nextIdx = i, (i+1)%len(number)
        if number[curIdx]<number[nextIdx]:
            number = number[:curIdx]+number[curIdx+1:]
            k-=1
            i = max(0, i-1)
            continue
        else:
            i = (i+1)%len(number)
    return number