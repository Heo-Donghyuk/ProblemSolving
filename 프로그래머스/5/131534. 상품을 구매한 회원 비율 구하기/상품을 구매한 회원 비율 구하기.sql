/*
아이디어:
- WITH절로 2021년에 가입한 사람들을 따로 모으자
    - GROUP BY user_id로 묶어 중복을 제거하자
- 메인 쿼리에서
    - where 절에서 2021년에 가입한 레코드만 선택하고
    - group by 년, 월로 묶고
        - count distinct user_id로 구매한 회원 수를 구하자
        
조건:
- 2021년에 가입한 전체 회원들 중
- 상품을 구매한 회원수와 상품을 구매한 회원의 비율
    (=2021년에 가입한 회원 중 상품을 구매한 회원수 / 2021년에 가입한 전체 회원 수)을 년, 월 별로 출력
- 상품을 구매한 회원의 비율은 소수점 두번째자리에서 반올림
- 전체 결과는 년을 기준으로 오름차순 정렬해주시고 년이 같다면 월을 기준으로 오름차순 정렬
주의:
- left join
- 중복 제거
- 서브 쿼리 밖에서 다시 조건
*/
WITH MEMBER_2021 AS (SELECT *
                    FROM USER_INFO
                    WHERE JOINED LIKE '2021%')
SELECT YEAR(SALES_DATE) AS YEAR,
    MONTH(SALES_DATE) AS MONTH,
    COUNT(DISTINCT USER_ID) AS PUCHASED_USERS,
    ROUND(COUNT(DISTINCT USER_ID)/(SELECT COUNT(USER_ID) FROM MEMBER_2021), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT USER_ID FROM MEMBER_2021)
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;