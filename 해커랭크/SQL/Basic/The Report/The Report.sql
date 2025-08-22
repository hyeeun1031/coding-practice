# Language: MySQL
SELECT CASE WHEN g.GRADE >= 8 THEN s.NAME
            ELSE 'NULL'
       END AS NAME,
       g.GRADE,
       s.MARKS
FROM STUDENTS s
JOIN GRADES g
ON s.MARKS BETWEEN g.MIN_MARK AND g.MAX_MARK
ORDER BY g.GRADE DESC, CASE WHEN g.GRADE >= 0 THEN s.NAME
                            ELSE s.MARKS
                       END ASC;
