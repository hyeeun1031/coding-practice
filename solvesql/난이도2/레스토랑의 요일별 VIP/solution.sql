SELECT t.*
FROM tips t
JOIN (SELECT day, MAX(total_bill) AS max_bill
      FROM tips
      GROUP BY day) m
ON t.day = m.day
AND t.total_bill = m.max_bill;
