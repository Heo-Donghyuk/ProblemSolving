SELECT PRODUCT_ID, PRODUCT_NAME, SUM(AMOUNT)*PRICE AS TOTAL_SALES
FROM FOOD_ORDER JOIN FOOD_PRODUCT USING(PRODUCT_ID)
WHERE YEAR(PRODUCE_DATE)=2022 AND MONTH(PRODUCE_DATE)=5
GROUP BY PRODUCT_ID
ORDER BY TOTAL_SALES DESC, PRODUCT_ID;