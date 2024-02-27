import sys
input = sys.stdin.readline
from collections import Counter
c = Counter(int(input()) for _ in range(int(input())))
for key in sorted(c.keys()):
    for _ in range(c[key]):
        print(key)