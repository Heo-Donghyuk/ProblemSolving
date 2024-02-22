"""
유형: 완전 탐색, DFS, 백트래킹
아이디어:
- 출발지에서 도착지로 갈 수 있는 남은 티켓 수를 저장하는 카운터 딕셔너리를 만들어 사용하자
- DFS를 이용하여 완전 탐색
    - 종료 조건:
        - 더이상 갈 수 없을 때, answer가 tickets길이 +1이라면 정답
    - DFS(사용한 티켓, 남은 티켓)
주의:
- 시간복잡도:
- 조건:
    - 주어진 항공권을 모두 사용해야 한다.
    - 알파벳 순서가 앞서는 경로를 선택해야 한다.
- 예외:
    - 티켓이 2개 있을 수 있다.
"""
def DFS(answer, ticketDict, target):
    if len(answer)==target:
        return True
    cur = answer[-1]
    for nextDeparture in sorted(ticketDict[cur].keys()):
        if ticketDict[cur][nextDeparture]==0:
            continue
        ticketDict[cur][nextDeparture]-=1
        answer.append(nextDeparture)
        if DFS(answer, ticketDict, target):
            return True
        ticketDict[cur][nextDeparture]+=1
        answer.pop()
    return False

from collections import defaultdict, Counter

def solution(tickets):
    ticketDict = defaultdict(Counter)
    for departure, arrival in tickets:
        ticketDict[departure][arrival]+=1
    answer = ['ICN']
    DFS(answer, ticketDict, len(tickets)+1)
    return answer