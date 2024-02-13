SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE find_in_set('통풍시트', OPTIONS) OR
    find_in_set('열선시트', OPTIONS) OR
    find_in_set('가죽시트', OPTIONS)
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE