/*
아이디어:
- union all로 테이블 합치기
    - offline 테이블에 null인 userId컬럼 만든 후 합치기
조건:
- 2022년 3월
- 판매 날짜, 상품ID, 유저ID, 판매량을 출력
- OFFLINE_SALE 테이블의 판매 데이터의 USER_ID 값은 NULL 로 표시
- 결과는 판매일을 기준으로 오름차순 정렬해주시고 
    판매일이 같다면 상품 ID를 기준으로 오름차순, 
    상품ID까지 같다면 유저 ID를 기준으로 오름차순 정렬해주세요.
주의:
- left join 필요한지
- 중복 제거 필요한지
- 서브쿼리 밖에서 조건 재확인 필요한지
*/
WITH U AS (SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
           FROM ONLINE_SALE
           WHERE SALES_DATE LIKE '2022-03%'
          UNION ALL
          SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
           FROM OFFLINE_SALE
          WHERE SALES_DATE LIKE '2022-03%')
SELECT *
FROM U
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID