SELECT
    classification,
    COUNT(CASE WHEN EXTRACT(YEAR FROM acquisition_date) = 2014 THEN 1 END) AS "2014",
    COUNT(CASE WHEN EXTRACT(YEAR FROM acquisition_date) = 2015 THEN 1 END) AS "2015",
    COUNT(CASE WHEN EXTRACT(YEAR FROM acquisition_date) = 2016 THEN 1 END) AS "2016"
FROM artworks
GROUP BY classification
ORDER BY classification;
