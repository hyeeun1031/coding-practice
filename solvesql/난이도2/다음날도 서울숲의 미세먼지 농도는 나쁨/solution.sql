SELECT m1.measured_at AS today,
       m2.measured_at AS next_day,
       m1.pm10,
       m2.pm10 AS next_pm10
FROM measurements m1
JOIN measurements m2
  ON m1.station = m2.station
 AND m2.measured_at = DATE_ADD(m1.measured_at, INTERVAL 1 DAY)
WHERE m2.pm10 > m1.pm10
ORDER BY m1.measured_at;
