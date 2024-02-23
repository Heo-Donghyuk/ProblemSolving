/*
아이디어:
- with절로 carId와 대여기간 컬럼을 가지는 테이블을 만들자
    - 이떄 datediff + 1을 해줘야 함에 주의
- 이후 group by carid로 그룹화 후 avg와 round를 이용하여 평균을 소수점 둘째자리에서 반올림하자
조건:
- 평균 대여 기간이 7일 이상인 자동차
- 자동차 ID와 평균 대여 기간(컬럼명: AVERAGE_DURATION) 리스트를 출력
- 평균 대여 기간은 소수점 두번째 자리에서 반올림
- 결과는 평균 대여 기간을 기준으로 내림차순 정렬해주시고, 
    평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순 정렬
주의:
- left join 필요 없는지
- 중복 제거가 필요한지
- 서브쿼리 밖에서 다시 조건을 확인 할 필요가 있는지
*/
WITH RENTAL_DUE AS (SELECT CAR_ID, DATEDIFF(END_DATE, START_DATE) + 1 AS DUE
                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY)
SELECT CAR_ID, ROUND(AVG(DUE), 1) AS AVERAGE_DURATION
FROM RENTAL_DUE
GROUP BY CAR_ID
HAVING AVERAGE_DURATION>=7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC