/*
아이디어:
- with 키워드로 2022년 점수가 가장 높은 사원들의 ID와 점수를 얻자
- 메인 쿼리에서 사원 테이블과 with 테이블을 join하여 ID가 존재하는 사원들만 남기고
    - 보여줄 컬럼만 보여주자
조건:
- 2022년도 
- 한해 평가 점수가 가장 높은 사원 정보를 조회
- 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회
- 2022년도의 평가 점수는 상,하반기 점수의 합을 의미
- 평가 점수를 나타내는 컬럼의 이름은 SCORE
주의:
- left join 필요없는지
- 중복제거 필요한지
- 서브쿼리 밖에서 조건 재확인 필요한지
*/
WITH SCORES_2022 AS (SELECT EMP_NO, SUM(SCORE) AS SCORE
            FROM HR_GRADE
            WHERE YEAR='2022'
            GROUP BY EMP_NO)
SELECT SCORE, EMP_NO, EMP_NAME, POSITION, EMAIL
FROM HR_EMPLOYEES JOIN SCORES_2022 USING(EMP_NO)
WHERE SCORE=(SELECT MAX(SCORE) FROM SCORES_2022)