from itertools import combinations
def solution(friends, gifts):
    giftNum = {person: {m:{'send':0, 'receive':0} for m in friends} for person in friends}
    total = {m:{'send':0, 'receive':0} for m in friends}
    for gift in gifts:
        sender, receiver = gift.split()
        giftNum[sender][receiver]['send']+=1
        total[sender]['send']+=1
        giftNum[receiver][sender]['receive']+=1
        total[receiver]['receive']+=1
    answer = {person: 0 for person in friends}
    for p1, p2 in combinations(friends, 2):
        send1, send2 = giftNum[p1][p2]['send'], giftNum[p2][p1]['send']
        if send1>send2:
            answer[p1]+=1
        elif send1<send2:
            answer[p2]+=1
        else:
            t1, t2 = total[p1]['send']-total[p1]['receive'], total[p2]['send']-total[p2]['receive']
            if t1>t2:
                answer[p1]+=1
            elif t1<t2:
                answer[p2]+=1
            
    return max(answer.values())