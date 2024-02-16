"""
시간 복잡도 : 10000*100000 -> 안될 것 같음 다른 방법이 필요
스택을 이용할 수 있지 않을까?
새로운 원소를 넣기 전 자기보다 큰 원소들은 빼자 그리고 빠진 녀석들은 정답 리스트에 값을 할당해 주자
스택에 원소를 넣자 원소를 넣을 때 자신의 인덱스와 값을 넣자
원소를 넣기 전에 자기보다 큰 가격을 가지는 원소들을 모두 빼자
그리고 그 원소들을 현재 인덱스와 빠진 인덱스를 비교하여 정답 리스트에 값을 할당하자
"""
def solution(prices):
    stack = []
    answer = [0]*len(prices)
    for i, p in enumerate(prices):
        while stack and stack[-1][1]>p:
            popI, popP = stack.pop()
            answer[popI] = i-popI
        stack.append((i, p))
    while stack:
        popI, popP = stack.pop()
        answer[popI] = i-popI
    return answer