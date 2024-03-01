/*
아이디어:
- with절로 2022 8~10까지의 레코드만 남기자
- 메인 쿼리에서 with절 테이블을 불러오고
    - where 절에서 서브쿼리로 총 대여 횟수가 5회 이상인 레코드만 남기자
    - 이후 group by month, carId를 하고
        - selct 절에서 month, car_id, records를 만들어주자
조건:
- 대여 시작일을 기준
- 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들
- 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: RECORDS) 리스트를 출력
- 결과는 월을 기준으로 오름차순 정렬
    - 월이 같다면 자동차 ID를 기준으로 내림차순 정렬
    - 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외
주의:
- left join 필요한지
- 중복제거 필요한지
- where 절 밖에서 조건 재확인 필요한지
*/
WITH REC8TO10 AS (SELECT *
                 FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 WHERE START_DATE BETWEEN '2022-08-00' AND '2022-11-00')
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(CAR_ID) AS RECORDS
FROM REC8TO10
WHERE CAR_ID IN (SELECT CAR_ID
                FROM REC8TO10
                GROUP BY CAR_ID
                HAVING COUNT(CAR_ID)>=5)
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC