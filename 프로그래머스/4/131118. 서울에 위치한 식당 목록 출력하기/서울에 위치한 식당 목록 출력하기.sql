/*
아이디어
- 리뷰테이블에서 group by로 레스토랑별 평균 점수를 얻자 - 단, 소수점 세번째 자리에서 반올림에 주의
- 이후 join하고
    - where 절에서 서울에 위치한 식당을 뽑은 후
    - 점수 내림차순, 즐겨찾기수 내림차순 정렬을 하자
*/
SELECT REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, SCORE
FROM REST_INFO JOIN (SELECT ROUND(AVG(REVIEW_SCORE), 2) AS SCORE, REST_ID
                    FROM REST_REVIEW
                    GROUP BY REST_ID) R USING(REST_ID)
WHERE ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC