/*
아이디어:
- 값이 없는 컬럼도 만들어 줘야 한다.
    - 어떻게 만들지? rownum over?
        => 겨우겨우 recursive cte로 만들었다.
- 시간별로 group by 후 count하고 이를 재귀 cte와 union하자
    - 이후 hour 별로 group by 후 count는 최댓값을 출력하자
조건:
주의:
- 서브쿼리의 조건으로 충분한지 확인
- 중복 제거 로직이 필요한지 확인
*/

WITH RECURSIVE T AS (SELECT 0 AS NUM, 0 AS COUNT
                     UNION SELECT NUM+1, COUNT FROM T WHERE NUM<23)
SELECT HOUR, MAX(COUNT) AS COUNT
FROM (SELECT HOUR(DATETIME) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
UNION SELECT * FROM T) AS UNION_T
GROUP BY HOUR
ORDER BY HOUR

