"""
유형:DP
아이디어:
- 길이가 3인 배열에 새로운 수를 하나 추가했다고 하자
    - 이때 연속합 중 최댓값은
        - 기존의 최댓값 그대로이거나
        - 새로운 수를 포함하는 연속합의 최댓값
        - 이 둘 중 하나일 것이다.
- 새로운 수를 포함하는 연속합의 최댓값은
    - 새로운 수가 추가되기 전의 최댓값 + 새로운 수
        => 맞나? -> 새로운 수가 추가되기 전의 최댓값이 0보다 작다면
                새로운 수가 새로운 lastMaxSum이 될 것이다.
    - 이렇게 생성된 최댓값을 answer와 비교하여 더 큰 값을 answer로 저장하자
- answer와 lastMaxSum 변수를 두자
- 값을 하나씩 추가하며
    - lastMaxSum에 새로운 수를 더해 lastMaxSum을 갱신하자
        - lastMaxSum이 음수인 경우에 대한 처리가 필요하다.
    - 갱신된 lastMaxSum과 answer의 값을 비교하여 더 큰 값을 answer로 갱신하자
주의:
- 시간복잡도: O(n)
- 예외: 음수가 되는 경우
"""
n = int(input())
answer, lastMaxSum = -10**9, -10**9
for num in map(int, input().split()):
    lastMaxSum = max(lastMaxSum+num, num)
    answer = max(answer, lastMaxSum)
print(answer)