"""
유형: 구현?
아이디어:
- 문제에 제시된 대로 나이브하게 구현하여
    - 모든 경우에 대해 탐색하기
- permutations를 이용하여 열어볼 상자 2개를 선택하자
    - 선택한 상자에 대해 문제의 조건에 맞게 상자를 열어보자
        - 상자를 여는 로직을 수행하는 함수를 만들자
        - 첫 번째 상자와 두 번쨰 상자가 공유하는 visited set이 필요하다
주의:
-시간복잡도: O(n^3) - 2개의 그룹을 고르는 방법 (n**2) * 고른 그룹에서 상자를 열어가기 (n)
-예외
    - 첫 번째로 고른 상자에서 모든 상자를 다 열어볼 수 있다.
        - 이때에 대한 처리가 필요하다.
    - permutations는 남은 상자 중 하나를 선택하지 않는다.
        - 그래서 시간 복잡도 면에서 좋지 않을 수 있다
"""
from itertools import permutations
def openBox(box, cards, visited):
    if box in visited:
        return 0
    visited.add(box)
    nextBox = cards[box]
    return 1 + openBox(nextBox, cards, visited)

def solution(cards):
    cards = [0]+cards
    answer = 0
    for box1, box2 in permutations(cards[1:], 2):
        visited = set()
        openNum1 = openBox(box1, cards, visited)
        openNum2 = openBox(box2, cards, visited)
        answer = max(answer, openNum1*openNum2)
    return answer