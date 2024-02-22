"""
총 소요 시간 : 15분, 아이디어 7분 구현 8분
유형: 그리디
아이디어:
- 선형적으로 탐색하며 카메라가 꼭 있어야할 갯수를 파악해 보자
    - 시작 지점을 기준으로 정렬하여
        - 선형 탐색이 가능하도록 하자
- 가능한 카메라 범위와 경로가 겹친다면
    - 카메라 범위를 새롭게 할당한다.
- 가능한 카메라 범위를 넘는다면
    - 새 경로로 카메라 범위를 잡고 answer += 1
주의:
-시간복잡도
-조건
-예외
"""
def solution(routes):
    answer = 0
    camera = [-10**6, -10**6]
    for route in sorted(routes):
        left, right = route
        camLeft, camRight = camera
        if camRight<left: # 겹치지 않는 경우
            camera = [left, right]
            answer += 1
        else:
            camera = [left, min(right, camRight)]
    return answer