/*
조건:
- 완료된 중고 거래의 총금액이 70만 원 이상인 사람
- 회원 ID, 닉네임, 총거래금액
- 총거래금액을 기준으로 오름차순 정렬
주의:
아이디어:
- board에서 status가 done인 레코드를 where 절에서 선택 후
    - writer_id를 기준으로 group by 후 
    - sum(price)로 총 거래 금액을 만들어 주자
    - 이 테이블과 user 테이블을 writer id로 join 하자
- 이후 총 거래금액 오름차순 정렬
*/
SELECT USER_ID, NICKNAME, TOTAL_SALES
FROM USED_GOODS_USER U JOIN (SELECT WRITER_ID, SUM(PRICE) AS TOTAL_SALES
                          FROM USED_GOODS_BOARD
                          WHERE STATUS = 'DONE'
                          GROUP BY WRITER_ID
                          HAVING TOTAL_SALES>=700000) B
                          ON U.USER_ID=B.WRITER_ID
ORDER BY TOTAL_SALES