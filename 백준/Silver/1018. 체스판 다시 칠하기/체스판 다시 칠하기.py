"""
유형:
아이디어:
1. 완전 탐색 - 시간 복잡도 O(n^4)
2. 누적합을 이용 - 시간 복잡도 O(n^2)
    - W, B를 가로, 세로열에 대해 번갈아가며, 동일하면 0, 동일하지 않으면 1로 누적합을 만든다.
주의:
-시간복잡도
-예외:
    - 시작점을 w, b 중 어떤 것으로 하느냐에 따라 바꿔야 할 칸의 수가 달라진다
        - min(누적합, 전체칸-누적합)으로 누적합의 최솟값을 구해야 한다.
"""
n, m = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    target = True if i%2 else False
    for j, val in enumerate(map(lambda x: {'B': True, 'W': False}[x], input()), start=1):
        graph[i][j]=graph[i-1][j]+graph[i][j-1]-graph[i-1][j-1]+int(val==target)
        target = not target
answer = 10**9     
for i in range(8, n+1):
    for j in range(8, m+1):
        val = graph[i][j]-graph[i-8][j]-graph[i][j-8]+graph[i-8][j-8]
        val = min(val, 8*8-val)
        answer = min(answer, val)
print(answer)
