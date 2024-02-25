"""
유형: 그리디
아이디어:
- 사람을 인출 시간이 적은 순서대로 정렬
- 이후 누적합을 구하고
- 누적합의 합을 반환
주의:
- 시간복잡도
- 예외
"""
n = int(input())
people = sorted(map(int, input().split()))
arr = [0]
for person in people:
    arr.append(arr[-1]+person)
print(sum(arr))