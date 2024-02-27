from collections import deque
import sys
input=sys.stdin.readline

def bfs(graph,sp):
    queue=deque([])
    t=0
    for si,sj in sp:
        queue.append((t,si,sj))
    
    while queue:
        t,i,j=queue.popleft()
        if i+1<n and graph[i+1][j]==0:
            graph[i+1][j]=1
            queue.append((t+1,i+1,j))
        if i-1>-1 and graph[i-1][j]==0:
            graph[i-1][j]=1
            queue.append((t+1,i-1,j))
        if j+1<m and graph[i][j+1]==0:
            graph[i][j+1]=1
            queue.append((t+1,i,j+1))
        if j-1>-1 and graph[i][j-1]==0:
            graph[i][j-1]=1
            queue.append((t+1,i,j-1))
    
    return graph,t

m,n=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

sp=[(i,j) for i in range(n) for j in range(m) if graph[i][j]==1]
graph,result=bfs(graph,sp)

for i in range(n):
    if not all(graph[i]):
        print(-1)
        quit()
        
print(result)