n, m = map(int, input().split())
memories, costs = list(map(int, input().split())), list(map(int, input().split()))
DP = [0]*(sum(costs)+1)
for mem, cost in zip(memories, costs):
    for i in range(len(DP)-1, cost-1, -1):
        DP[i] = max(DP[i], DP[i-cost]+mem)
for i, mem in enumerate(DP):
    if mem>=m:
        print(i)
        break