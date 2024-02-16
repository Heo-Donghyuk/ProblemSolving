import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write
V, E = map(int, input().split())
start = int(input())
INF = 10**9
graph = {i:{i:0} for i in range(V+1)}
for _ in range(E):
    node1, node2, cost = map(int, input().split())
    graph[node1][node2] = cost if node2 not in graph[node1] else min(graph[node1][node2], cost)

def djikstra(start):
    q = [(0, start)]
    answer = [INF]*(V+1)
    while q:
        curCost, curNode = heapq.heappop(q)
        if curCost>answer[curNode]:
            continue
        else:
            for nextNode, nextCost in graph[curNode].items():
                if curCost+nextCost < answer[nextNode]:
                    answer[nextNode]=curCost+nextCost
                    heapq.heappush(q, (curCost+nextCost, nextNode))
    for num in answer[1:]:
        print((str(num) if num!=INF else 'INF')+'\n')
djikstra(start)