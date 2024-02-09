def solution(people, limit):
    people.sort()
    minIdx, maxIdx = 0, len(people)-1
    answer = 0
    while minIdx<maxIdx:
        if people[minIdx]+people[maxIdx]>limit:
            maxIdx-=1
        else:
            minIdx+=1
            maxIdx-=1
        answer+=1
    if minIdx==maxIdx:
        answer+=1
    return answer