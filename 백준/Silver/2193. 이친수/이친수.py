n = int(input())
DP = [0, [0, 1]]
for i in range(n-1):
    DP.append([sum(DP[-1]), DP[-1][0]])
print(sum(DP[-1]))