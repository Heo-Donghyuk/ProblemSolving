SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(SUM_SALES*PRICE) AS TOTAL_SALES
FROM BOOK
JOIN AUTHOR USING(AUTHOR_ID)
JOIN (SELECT BOOK_ID, SUM(SALES) AS SUM_SALES
      FROM BOOK_SALES WHERE SALES_DATE LIKE '2022-01%' 
      GROUP BY BOOK_ID) AS S USING(BOOK_ID)
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC