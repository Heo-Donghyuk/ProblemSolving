from itertools import combinations_with_replacement as H
n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
for h in H(nums, m):
    print(' '.join(map(str, h)))
