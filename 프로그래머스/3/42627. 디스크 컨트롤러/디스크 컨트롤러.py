"""
유형: 그리디
아이디어:
- 작업의 대기시간을 최소로 하기
- 작업 a가 끝났을 때, 대기 목록에 b, c가 있다고 하자
    - b는 9초, c는 6초가 걸린다.
    - b를 선택한다면
        - c, d,e..등 남은 작업들이 대기 시간이 9초씩 늘어난다
    - c를 선택한다면
        - b, d.. 남은 작업들의 대기 시간이 6초씩 늘어난다.
    => 남은 작업 중 수행 시간이 적은 작업을 우선 처리하자
        -> 수행시간이 가장 적게 남은 원소를 어떻게 고르지?
        - 순차 탐색 : n
        - 힙 : 1 -> 힙을 사용하자.
구체화:
- jobs를 요청 시점 순으로 정렬하자(deque or list(reversed))
- 힙에 최초 원소를 넣자
- 힙에서 원소를 빼고 대기시간을 구해 answer에 더하자
- 현재 시간 까지 요청이 들어온 원소들을 대기 큐(스택)에서 pop하여 heap에 넣자
- heap이 빌 때 까지 반복하자
- answer를 원소의 수로 나누어 주자 (소수점 이하는 버린다.)
"""
from heapq import heappush, heappop
def solution(jobs):
    n = len(jobs)
    jobs = sorted(jobs, reverse=True)
    time = jobs[-1][0]
    answer = 0
    q = [jobs.pop()[::-1]]
    while q:
        dueTime, requestTime = heappop(q)
        answer += max(time-requestTime, 0)+dueTime
        time=max(time, requestTime)+dueTime
        while jobs and jobs[-1][0]<=time:
            heappush(q, jobs.pop()[::-1])
        if not q and jobs:
            heappush(q, jobs.pop()[::-1])
    return answer//n