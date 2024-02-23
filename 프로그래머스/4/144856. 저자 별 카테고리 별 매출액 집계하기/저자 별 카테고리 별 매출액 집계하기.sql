/*
아이디어:
- sales와 book, author를 2중 join하고
- 저자, 카테고리별로 group by 후 TOTAL_SALES 컬럼을 만들어 주자 -> sum(sales*price)
- 이후 조건에 맞게 정렬하자
조건:
- 2022년 1월의 도서 판매 데이터를 기준
- 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력
- 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬
주의
*/
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SALES*PRICE) AS TOTAL_SALES
FROM BOOK_SALES JOIN BOOK USING(BOOK_ID) JOIN AUTHOR USING(AUTHOR_ID)
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC