"""
유형: DP
아이디어:
- 각 행에 대한 누적합을 저장하는 리스트를 만들자
- (x1, y1)부터 (x2, y2)까지의 누적합을 구해야한다
    - 누적합을 각 행에 대한 누적합으로 분리하자
    - x1에서 x2의 행에서
    - y1부터 y2까지의 누적합을 구하면 그것이 정답
주의:
- 시간복잡도
- 예외
    - 인덱스 범위 주의
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write
read = lambda: input().split()

n, m = map(int, read())
dictionary = {0:[0]*(n+1)}

for row in range(1, n+1):
    temp = [0]
    dictionary[row] = [0]
    for i, num in enumerate(map(int, read()), start=1):
        lastSum = temp[-1]
        lastColSum = dictionary[row-1][i]
        temp.append(lastSum+num)
        dictionary[row].append(lastSum+lastColSum+num)
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, read())
    res = dictionary[x2][y2]-dictionary[x1-1][y2]-dictionary[x2][y1-1]+dictionary[x1-1][y1-1]
    print(str(res)+'\n')