/*
아이디어:
- where 절에서 수원의 레코드만 분리하고
- group by로 연도별로 그룹화 하자
- avg 집계함수로 미세먼지, 초미세먼지의 평균을 구하고
    - round로 두번째 자리에서 반올림하자
    - 컬럼명 커스텀하기
- 이후 연도 오름차순 정렬
조건:
- 수원 지역
- 연도 별 평균 미세먼지 오염도와 평균 초미세먼지 오염도를 조회
- 평균 미세먼지 오염도와 평균 초미세먼지 오염도의 컬럼명은 각각 PM10, PM2.5
- 값은 소수점 두 번째 자리에서 반올림
- 결과는 연도를 기준으로 오름차순 정렬
주의:
- left join 필요없는지
- 중복 제거 필요한지
- 서브쿼리 밖에서 조건 재확인 필요한지
*/
SELECT YEAR(YM) AS YEAR, ROUND(AVG(PM_VAL1), 2) AS 'PM10', ROUND(AVG(PM_VAL2), 2) AS 'PM2.5'
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR
ORDER BY YEAR