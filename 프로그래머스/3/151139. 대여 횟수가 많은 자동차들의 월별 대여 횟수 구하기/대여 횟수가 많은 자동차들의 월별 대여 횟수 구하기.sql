/*
아이디어:
- where 절에서 
    - 서브쿼리를 이용하여 대여 시작일이 22 08, 22 10 사이이고 총 대여 횟수가 5회 이상인 ID만 남기자
    - 이후 id가 서브쿼리에 포함되는 레코드만 남기자
- 이후 group by month, car id로 그룹화
    - count(*)로 원소의 개수를 세자 (RECORDS)
조건:
- 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력
- 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬
- 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외
주의:
*/
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN (SELECT CAR_ID
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                WHERE START_DATE LIKE '2022-08%' OR
                 START_DATE LIKE'2022-09%' OR
                START_DATE LIKE '2022-10%'
                GROUP BY CAR_ID
                HAVING COUNT(*)>=5) AND
                (START_DATE LIKE '2022-08%' OR
                 START_DATE LIKE'2022-09%' OR
                START_DATE LIKE '2022-10%')
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC