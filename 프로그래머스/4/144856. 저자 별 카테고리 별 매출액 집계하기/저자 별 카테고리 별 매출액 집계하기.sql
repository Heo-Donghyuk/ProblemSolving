/*
아이디어:
- sales join book (book_id) join author (quthor_id)로 삼중 join 후
    - where절에서 2022 1월의 레코드만 남기자
    - group by로 저자, 카테고리별로 묶고
        - sum(sales*price)로 매출을 구하자
조건:
- 2022년 1월의 도서 판매 데이터를 기준
- 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여
- 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력
- 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬
주의:
- left join 필요한지
- 중복제거 필요한지
- 서브쿼리 밖에서 재확인 필요한지
*/
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(PRICE*SALES) AS TOTAL_SALES
FROM BOOK_SALES JOIN BOOK USING(BOOK_ID) JOIN AUTHOR USING(AUTHOR_ID)
WHERE SALES_DATE LIKE '2022-01%'
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC;