/*
아이디어:
- history 테이블에서 대여 기간을 확인하여 221016일을 포함하는 기간이라면 1, 아니면 0을 표현하는 컬럼을 만들자
- 차량 id로 group by 후 새 컬럼의 합이 0이면 대여 가능, 1이상이면 대여중을 표현하는 새 컬럼을 만들자
- 이후 차량id 내림차순 정렬하자
조건:
- 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: AVAILABILITY)을 추가
- 자동차 ID와 AVAILABILITY 리스트를 출력
- 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시
- 결과는 자동차 ID를 기준으로 내림차순 정렬
주의:
*/
SELECT CAR_ID, if(SUM('2022-10-16' BETWEEN START_DATE AND END_DATE)=0, '대여 가능', '대여중') AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC