/*
아이디어:
- GROUP BY로 ROUTE(노선)별 그룹화
- 이후 select 절에서 총 누계 거리, 평균 역 사이 거리 컬럼 만들기
    - 총 누계 거리는 D_BETWEEN_DIST의 합
    - 평균 역 사이 거리는 D_BETWEEN_DIST의 평균
    - 이후 조건에 맞게 반올림하고
    - 단위를 함께 출력
        - 단위를 함께 어떻게 출력하지? concat을 사용해야 하나?
조건:
- 노선별(ROUTE)
    - 노선, 총 누계 거리, 평균 역 사이 거리를 노선별로 조회
- 총 누계거리는 테이블 내 존재하는 역들의 역 사이 거리의 총 합
- 총 누계 거리와 평균 역 사이 거리의 컬럼명은 각각 TOTAL_DISTANCE, AVERAGE_DISTANCE
- 총 누계거리는 소수 둘째자리에서, 평균 역 사이 거리는 소수 셋째 자리에서 반올림 한 뒤 단위(km)를 함께 출력
- 결과는 총 누계 거리를 기준으로 내림차순 정렬
주의:
- left join 필요한지
- 중복제거 필요한지
- 서브쿼리 밖에서 조건 재확인 필요한지
*/
# help 'substr'
SELECT ROUTE,
    CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
    CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY SUBSTR(TOTAL_DISTANCE, -3) DESC