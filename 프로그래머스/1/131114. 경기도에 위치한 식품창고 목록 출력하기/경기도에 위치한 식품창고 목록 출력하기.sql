/*
아이디어
- where절에서 like로 경기도 주소 파악
- select절에서 ifnull로 null인 경우 'N'으로 출력
조건:
- 경기도에 위치한 창고
- ID, 이름, 주소, 냉동시설 여부를 조회
- 냉동시설 여부가 NULL인 경우, 'N'으로 출력
- 결과는 창고 ID를 기준으로 오름차순 정렬
주의
- 중복 제거 필요한지
- left join 필요한지
- 서브쿼리 밖에서 조건 확인 필요한지
*/
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID