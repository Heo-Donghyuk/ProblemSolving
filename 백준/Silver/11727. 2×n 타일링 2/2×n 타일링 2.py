# DP[i] = DP[i-1]+2*DP[i-2]
n = int(input())
DP = [0, 1, 1]
for _ in range(n-1):
    DP = DP[1:]+[(DP[2]+2*DP[1])%10007]
print(DP[-1])