/*
아이디어:
- 온, 오프라인 테이블을 세로로 합친다.
    -> union all 사용
- 2022년 3월에 해당하는 원소만 선택한다.
- userId가 null로 표시되는지 확인하고
- 정렬한다.
조건:
- 2022년 3월 오프라인/온라인 상품 판매 데이터
- 판매 날짜, 상품ID, 유저ID, 판매량
- 오프라인 테이블의 user_id 값은 Null로 표시
- 판매일 오름차순, id 오름차순, 유저 id 오름차순
*/
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'
UNION ALL
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE LIKE '2022-03%'
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID