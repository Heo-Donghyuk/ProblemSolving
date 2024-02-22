SELECT (CASE
        WHEN (SELECT SUM(CODE) # 프론트엔드
             FROM SKILLCODES
             GROUP BY CATEGORY
             HAVING CATEGORY='Front End') & SKILL_CODE>0 AND
            (SELECT CODE # 파이썬
            FROM SKILLCODES
            WHERE NAME='Python') & SKILL_CODE>0 THEN 'A'
        WHEN (SELECT CODE # C#
             FROM SKILLCODES
             WHERE NAME='C#') & SKILL_CODE>0 THEN 'B'
        WHEN (SELECT SUM(CODE) # 프론트엔드
             FROM SKILLCODES
             GROUP BY CATEGORY
             HAVING CATEGORY='Front End') & SKILL_CODE>0 THEN 'C'
        END) AS GRADE, ID, EMAIL
FROM DEVELOPERS
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID