/*
아이디어:
- 해당 기간동안 대여 가능한 차량을 with절로 분리하자
- 트럭, 세단의 30일 할인률을 저장하는 테이블을 with절 또는 변수로 만들자
    - with절로 만들어서 join하자
        - 자연스럽게 트럭, 세단만 남게 된다
- 이후 메인 쿼리에서
    - where in으로 대여 가능한 차량만 남기자
    - select절에서 fee를 구하고
    - having절에서 fee가 50만 이상 200만 미만!!!!인 레코드만 남기자
    - 이후 정렬
조건:
- 자동차 종류가 '세단' 또는 'SUV' 
- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해
- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력
- 결과는 대여 금액을 기준으로 내림차순 정렬
    - 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 
    - 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬
주의:
- left join 필요한지
- 중복 제거 필요한지
- 
*/
WITH ISNOTVALID AS (SELECT CAR_ID
                FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                WHERE NOT(START_DATE>'2022-11-30' OR END_DATE<'2022-11-01')),
    DC_RATE AS (SELECT CAR_TYPE, DISCOUNT_RATE
               FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
               WHERE CAR_TYPE IN ('세단', 'SUV') AND DURATION_TYPE LIKE '30%')
SELECT CAR_ID, CAR_TYPE, FLOOR(DAILY_FEE * 30 * (100-DISCOUNT_RATE) / 100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR JOIN DC_RATE USING(CAR_TYPE)
WHERE CAR_ID NOT IN (SELECT * FROM ISNOTVALID)
HAVING FEE >=500000 AND FEE < 2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC