/*
아이디어:
- 리뷰를 가장 많이 작성한 회원의 아이디를 with절로 만들자
- 이후 where 절에서 아이디가 with 절에서 만든 테이블에 속한다면 선택하자
- 조건에 맞게 정렬
조건:
- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회
- 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력
- 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬
주의:
- 가장 많이 작성한 사람이 여러 명이라면? -> 모두 포함하도록 일단 하자
- left join 사용이 필요한지
- 중복 제거가 필요한지
- 서브 쿼리 밖에서 다시 한 번 조건을 적용할 필요가 있는지
*/

WITH MEMBER_COUNT AS (SELECT MEMBER_ID, COUNT(*) AS COUNT
            FROM REST_REVIEW
            GROUP BY MEMBER_ID)
            
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW JOIN MEMBER_PROFILE USING(MEMBER_ID)
WHERE MEMBER_ID IN (SELECT MEMBER_ID FROM MEMBER_COUNT
                   WHERE COUNT=(SELECT MAX(COUNT) FROM MEMBER_COUNT))
ORDER BY REVIEW_DATE, REVIEW_TEXT