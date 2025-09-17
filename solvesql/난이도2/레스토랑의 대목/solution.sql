WITH daily_sales AS (SELECT day, SUM(total_bill) as daily_total
                     FROM tips 
                     GROUP BY day
                     HAVING SUM(total_bill) >= 1500)
SELECT t.*
FROM tips t
INNER JOIN daily_sales ds ON t.day = ds.day
ORDER BY t.day, t.total_bill DESC;
