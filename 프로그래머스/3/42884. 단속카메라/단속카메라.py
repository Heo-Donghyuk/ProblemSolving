from collections import deque
def solution(routes):
    routes = deque(sorted([[min(a, b), max(a, b)] for a, b in routes]))
    answer, lastCamPos = 0, [-10**6, -10**6]
    while routes:
        i, o = routes.popleft()
        if lastCamPos[1]<i:
            lastCamPos = [i, o]
            answer+=1
        else:
            x, y = lastCamPos
            lastCamPos = [max(i, x), min(o, y)]
    return answer