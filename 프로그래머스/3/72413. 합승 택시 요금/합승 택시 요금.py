from heapq import *

def dijkstra(n, start, graph):
    INF = 10**9
    res = [INF]*(n+1)
    q = [(0, start)]
    while q:
        cost, node = heappop(q)
        if cost>res[node]:
            continue
        for nextNode, nextCost in graph[node].items():
            totalCost = cost+nextCost
            if res[nextNode]>totalCost:
                res[nextNode]=totalCost
                heappush(q, (totalCost, nextNode))
    return res

def solution(n, s, a, b, fares):
    graph = {i:{i:0} for i in range(n+1)}
    for node1, node2, cost in fares:
        graph[node1][node2]=cost
        graph[node2][node1]=cost
    
    S, A, B = dijkstra(n, s, graph), dijkstra(n, a, graph), dijkstra(n, b, graph)
    answer = 10**9
    for i in range(1, n+1):
        answer = min(answer, S[i]+A[i]+B[i])
    return answer