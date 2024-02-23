/*
아이디어:
- 서브쿼리로 조건을 만족하는 레코드의 분류와 가격을 선택하고
    - 분류와 가격이 서브쿼리에 포함되는 레코드만 선택하자
조건:
- 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
- 결과는 식품 가격을 기준으로 내림차순 정렬
주의:
- 분류와 최대 가격이 동시에 일치해야 한다
- 분류는 과자 국 김치 식용유여야 한다.
*/
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE (CATEGORY, PRICE) IN (SELECT CATEGORY, MAX(PRICE)
                    FROM FOOD_PRODUCT
                    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
                    GROUP BY CATEGORY)
ORDER BY MAX_PRICE DESC