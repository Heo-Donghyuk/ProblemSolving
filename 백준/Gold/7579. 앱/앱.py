n, m = map(int, input().split())
memory, costs = list(map(int, input().split())), list(map(int, input().split()))
max_cost = sum(costs)

# dp[i]: i 비용으로 얻을 수 있는 최대 메모리
dp = [0] * (max_cost + 1)

for mem, cost in zip(memory, costs):
    for c in range(max_cost, cost - 1, -1):
        dp[c] = max(dp[c], dp[c - cost] + mem)

answer = next(i for i in range(max_cost + 1) if dp[i] >= m)
print(answer)
