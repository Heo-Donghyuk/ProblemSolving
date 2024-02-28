import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
edges = {i: [] for i in range(n+1)}
parent = [0]*(n+1)
parent[1]=1
for _ in range(n-1):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    edges[node2].append(node1)
    
q = deque([1])
while q:
    cur = q.popleft()
    for nextNode in edges[cur]:
        if parent[nextNode]==0:
            parent[nextNode]=cur
            q.append(nextNode)

for n in parent[2:]:
    print(n)