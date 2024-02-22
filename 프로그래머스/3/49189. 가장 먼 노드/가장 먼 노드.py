"""
유형: BFS
아이디어:
- 간선들의 정보로 한 노드에서 이동할 수 있는 다른 노드들의 정보를 저장하는 딕셔너리를 만들자
- BFS로 노드를 탐색하자
    - visited를 이용하여 중복 방문 방지
    - 큐에서 pop 한 결과(거리)를 리스트에 저장하자
    - 저장한 결과들 중 가장 큰 값의 개수를 세자 -> 정답으로 반환
주의:
-시간복잡도
-조건
-예외
"""
from collections import deque, defaultdict
def solution(n, edge):
    answer = []
    graph = defaultdict(list)
    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)
    q = deque([(0, 1)])
    visited = set([1])
    while q:
        dist, cur = q.popleft()
        answer.append(dist)
        for nextNode in graph[cur]:
            if nextNode not in visited:
                visited.add(nextNode)
                q.append((dist+1, nextNode))
    return answer.count(max(answer))