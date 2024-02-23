/*
아이디어:
- where 절에서 나이정보가 없는 레코드만 선택
- select 절에서 count(*)
조건:
- 나이 정보가 없는 회원이 몇 명인지 출력
- 컬럼명은 USERS로 지정
주의:
- 서브쿼리 밖에서 조건 확인
- left join 필요한지
- 중복 제거 필요한지
*/
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;
# select * from user_info order by gender