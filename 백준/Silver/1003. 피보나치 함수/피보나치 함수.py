DP = [[1, 0], [0, 1]]
for i in range(2, 41):
    DP.append([DP[i-1][0]+DP[i-2][0], DP[i-1][1]+DP[i-2][1]])
for _ in range(int(input())):
    n = int(input())
    print(DP[n][0], DP[n][1])
    
