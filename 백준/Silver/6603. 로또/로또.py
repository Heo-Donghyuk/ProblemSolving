"""
유형: 조합
아이디어:
- combinations를 이용하자
- 입력이 정렬되지 않았을 수 있으니 정렬하자
주의:
-시간복잡도
-예외
"""
from itertools import combinations
while True:
    arr = list(input().split())
    if len(arr)==1:
        break
    n, arr = arr[0], sorted(arr[1:], key=int)
    for c in combinations(arr, 6):
        print(' '.join(c))
    print()