from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    INF = 10**9
    graph = {i: {i:0} for i in range(n+1)}
    for node1, node2, cost in fares:
        graph[node1][node2] = cost
        graph[node2][node1] = cost
    
    def djikstra(start):
        res = [INF] * (n+1)
        q = [(0, start)]
        while q:
            curCost, curNode = heappop(q)
            if curCost>res[curNode]:
                continue
            else:
                for nextNode, cost in graph[curNode].items():
                    nextCost = curCost+cost
                    if nextCost<res[nextNode]:
                        res[nextNode]=nextCost
                        heappush(q, (nextCost, nextNode))
        return res
    
    ansGraph = [djikstra(i) for i in range(n+1)]
    answer = min([ansGraph[s][i]+ansGraph[i][a]+ansGraph[i][b] for i in range(n+1)])
    return answer