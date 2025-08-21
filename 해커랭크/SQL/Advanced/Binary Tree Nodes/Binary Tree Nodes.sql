#Language: MySQL
SELECT b1.N, CASE WHEN b1.P IS NULL THEN 'Root'
                  WHEN b1.N IN (SELECT P
                                FROM BST
                                WHERE P IS NOT NULL) THEN 'Inner'
                  ELSE 'Leaf' 
             END AS NodeType
FROM BST b1
ORDER BY b1.N;
