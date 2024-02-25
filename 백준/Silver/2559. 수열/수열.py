n, k = map(int, input().split())
temps = list(map(int, input().split()))
answer = sum(temps[:k])
cur = answer
for i in range(k, len(temps)):
    cur += temps[i]-temps[i-k]
    answer = max(answer, cur)
print(answer)