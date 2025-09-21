SELECT c.name
FROM games g
JOIN companies c
  ON g.publisher_id = c.company_id
GROUP BY c.name
HAVING COUNT(*) >= 10
ORDER BY c.name;
