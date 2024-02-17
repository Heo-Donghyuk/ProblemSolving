SELECT USER_ID, NICKNAME,
CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소',
CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 8, 4)) AS '전화번호'
FROM USED_GOODS_USER
WHERE USER_ID IN (SELECT WRITER_ID
                FROM USED_GOODS_BOARD
                GROUP BY WRITER_ID
                HAVING COUNT(WRITER_ID)>=3)
ORDER BY USER_ID DESC