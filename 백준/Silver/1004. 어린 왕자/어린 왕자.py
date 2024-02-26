import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    start, end = [], []
    for __ in range(int(input())):
        cx, cy, r = map(int, input().split())
        r1Square = (cx-x1)**2+(cy-y1)**2
        r2Square = (cx-x2)**2+(cy-y2)**2
        if r1Square<r**2:
            start.append((cx, cy, r))
        if r2Square<r**2:
            end.append((cx, cy, r))
    print(len(set(start+end))*2-len(start)-len(end))