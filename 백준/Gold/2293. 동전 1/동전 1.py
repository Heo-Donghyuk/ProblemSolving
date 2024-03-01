import sys
input = sys.stdin.readline
n, k = map(int, input().split())
DP = [1]+[0]*k
for _ in range(n):
    coin = int(input())
    for i in range(coin, k+1):
        DP[i]+=DP[i-coin]
print(DP[-1])
        