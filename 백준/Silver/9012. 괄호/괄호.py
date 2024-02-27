"""
유형: 스택
아이디어:
- 괄호의 짝 맞추기 -> 스택
주의:
- 시간복잡도: O(n)
- 예외:
    - 스택이 비어있을 경우
"""
for _ in range(int(input())):
    stack = []
    for char in input():
        if char=='(':
            stack.append(0)
        elif not stack:
            stack = [0]
            break
        else:
            stack.pop()
    print('NO' if stack else 'YES')