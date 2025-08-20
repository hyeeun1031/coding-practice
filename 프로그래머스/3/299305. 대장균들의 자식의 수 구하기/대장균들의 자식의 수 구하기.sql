-- 코드를 작성해주세요
SELECT e1.ID, COUNT(e2.ID) AS CHILD_COUNT
FROM ECOLI_DATA e1
LEFT JOIN ECOLI_DATA e2 # self join
# 하나의 테이블 안에 계층적 관계가 있을 때 사용 (부모-자식 관계)
ON e1.ID = e2.PARENT_ID
GROUP BY e1.ID
ORDER BY e1.ID;