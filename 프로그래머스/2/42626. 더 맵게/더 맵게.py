"""
문제 유형 : 힙
아이디어 :
- 모든 음식의 스코빌 지수가 k 이상일 때 까지 반복하여 섞는다.
    -> 힙을 이용하여 2개의 원소를 pop 후
    -> 새로운 원소를 만들어 push
- while len(q)>1, 종료 조건은 q[0]이 k>=일 때,
"""
from heapq import heappush, heappop, heapify
def solution(scoville, K):
    q = scoville
    heapify(q)
    answer = 0
    while len(q)>=2:
        a, b = heappop(q), heappop(q)
        if a>=K:
            return answer
        heappush(q, a+b*2)
        answer += 1
    return answer if q[0]>=K else -1