"""
유형: 재귀, 스택
아이디어:
- 재귀적으로 문자열을 디코딩하는 함수를 만들자
- 괄호를 만나면 괄호 내부의 압축된 문자열을 받아 재귀적으로 호출하자
- 괄호가 언제 끝나는지에 대한 판단은 스택을 이용하자
    - 값이 필요한 것이 아니기 때문에 스택이 아닌 수를 이용하자
주의:
-시간복잡도
-예외
"""
def decode(string):
    answer = 0
    lastchar = ''
    i = 0
    while i<len(string):
        if string[i]!='(':
            answer+=1
            lastChar = string[i]
            i+=1
        else:
            n = int(lastChar)
            answer-=1
            i+=1
            stack, count = [], 1
            while count:
                stack.append(string[i])
                if string[i]=='(':
                    count+=1
                elif string[i]==')':
                    count-=1
                i+=1
            stack.pop()
            answer+=n*decode(stack)
    return answer

print(decode(input()))