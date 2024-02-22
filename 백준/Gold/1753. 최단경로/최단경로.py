import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

inf = 10**9
v, e = map(int, input().split())
start = int(input())
graph = {i: {i:0} for i in range(v+1)}
answer = [inf] * (v+1)
for _ in range(e):
    u, v, w = map(int, input().split())
    if v not in graph[u] or graph[u][v]>w:
        graph[u][v]=w
    
def djikstra(start):
    q = [(0, start)]
    while q:
        cost, node = heapq.heappop(q)
        if cost>answer[node]:
            continue
        else:
            for i, b in graph[node].items():
                if cost+b<answer[i]:
                    answer[i]=cost+b
                    q.append((answer[i], i))
    for i in answer[1:]:
        print((str(i) if i!=inf else 'INF')+'\n')
djikstra(start)