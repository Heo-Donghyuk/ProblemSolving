/*
아이디어:
- where 절에서 세단, suv를 선택
- where 절에서 서브쿼리로 해당 기간동안 대여가 불가능한 자동차의 아이디를 얻자
    - not in 으로 대여 가능한 자동차를 선택하자
- duration_type이 30일 이상인 plan 테이블과 car type으로 join하자
- 그리고 30일 간의 대여금액을 구한 fee 컬럼을 만들고
- having절에서 fee가 50만 이상 200만 미만!인 자동차를 선택하자
- 이후 정렬
조건:
- 자동차 종류가 '세단' 또는 'SUV' 인 자동차
- 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차
- 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력
- 대여 금액을 기준으로 내림차순 정렬하고, 
    대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 
    자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬
주의:
- 서브쿼리 밖에서 조건을 추가로 지정할 필요가 있는지
- left join이 필요한지
- 중복 제거가 필요한지
*/
# WITH NOT_AVAILABLE AS (SELECT CAR_ID
#                       FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#                       WHERE (START_DATE NOT BETWEEN '2022-11-01' AND '2022-11-30 24:00:00') AND
#                             (END_DATE NOT BETWEEN '2022-11-01' AND '2022-11-30 24:00:00'))
SELECT CAR_ID, CAR_TYPE, FLOOR(DAILY_FEE*30*(100-DISCOUNT_RATE)/100) AS FEE
FROM CAR_RENTAL_COMPANY_CAR JOIN (SELECT * 
                                  FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
                                 WHERE DURATION_TYPE LIKE '30%') PLAN USING(CAR_TYPE)
WHERE CAR_TYPE IN ('세단', 'SUV') AND 
        CAR_ID NOT IN (SELECT CAR_ID
                      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                      WHERE NOT ((START_DATE > '2022-11-30') OR
                            (END_DATE < '2022-11-01')))
HAVING FEE>=500000 AND FEE<2000000
ORDER BY FEE DESC, CAR_TYPE, CAR_ID DESC