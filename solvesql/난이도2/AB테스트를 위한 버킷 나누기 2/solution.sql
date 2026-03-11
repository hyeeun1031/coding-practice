SELECT bucket,
       COUNT(custoer_id) AS user_count, 
       ROUND(AVG(order_cnt), 2) AS avg_orders,
       ROUND(AVG(revenue), 2) AS avg_revenue
FROM (SELECT CASE WHEN customer_id % 10 = 0 THEN 'A'
                  ELSE 'B'
             END AS bucket,
             customer_id,
             COUNT(*) AS order_cnt,
             SUM(total_price) AS revenue
      FROM transactions
      WHERE is_returned = FALSE
      GROUP BY customer_id) t
GROUP BY bucket
ORDER BY bucket;
