"""
문제 유형: 해시, 수학
아이디어:
- 가지고 있는 옷을 분류에 따라 딕셔너리에 집어 넣자
- 그러면 분류에 따라 각각 
    - 1 3 2 와 같은 가진 갯수가 나올 것이다.
    - combinations로 종류를 1개 선택, 2개 선택 ... n개 선택 하는 각각의 경우에 대한 경우의 수를 구하자
        - 그리고 이를 answer에 더하며 정답을 구하자
시간 복잡도:
- 가진 의상의 수가 30개 이하 -> 종류는 언급 x -> 종류도 최대 30개? 아니면 예시처럼 4개? 모르겠다.
- 30종이면 불가. -> 다른 아이디어 필요
새로운 아이디어 :
- 안입은 경우까지 포함한 모든 경우의 수를 구하고
    - 안입은 경우(-1)를 빼주자
"""
def solution(clothes):
    dic = dict()
    for name, category in clothes:
        if category not in dic:
            dic[category] = 1
        else:
            dic[category] +=1
    answer = 1
    for count in dic.values():
        answer *= count+1
    return answer -1