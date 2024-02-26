"""
유형:
아이디어:
- 가장 긴 증가하는 부분 수열로 문제를 나눌 수 없을까?
- i인덱스를 기준으로 좌측은 증가하는 수열 우측은 감소하는 수열
- i인덱스를 기준으로
    - i를 증가시키며 해당 인덱스 까지의 최장 증가 부분수열의 길이를 저장하자
    - 이떄 시간 복잡도는 nlogn(이진 탐색 사용 시)
- 이후 배열을 뒤집어
    - 해당 인덱스에 대해 최장 증가 부분수열의 길이를 구하여
        - 감소하는 부분수열의 최대 길이를 저장하자
- 인덱스를 기준으로 증가, 감소하는 부분수열의 길이를 구하여
    - 이 중 최댓값을 반환하자
주의:
- 시간복잡도
- 예외
"""
from bisect import *
n = int(input())
arr = list(map(int, input().split()))
ASCDP, DESCDP = [], []
# 증가하는 부분 수열
stack = []
for i, num in enumerate(arr): 
    if not stack or stack[-1]<num:
        stack.append(num)
    else:
        stack[bisect_left(stack, num)]=num
    ASCDP.append(len(stack))
# 감소하는 부분 수열
stack = []
for i, num in enumerate(arr[::-1]): 
    if not stack or stack[-1]<num:
        stack.append(num)
    else:
        stack[bisect_left(stack, num)]=num
    DESCDP.append(len(stack))
# 바이토닉 부분 수열
print(max(map(sum, zip(ASCDP, DESCDP[::-1]))) - 1) # 기준이 되는 인덱스의 수가 중복포함되므로 1을 빼준다