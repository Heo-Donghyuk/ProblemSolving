/*
# help 'log'
# select log(2, 16)
# help 'bin'
skillcodes에서 python, c#의 코드를 얻고 log를 취해 인덱스를 얻자(뒤에서 부터, 시작은 1이므로 +1을 한다)
이후 developers에서 각 레코드에 대해
    where문으로 skillcode를 bin으로 이진 변환 후 뒤에서 python, c#인덱스 번째의 비트가 1이면 포함하도록 하자
    주의! : bin으로 변환한 길이가 python c#의 인덱스를 넘었을 경우에 대한 예외 처리가 필요하다
이후 결과를 ID 오름차순 정렬하자
*/
# SET @pythonIdx = (SELECT LOG(2, CODE)
#                     FROM SKILLCODES
#                     WHERE NAME='Python')

# SET @CSharpIdx = (SELECT LOG(2, CODE)
#                     FROM SKILLCODES
#                     WHERE NAME='C#')
                    
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SUBSTR(BIN(SKILL_CODE), 
             -(SELECT LOG(2, CODE)
               FROM SKILLCODES
               WHERE NAME='Python')-1, 1)='1' OR
      SUBSTR(BIN(SKILL_CODE), 
             -(SELECT LOG(2, CODE)
               FROM SKILLCODES
               WHERE NAME='C#')-1, 1)='1'
ORDER BY ID