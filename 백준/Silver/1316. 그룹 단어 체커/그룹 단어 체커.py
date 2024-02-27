"""
유형:
아이디어:
주의:
-시간복잡도
-예외
"""
import sys
input = sys.stdin.readline

def isGroup(string):
    visited = set(string[0])
    for i, char in enumerate(string[1:]):
        if char not in visited:
            visited.add(char)
        elif string[i]!=char:
                return False
    return True

answer = 0
for _ in range(int(input())):
    answer += isGroup(input())
print(answer)