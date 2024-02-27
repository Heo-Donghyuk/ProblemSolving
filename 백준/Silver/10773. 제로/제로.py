"""
유형: 스택
아이디어:
- 스택을 이용한 풀이
주의:
- 시간복잡도: O(n)
- 예외: 스택이 비었을 경우에 pop -> 문제에서 정수가 0일 경우에 지울 수 있는 수가 있음을 보장
"""
import sys
input = sys.stdin.readline
stack = []
for _ in range(int(input())):
    val = int(input())
    if val: #push
        stack.append(val)
    else: #pop
        stack.pop()
print(sum(stack))