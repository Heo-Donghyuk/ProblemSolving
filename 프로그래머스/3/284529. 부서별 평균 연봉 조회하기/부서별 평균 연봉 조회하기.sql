/*
아이디어:
- 테이블 2개를 DEPT_ID로 join
- 이후 DEPT_ID로 GROUP BY
    - select 절에서 avg를 이용하여 평균연봉을 구하고
        - round로 첫째 자리에서 반올림
        - 컬럼명 변경 필요
- 조건에 맞게 정렬
조건:
- 부서별 평균 연봉을 조회
- 평균연봉은 소수점 첫째 자리에서 반올림
    - 컬럼명은 AVG_SAL
- 부서별 평균 연봉을 기준으로 내림차순 정렬
주의:
- left join 필요한지
- 중복제거 필요한지
- 서브쿼리 밖에서 조건 재확인 필요한지
*/
SELECT DEPT_ID, DEPT_NAME_EN, ROUND(AVG(SAL)) AS AVG_SAL
FROM HR_DEPARTMENT JOIN HR_EMPLOYEES USING(DEPT_ID)
GROUP BY DEPT_ID
ORDER BY AVG_SAL DESC