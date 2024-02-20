from collections import deque
def solution(scoville, K):
    inf = 10**9
    q = deque(sorted(scoville))
    mix = deque()
    answer = 0
    while len(q)+len(mix)>=2:
        if min(q[0] if q else inf, mix[0] if mix else inf)>=K:
            return answer
        temp = []
        for _ in range(2):
            if q and not mix:
                temp.append(q.popleft())
            elif q and mix:
                if q[0]<mix[0]:
                    temp.append(q.popleft())
                else:
                    temp.append(mix.popleft())
            elif not q and mix:
                temp.append(mix.popleft())
        mix.append(temp[0]+temp[1]*2)
        answer+=1
    return answer if mix[0]>=K else -1