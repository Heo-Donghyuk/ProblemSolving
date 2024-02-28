"""
유형:
아이디어:
- 참을 말해야만 하는 사람이 파티에 있으면 그 파티에서는 참을 말해야 한다.
    - 그 파티에 참여한 모든 사람들에게 참을 말해야 하고
        - 그 사람이 참여한 다른 파티에도 항상 참을 말해야 한다.
        => 연결되어있으면 참을 말해야 한다.
         -> 연결되어있다 -> 한 그래프 내에 속한다 -> 유니온파인드?
- 항상 참을 말해야 하는 사람들의 루트 노드를 0으로 하자
- 각 파티를 입력받아 각 사람들끼리 union 하자
    - 각 사람들에 대해 find하고
        - find의 결과가 가장 작은 노드를 root 노드로하여
        - 파티에 속하는 모든 사람들의 root 노드를 위에서 얻은 루트 노드로 바꿔주자
- 이후 각 파티를 입력받아
    - 모든 사람에 대해 find 연산했을 때 0이 하나도 없다면 count+=1
주의:
-시간복잡도
-예외
"""
import sys
input = sys.stdin.readline

def find(node, roots):
    if node!=roots[node]:
        roots[node]=find(roots[node], roots)
    return roots[node]
def union(node1, node2, roots):
    root1, root2 = find(node1, roots), find(node2, roots)
    if root1>root2:
        roots[root1]=root2
    else:
        roots[root2]=root1

n, m = map(int, input().split())
roots = [i for i in range(n+1)]
_, *initMember = map(int, input().split())
for i in initMember:
    roots[i]=0
parties = []
for _ in range(m):
    __, *members = map(int, input().split())
    parties.append(members)
    leastMemberRoot = find(members[0], roots)
    for mem in members:
        curRoot = find(mem, roots)
        if curRoot<leastMemberRoot:
            leastMemberRoot=curRoot
    for mem in members:
        union(leastMemberRoot, mem, roots)
        
answer = 0
for party in parties:
    if all(find(mem, roots)!=0 for mem in party):
        answer+=1
print(answer)