"""
문제 유형: 그리디
아이디어 : 16분
최소한의 비용으로 이동을 완료해야 한다.
- 남은 주유소들 중 현재 리터당 비용이 가장 싸다면 
    남은 거리를 모두 갈 수 있는 기름을 구매해야 한다.
- 현재 주유소에서 주유해야 하는 양은 다음으로 나오는 자기보다 싼 주유소가 나올 때 까지
    갈 수 있는 양의 기름을 구매해야 한다.
- 그러면 자기보다 작은 주유소 까지 남은 거리를 어떻게 구할 수 있을까?
    - 순차 탐색 : n**2 -> 불가능(100억)
    - 스택을 이용 : N -> 가능(200만)
            - 스택을 이용하여 새로운 원소보다 큰 원소들을 모두 빼내자
            - 원소에는 스택에 들어간 시간과 리터당 가격을 튜플로 넣자
- 주의 마지막 주유소는 가격에 상관없이 모든 주유소당 가격보다 낮은 0과 같은 값을 사용하자
"""
n = int(input())
edge = list(map(int, input().split()))
vertex = list(map(int, input().split()))
time = [0]
for e in edge:
    time.append(time[-1]+e)
stack = []
remain = [0]*len(vertex)
for i, (v, t) in enumerate(zip(vertex, time)):
    while stack and stack[-1][1]>v:
        lastI, lastV, lastT = stack.pop()
        remain[lastI]=t-lastT
    stack.append([i, v, t])
while stack:
    lastI, lastV, lastT = stack.pop()
    remain[lastI]=t-lastT
answer = 0
fuel = 0
for e, v, r in zip([0]+edge, vertex, remain):
    fuel-=e
    if not fuel:
        fuel = r
        answer += fuel*v
print(answer)