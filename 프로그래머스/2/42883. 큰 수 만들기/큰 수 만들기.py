"""
유형 : 그리디
아이디어:
- 어떤 수를 우선적으로 없애야 할까?
    - 1924 -> 924 -> 94
    - 4177252841 -> 477252841 -> 77252841 -> 7752841 -> 775841
    => 다음 수가 현재 수 보다 크면 현재 수를 삭제
        -> 삭제 후 인덱스는 현재 인덱스 -1 에서 다시 시작
     -> 수의 끝에 도달할 때 까지 그러한 수가 없다면 마지막 수를 삭제
주의:
-시간복잡도: O(n)
-조건:
    - 문자열 형태의 수
-예외:
    - 인덱스 처리 주의
"""
def solution(number, k):
    stack = []
    count=0
    for char in number:
        while stack and stack[-1]<char:
            if count>=k:
                break
            stack.pop()
            count+=1
        stack.append(char)
    
    return ''.join(stack[:-(k-count)] if k!=count else stack)