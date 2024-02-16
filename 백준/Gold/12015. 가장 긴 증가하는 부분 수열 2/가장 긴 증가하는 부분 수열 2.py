import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = []
for val in arr:
    if not stack or stack[-1]<val:
        stack.append(val)
    else:
        i = bisect_left(stack, val)
        stack[i]=val
print(len(stack))