SELECT bike_id
FROM rental_history
WHERE rent_at >= '2021-01-01'
AND   rent_at < '2021-02-01'
GROUP BY bike_id
HAVING SUM(COALESCE(distance, 0)) >= 50000
ORDER BY bike_id;
