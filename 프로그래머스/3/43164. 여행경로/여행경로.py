"""
문제 유형 : DFS
아이디어 :
- DFS를 이용해야겠구나
주의 : 똑같은 티켓이 2개 있을 수 있다. -> visited를 set말고 리스트로 이용하자
"""
def solution(tickets):
    tickets.sort()
    used = [0]*len(tickets)
    answer = ['ICN']
    def DFS():
        if len(answer)==len(tickets)+1:
            return True
        for i, (departure, arrival) in enumerate(tickets):
            if not used[i] and departure==answer[-1]:
                used[i]=1
                answer.append(arrival)
                if DFS():
                    return True
                used[i]=0
                answer.pop()
        return False
    DFS()
    return answer