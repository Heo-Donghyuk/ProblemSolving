"""
유형: 스택
아이디어:
- 스택을 이용하여 새로 들어오는 원소가 스택의 마지막 원소 보다 크거나 같을 떄 까지 pop하며
    - pop되는 원소의 가격이 떨어지기 까지의 시간을 구하자
"""
def solution(prices):
    stack = []
    answer = [0]*(len(prices)+1)
    for i, price in enumerate(prices, start=1):
        while stack and stack[-1][1] > price:
            time, p = stack.pop()
            answer[time]=i-time
        stack.append((i, price))
    while stack:
        time, p = stack.pop()
        answer[time]=i-time
    return answer[1:]