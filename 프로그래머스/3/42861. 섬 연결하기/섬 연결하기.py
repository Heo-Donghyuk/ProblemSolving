def find(graph, node):
    if graph[node]!=node:
        graph[node]=find(graph, graph[node])
    return graph[node]
def union(graph, node1, node2):
    root1, root2 = find(graph, node1), find(graph, node2)
    if root1<root2:
        graph[root2]=root1
    else:
        graph[root1]=root2
def solution(n, costs):
    graph = [i for i in range(n)]
    answer = 0
    for node1, node2, cost in sorted(costs, key=lambda x: x[-1]):
        if find(graph, node1)!=find(graph, node2):
            union(graph, node1, node2)
            answer+=cost
    return answer