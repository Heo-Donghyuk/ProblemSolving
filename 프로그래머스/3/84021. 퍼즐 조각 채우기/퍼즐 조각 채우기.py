"""
유형: DFS
아이디어: 11분
- 조각의 정보를 DFS로 생성 -> 회전한 조각도 생성해야 한다
    - 회전한 조각을 어떻게 생성할까?
    - 조각 자체를 회전 시키기
        - DFS로 조각을 찾고
        - 해당 조각 정보를 회전시켜서 회전한 조각 정보를 얻자
            - 단 회전한 결과가 보드에서의 조각과 일치할 수 있도록 로직이 정확해야 한다!!!!
                - 조각에 포함된 좌표들을 회전 후 정렬하여 이용하자
    - 회전한 테이블에서 조각을 찾기
- 생성한 조각이 Game_board의 빈 칸에 딱 맞는 경우가 있다면 정답을 증가시키자.

주의:
- 시간 복잡도
- 조건:
    - 인접한 칸이 비어있으면 안된다 -> 딱 맞게 채워 넣어야 한다.
- 예외:
    - 같은 모양의 조각이 여러개 일 수 있다.
    - 보드를 벗어난 인덱스에 접근하지 않도록 하자
    - 같은 조각인지를 판단할 수 있는 기준을 정해야 한다.
        - 조각에 포함된 좌표들을 정렬하고, 가장 작은 값을 가지는 좌표를 0, 0으로 하도록 조각을 만들어야 한다.
"""
def rotateCoord(coord, boardLen):
    # 좌표를 90도 회전한 결과를 반환
    x, y = coord
    # 1, 2 => 2, -1 -1
    newX, newY = y, boardLen-x-1
    return (newX, newY)
def convertPiece(piece):
    newPiece = sorted(piece)
    minCoord = min(newPiece)
    newPiece = [(x-minCoord[0], y-minCoord[1]) for x, y in newPiece]
    return newPiece

def isMovable(board, coord, target):
    # 다음 위치로 이동 가능 여부를 판단, 보드는 0일 때 이동 가능, table은 1일 때 이동 가능
        # 범위를 벗어난 인덱스를 참조하지 않도록 주의
    x, y = coord
    n = len(board)
    if 0<=x<n and 0<=y<n and board[x][y]==target:
        return True
    
def DFS(board, coord, target):
    # 재귀적으로 이동 가능한 좌표들을 탐색하자
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = coord
    board[x][y] = 0 if target else 1
    res = [coord]
    for nextAdd in directions:
        nextCoord = tuple(map(sum, zip(nextAdd, coord)))
        if isMovable(board, nextCoord, target):
            res+=DFS(board, nextCoord, target)
    return res
    
def solution(game_board, table):
    answerPiece = []
    for x in range(len(game_board)):
        for y in range(len(game_board)):
            if game_board[x][y]==0:
                piece = DFS(game_board, (x, y), 0)
                answerPiece.append(tuple(convertPiece(piece)))
    tablePiece = []
    for x in range(len(table)):
        for y in range(len(table)):
            if table[x][y]==1:
                res = []
                piece = DFS(table, (x, y), 1)
                for _ in range(4):
                    piece = [rotateCoord(coord, len(table)) for coord in piece]
                    res.append(tuple(convertPiece(piece)))
                tablePiece.append(res)
    
    answer = 0
    while tablePiece and answerPiece:
        piece = tablePiece.pop()
        for i, ansPiece in enumerate(answerPiece):
            if any(p==ansPiece for p in piece):
                answer += len(ansPiece)
                answerPiece.pop(i)
                break
    return answer
                    
    