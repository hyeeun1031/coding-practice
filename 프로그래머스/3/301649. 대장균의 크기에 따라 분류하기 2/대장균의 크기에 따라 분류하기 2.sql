-- 코드를 작성해주세요
WITH ranked AS (SELECT ID, NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS tile
                FROM ECOLI_DATA)

SELECT ID, CASE tile WHEN 1 THEN 'CRITICAL'
                     WHEN 2 THEN 'HIGH'
                     WHEN 3 THEN 'MEDIUM'
                     ELSE 'LOW'
           END AS COLONY_NAME
FROM ranked
ORDER BY ID;