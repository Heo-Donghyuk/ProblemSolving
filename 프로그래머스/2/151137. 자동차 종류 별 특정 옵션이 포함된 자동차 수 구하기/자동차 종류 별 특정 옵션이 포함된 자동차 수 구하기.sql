/*
아이디어:
- 통, 열, 가죽시트를 포함한 레코드를 where 절에서 선택
    - like 또는 in 키워드를 사용하자
        - '가죽시트' in '가죽시트,열선시트,후방카메라'는 0을 리턴 => like 키워드를 사용하자
- 이후 group by로 car type에 따라 그룹화
- 해당 종류에 속하는 레코드 수를 count로 세자
- 이후 종류를 기준으로 오름차순 정렬
조건:
- '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 자동차 종류 별로 몇 대인지 출력
- 자동차 수에 대한 컬럼명은 CARS로 지정
- 결과는 자동차 종류를 기준으로 오름차순 정렬
주의:
*/
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%' OR
        OPTIONS LIKE '%열선시트%' OR
        OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE