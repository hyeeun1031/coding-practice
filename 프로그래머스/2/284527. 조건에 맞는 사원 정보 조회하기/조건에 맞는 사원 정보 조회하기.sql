-- 코드를 작성해주세요
SELECT y.SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
FROM (SELECT EMP_NO, SUM(SCORE) AS SCORE
      FROM HR_GRADE
      WHERE YEAR = 2022
      GROUP BY EMP_NO) AS y
JOIN HR_EMPLOYEES AS e
ON e.EMP_NO = y.EMP_NO
WHERE y.SCORE = (SELECT MAX(sum_score)
                 FROM (SELECT SUM(SCORE) AS SUM_SCORE
                       FROM HR_GRADE
                       WHERE YEAR = 2022
                       GROUP BY EMP_NO) AS s)
ORDER BY e.EMP_NO;