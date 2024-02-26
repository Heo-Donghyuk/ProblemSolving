import sys
input = sys.stdin.readline
n = int(input())
DP = [[0]*3 for _ in range(3)]
lastNum = 0
for _ in range(n):
    num = int(input())
    DP = DP[1:]+[[max(DP[-1]), max(DP[-2])+num, max(DP[-3])+num+lastNum]]
    lastNum = num
print(max(DP[-1]))