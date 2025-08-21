-- 코드를 작성해주세요
WITH RECURSIVE gen AS (SELECT ID, PARENT_ID, 1 AS GENERATION
                       FROM ECOLI_DATA
                       WHERE PARENT_ID IS NULL
                       
                       UNION ALL
                       
                       SELECT e.ID, e.PARENT_ID, g.GENERATION + 1
                       FROM ECOLI_DATA AS e
                       JOIN GEN AS g
                       ON e.PARENT_ID = g.ID),

LEAF AS (SELECT g.ID, g.GENERATION
                        FROM GEN AS g
                        LEFT JOIN ECOLI_DATA AS c
                        ON c.PARENT_ID = g.ID
                        WHERE c.ID IS NULL)

SELECT COUNT(*) AS COUNT, GENERATION
FROM LEAF
GROUP BY GENERATION
ORDER BY GENERATION;
         