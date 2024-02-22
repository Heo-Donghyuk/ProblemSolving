"""
소요시간 : 
유형: BFS
아이디어: 6분
- BFS를 이용하여 최소 단계를 찾자
    - 한 단어에서 갈 수 있는 다른 단어들을 저장하는 딕셔너리를 만들자
        - 한 단어에서 다른 단어로 갈 수 있는지를 판단하는 함수를 만들어 이용하자
주의
- 시간복잡도
    - 딕셔너리 만들기 n^2
    - BFS N
- 조건
    - 변환할 수 없는 경우 0을 반환
- 예외
"""
from collections import defaultdict, deque

def isConvertable(begin, target):
    if len(begin)!=len(target):
        return False
    return True if sum(1 if a!=b else 0 for a, b in zip(begin, target))==1 else False

def solution(begin, target, words):
    # 딕셔너리 초기화
    convertDict = defaultdict(list)
    for start in words+[begin]:
        for end in words:
            if isConvertable(start, end):
                convertDict[start].append(end)
    # BFS
    q = deque([(0, begin)])
    visited = set()
    while q:
        step, curWord = q.popleft()
        if curWord==target:
            return step
        for nextWord in convertDict[curWord]:
            if nextWord not in visited:
                q.append((step+1, nextWord))
                visited.add(nextWord)
    return 0