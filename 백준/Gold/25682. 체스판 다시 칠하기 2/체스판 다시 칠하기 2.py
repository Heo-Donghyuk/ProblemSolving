"""
유형:
아이디어:
- 누적합으로 풀 수 있을 것 같은데?
- (0, 0)에서 특정 좌표까지 다시 칠해야 하는 칸의 수를 누적합으로 구하자
    - x, y좌표의 합이 홀, 짝인 지에 따라 w, b를 선택하고 해당 칸이 선택된 색이 맞는지 확인하자
    - 그리고 (0,0)~(x-1,y), (0,0)~(x,y-1)까지의 누적합을 빼주고
        - 중복된 (0,0)~(x-1,y-1)까지의 누적합을 더한 후 새로운 칸의 wb여부를 더하여 새로운 누적합을 만들어주자
- 이후 k의 범위를 갖는 칸의 누적합을 탐색하며 판단하고 가장 적은 값을 갱신하며 저장하자
    - 이때의 값은 max(누적합, k^2-누적합)를 이용하자
주의:
-시간복잡도: O(n^2)
-예외:
    - 인덱스 주의
"""
import sys
input = sys.stdin.readline

def getSum(coord1, coord2, board):
    x1, y1 = coord1
    x2, y2 = coord2
    return board[x2][y2]-board[x1-1][y2]-board[x2][y1-1]+board[x1-1][y1-1]

n, m, k = map(int, input().split())
board = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j, val in enumerate(input().strip(), start=1): #strip 필요 없는지 확인
        board[i][j]=getSum((1, 1), (i-1, j), board)+getSum((1, 1), (i, j-1), board)-getSum((1, 1), (i-1, j-1), board)+(1 if val==('W' if (i+j)%2 else 'B') else 0)
answer = n*m
for i in range(k, n+1):
    for j in range(k, m+1):
        s = getSum((i-k+1, j-k+1), (i, j), board)
        s = min(s, k**2-s)
        answer = min(answer, s)
print(answer)