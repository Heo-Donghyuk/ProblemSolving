"""
유형:
아이디어:
1. 번호의 범위가 작은 순서대로 정렬하여 작은 원소부터 하나씩 제거하며 책을 나눠준다.
    - 범위가 같은 경우 앞 번호가 작은 순서대로 책을 나눠준다.
    -> 확실한 로직인가? 예외는 없는가?
        1 1 2 2 3 3 2 3
        11 22 12 23 => 예외를 찾기 힘들다. 확실한 로직인지 잘 모르겠다. 일단 구현
        => 틀렸다. 12 23 34 13의 경우 정답은 4이지만 내 로직으로는 3
2. 끝나는 수를 기준으로 정렬하기
    - 끝나는 수가 같다면 시작하는 수를 기준으로 정렬하기
주의:
-시간복잡도: O(n^2)
-예외
"""
import sys
input = sys.stdin.readline

def find(a, b, visited):
    for i in range(a, b+1):
        if visited[i]==False:
            return i
    return None

for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = 0
    visited = [False]*(n+1)
    people = [tuple(map(int, input().split())) for __ in range(m)]
    people.sort(key=lambda x: (x[1], -x[0]))
    for a, b in people:
        idx = find(a, b, visited)
        if idx:
            visited[idx]=True
            answer += 1
    print(answer)