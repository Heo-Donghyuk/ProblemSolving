"""
유형:
아이디어:
- board 초기화
    - 사각형을 하나씩 추가하면서 이동 가능한 좌표의 값을 1로 설정
        - 이미 -1이라면 1로 설정하지 않도록 주의
    - 이동 불가능한 사각형 내부의 값은 -1로 설정
        - 이미 1이어도 -1로 설정
    
- BFS
    - 큐에 다음으로 이동 가능한 좌표를 넣고 방문 처리
    - 큐에서 원소를 빼고
        - 타겟과 같은 좌표면 현재 step을 리턴(좌표를 2배 했으므로 //2를 리턴)
        - 다음 위치의 좌표를 방문하지 않았다면 큐에 넣고 방문처리
주의:
-시간복잡도
-조건 :
    - 꼭짓점에서 만나거나 변이 겹치는 경우, 지형이 2개 이상으로 분리된 경우도 없다.
-예외 : ㄷ자로 꺾인 부분에 대한 처리 -> 좌표를 *2하여 처리
"""
from collections import deque
def initBoard(board, rectangle):
    for rect in rectangle:
        LX, LY, RX, RY = map(lambda x: x*2, rect)
        for x in range(LX, RX+1):
            for y in range(LY, RY+1):
                if (x in [LX, RX] or y in [LY, RY]) and board[x][y]!=-1:
                    board[x][y]=1
                else:
                    board[x][y]=-1
def isMovable(board, nextNode):
    x, y = nextNode
    return board[x][y]==1
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]*102 for _ in range(102)]
    initBoard(board, rectangle) # 보드 초기화
    q = deque([(0, (characterX*2, characterY*2))])
    visited = set()
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        step, cur = q.popleft()
        if cur==(itemX*2, itemY*2):
            return step//2 # 좌표를 2배 했으므로 이동한 거리를 2로 나누어 반환
        for nextDir in direction:
            nextNode = tuple(map(sum, zip(cur, nextDir)))
            if isMovable(board, nextNode) and nextNode not in visited:
                q.append((step+1, nextNode))
                visited.add(nextNode)