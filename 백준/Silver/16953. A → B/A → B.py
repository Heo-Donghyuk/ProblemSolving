from collections import deque
a, b = map(int, input().split())
q = deque([(1, b)])
while q:
    step, val = q.popleft()
    if val==a:
        break
    if val%10==1 and val//10>=a:
        q.append((step+1, val//10))
    if val%2==0 and val//2>=a:
        q.append((step+1, val//2))
print(-1 if val!=a else step)