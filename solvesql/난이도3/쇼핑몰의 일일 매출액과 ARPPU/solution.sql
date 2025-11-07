-- 2018-01-01 이후 일별 결제 고객 수(PU), 매출액, ARPPU
WITH pay_per_order AS (
  SELECT
    order_id,
    SUM(payment_value) AS order_amount
  FROM olist_order_payments_dataset
  GROUP BY order_id
),
orders_base AS (
  SELECT
    order_id,
    customer_id,
    DATE(order_purchase_timestamp) AS dt
  FROM olist_orders_dataset
  WHERE DATE(order_purchase_timestamp) >= '2018-01-01'
)

SELECT
  o.dt AS dt,                                   -- 매출 날짜 (YYYY-MM-DD)
  COUNT(DISTINCT o.customer_id) AS pu,          -- 결제 고객 수
  ROUND(SUM(p.order_amount), 2) AS revenue_daily,             -- 일 매출액(소수점 둘째자리)
  ROUND(SUM(p.order_amount) / COUNT(DISTINCT o.customer_id), 2) AS arppu  -- ARPPU
FROM orders_base o
JOIN pay_per_order p
  USING (order_id)
GROUP BY o.dt
ORDER BY o.dt;
