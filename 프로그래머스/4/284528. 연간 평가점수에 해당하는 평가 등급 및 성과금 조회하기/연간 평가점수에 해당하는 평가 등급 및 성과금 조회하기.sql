/*
아이디어:
- with절에서 각 사원들의 grade를 만들어 내자
- 메인 쿼리에서 사원 정보와 grade 테이블을 join하자
    - select 절에서 case문으로 보너스 컬럼을 만들자
조건:
- 사원별 성과금 정보를 조회
    - 사번, 성명, 평가 등급, 성과금을 조회
- grade는 1분기 2분기 점수의 평균을 이용하여 매기는 것 같다.
- 결과 사번 오름차순
주의:
- left join 필요없는지
- 중복제거 필요한지
- 서브쿼리 밖에서 조건 재확인 필요한지
*/
WITH BONUS_GRADE AS (SELECT EMP_NO, (CASE
                                        WHEN AVG(SCORE)>=96 THEN 'S'
                                        WHEN AVG(SCORE)>=90 THEN 'A'
                                        WHEN AVG(SCORE)>=80 THEN 'B'
                                        WHEN AVG(SCORE)<80 THEN 'C'
                                    END) AS GRADE
                    FROM HR_GRADE
                    GROUP BY EMP_NO)
SELECT EMP_NO, EMP_NAME, GRADE, (CASE
                                    WHEN GRADE='S' THEN 0.2
                                    WHEN GRADE='A' THEN 0.15
                                    WHEN GRADE='B' THEN 0.1
                                    WHEN GRADE='C' THEN 0
                                END)*SAL AS BONUS
FROM HR_EMPLOYEES JOIN BONUS_GRADE USING(EMP_NO)
ORDER BY EMP_NO