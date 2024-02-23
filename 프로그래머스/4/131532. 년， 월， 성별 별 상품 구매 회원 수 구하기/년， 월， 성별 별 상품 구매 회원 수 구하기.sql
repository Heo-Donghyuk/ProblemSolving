/*
아이디어
- sales와 info를 id로 join
- where 절에서 성별이 null인 레코드 제외
- month, year 컬럼을 만들고
    - group by month, year, gender로 그룹화
    - select 문에서 users 컬럼 만들기
        - count(user_id) => distinct 사용하기(중복 제거 필요)
- 이후 정렬
조건:
- 동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.
- 년, 월, 성별 별로 상품을 구매한 회원수를 집계
- 결과는 년, 월, 성별을 기준으로 오름차순 정렬
- 이때, 성별 정보가 없는 경우 결과에서 제외
주의:
*/
SELECT YEAR(SALES_DATE) AS YEAR, 
    MONTH(SALES_DATE) AS MONTH, 
    GENDER, 
    COUNT(DISTINCT USER_ID) AS USERS
FROM ONLINE_SALE JOIN USER_INFO USING(USER_ID)
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER