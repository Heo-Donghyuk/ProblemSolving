"""
유형: 구현
아이디어:
- upper로 모두 대문자 변환
- Counter로 각 알파벳의 수 세기
- max로 가장 많이 사용된 횟수를 획득
- 카운터에서 횟수가 max인 원소들을 얻고
    - 그 원소의 수가 하나면 이를 출력
    - 둘 이상이면 ?를 출력
주의:
- 시간복잡도: O(n)
- 예외
"""
from collections import Counter
count = Counter(input().upper())
maxNum = max(count.values())
arr = [key for key, val in count.items() if val==maxNum]
print(arr[0] if len(arr)==1 else "?")