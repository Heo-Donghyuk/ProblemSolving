/*
아이디어:
- group by로 그룹화 하자
    - price를 10000으로 나눈 몫 * 10000을 그룹화의 키로 사용하자
조건
주의:
- 중복 제거 필요한지
- left join
- 서브쿼리 밖에서 조건을 추가할 필요가 있는지
*/
SELECT FLOOR(PRICE/10000)*10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY FLOOR(PRICE/10000)*10000
ORDER BY PRICE_GROUP