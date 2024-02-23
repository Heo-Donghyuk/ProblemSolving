/*
아이디어:
- 예약내역 테이블에서 220413 취소되지 않고, 흉부외과 진료 예약인 레코드만 선택
    - 이 테이블에 필요한 테이블을 join하자
조건:
- 2022년 4월 13일 취소되지 않은
- 흉부외과(CS) 진료 예약 내역을 조회
- 진료예약번호(A), 환자이름(P), 환자번호(A, P), 진료과코드(A), 의사이름(D), 진료예약일시(A) 항목이 출력
- 결과는 진료예약일시를 기준으로 오름차순 정렬
주의:
- left join 필요 없는지
- 중복 제거 필요한지
- 서브쿼리 밖에서 조건을 다시 지정할 필요가 있는지
*/
WITH A AS (SELECT *
          FROM APPOINTMENT
          WHERE APNT_YMD LIKE '2022-04-13%' AND
            MCDP_CD='CS' AND APNT_CNCL_YN='N')
SELECT APNT_NO, PT_NAME, PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM A JOIN PATIENT USING(PT_NO) JOIN DOCTOR ON A.MDDR_ID=DOCTOR.DR_ID
ORDER BY APNT_YMD