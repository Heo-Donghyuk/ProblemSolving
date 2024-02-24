/*
아이디어:
- 프론트엔드, 파이썬, C#의 코드를 with 절로 따로 뺴자
- CASE 절로 각 개발자의 GRADE를 설정해 주자
- GRADE가 없는 레코드는 제외하자
조건:
- GRADE:
    A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
    B : C# 스킬을 가진 개발자
    C : 그 외의 Front End 개발자
- GRADE가 존재하는 개발자의
- GRADE, ID, EMAIL을 조회
- 결과는 GRADE와 ID를 기준으로 오름차순 정렬
주의:
- left join 필요한지
- 중복 제거 필요한지
- 서브쿼리 밖에서 다시 조건 판단 필요한지
- 출력 주의
- 날짜 범위 주의
*/

WITH FE AS (SELECT SUM(CODE) AS CODE
           FROM SKILLCODES
           WHERE CATEGORY='Front End'),
PYTHON AS (SELECT CODE
FROM SKILLCODES
WHERE NAME = 'Python'),
CSHARP AS (SELECT CODE
FROM SKILLCODES
WHERE NAME = 'C#')

SELECT (CASE
        WHEN (SELECT * FROM FE)&SKILL_CODE>0 AND 
            (SELECT * FROM PYTHON)&SKILL_CODE>0 THEN 'A'
        WHEN (SELECT * FROM CSHARP)&SKILL_CODE>0 THEN 'B'
        WHEN (SELECT * FROM FE)&SKILL_CODE>0 THEN 'C'
      END) AS GRADE, ID, EMAIL
FROM DEVELOPERS
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID
