def solution(game_board, table):
    def DFS(cur, visited, target, board):
        visited.append(cur)
        curX, curY = cur
        board[curX][curY] = 0 if target else 1
        n = len(board)
        for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            i, j = map(sum, zip(cur, d))
            nextPos = (i, j)
            if 0<=i<n and 0<=j<n and board[i][j]==target:
                DFS(nextPos, visited, target, board)
        minX, minY = min(visited)    
        return sorted([(i-minX, j-minY) for i, j in visited])
    
    def rotate(table):
        return [list(l) for l in zip(*table[::-1])]
    # 테이블을 회전시키며 조각들을 생성
    pieces = []
    t1 = table
    t2 = rotate(t1)
    t3 = rotate(t2)
    t4 = rotate(t3)
    rotatedTable = [t1, t2, t3, t4]
    # 각 테이블을 순회하며 조각들을 생성
    n, m = len(table), len(table[0])
    def rotatedCoord(coord, n, time):
        x, y = coord
        for _ in range(time):
            x, y = y, n-x-1
        return (x, y)
    for x in range(n):
        for y in range(m):
            if table[x][y]:
                cur, res = (x, y), []
                for i, t in enumerate(rotatedTable):
                    res.append(DFS(rotatedCoord(cur, n, i), [], 1, t))
                pieces.append(res)
    # 보드를 순회하며 조각들을 생성
    answerPieces =  []
    for x in range(len(game_board)):
        for y in range(len(game_board[0])):
            if game_board[x][y]==0:
                answerPieces.append(DFS((x, y), [], 0, game_board))
    # 조각을 순회하며 정답 조각과 비교
    answer = 0
    for piece in pieces:
        for p in piece:
            if p in answerPieces:
                answer+=len(p)
                answerPieces.remove(p)
                break
    return answer