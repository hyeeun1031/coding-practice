WITH
  base AS (
    SELECT
      DATE(order_purchase_timestamp) AS purchase_date,
      order_delivered_customer_date,
      order_estimated_delivery_date
    FROM
      olist_orders_dataset
    WHERE
      order_purchase_timestamp >= TIMESTAMP '2017-01-01 00:00:00'
      AND order_purchase_timestamp < TIMESTAMP '2017-02-01 00:00:00'
      AND order_delivered_customer_date IS NOT NULL
      AND order_estimated_delivery_date IS NOT NULL
  )
SELECT
  purchase_date,
  SUM(
    CASE
      WHEN order_delivered_customer_date <= order_estimated_delivery_date THEN 1
      ELSE 0
    END
  ) AS success,
  SUM(
    CASE
      WHEN order_delivered_customer_date > order_estimated_delivery_date THEN 1
      ELSE 0
    END
  ) AS fail
FROM
  base
GROUP BY
  purchase_date
ORDER BY
  purchase_date;
