/*
아이디어:
서브쿼리와 in을 사용하자
- 서브쿼리에서 group by로 음식 종류별로 그룹화 후
    - 즐겨찾기가 가장 많은 즐겨찾기 수를 select 하자 (max 이용)
- 이후 where 절에서 해당 음식종류, 즐겨찾기 수가 서브쿼리 절에 존재하면 선택하자
조건:
- 음식종류별로 즐겨찾기수가 가장 많은 식당
- 음식 종류, ID, 식당 이름, 즐겨찾기수
- 음식 종류를 기준으로 내림차순 정렬
*/
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (SELECT FOOD_TYPE, MAX(FAVORITES)
                                FROM REST_INFO
                                GROUP BY FOOD_TYPE)
ORDER BY FOOD_TYPE DESC