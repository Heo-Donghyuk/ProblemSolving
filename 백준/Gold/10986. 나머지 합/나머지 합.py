"""
유형: DP
아이디어:
- 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구해야 한다.
- 새로운 수가 들어왔을 때
    - 새로운 수가 포함되는 구간에서 M으로 나누어 떨어지는 구간의 수를 구하여 더하자
        -> 이렇게 하면 N^2
    - 연속 부분 구간 합의 나머지를 저장하는 DP 테이블을 만들자
        - 해당 DP 테이블에서 현재 숫자를 더해 나머지가 0이될 수 있는 부분 구간의 개수를 answer에 더하자
        - DP를 갱신하자
            - 나눠야 하는 숫자가 5고
                - 현재 숫자가 3일 때
                    - 나머지가 2인 연속 수열이 1개라면 answer+=1을 해주자
                    - 그리고 나머지가 2인 연속 수열의 개수는 
                        - 다음 회차에서 나머지가 0인 연속 수열이 된다.
                    - 나머지가 3인 연속 수열의 개수는
                        - 다음 회차에서 나머지가 1
                    - 나머지가 0 -> 나머지가 3
                    -> 프리셋을 두어 인덱스를 찾을 수 있도록 하자
주의:
-시간복잡도: O(NM)
-예외
"""
import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
DP = deque([0]*m)
answer, preset = 0, 0
for num in map(int, input().split()):
    answer+=DP[-num%m]
    answer+= 0 if num%m else 1
    DP.rotate(num%m)
    DP[num%m]+=1
print(answer)