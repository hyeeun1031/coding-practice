# 12월 우수 고객 찾기

US E-Commerce Records 2020 데이터베이스에는 2020년 1년 동안 미국의 한 커머스 업체의 주문 정보가 저장되어 있습니다. <br>

12월 판매 실적을 개선하기 위해 지난 12월에 매출이 높았던 고객들에게 프로모션을 제공하려고 합니다. <br>
2020년 12월 동안 있었던 모든 주문의 매출 합계가 1000$ 이상인 고객 ID를 출력하는 쿼리를 작성해주세요. <br>
쿼리 결과에는 고객 ID가 들어있는 컬럼 하나만 있어야 합니다. <br>

### records

| 컬럼명 | 데이터 타입 | 설명 |
|------|-----------|------|
| order_date | date | 주문 날짜 |
| order_id | string | 주문 ID |
| ship_mode | string | 배송 타입 |
| customer_id | string | 고객 ID |
| segment | string | 고객 타입 |
| country | string | 국가 |
| city | string | 도시 |
| state | string | 주 |
| postal_code | integer | 우편번호 |
| region | string | 지역 |
| product_id | string | 상품 ID |
| category | string | 카테고리 |
| sub_category | string | 서브 카테고리 |
| product_name | string | 상품명 |
| sales | number | 주문 총 매출 ($) |
| quantity | integer | 수량 |
| discount | number | 할인 ($) |
| profit | number | 이익 ($) |

### customer_stats

| 컬럼명 | 데이터 타입 | 설명 |
|------|-----------|------|
| customer_id | string | 고객 ID |
| first_order_date | date | 첫 주문일 |
| last_order_date | date | 마지막 주문일 |
| cnt_orders | integer | 주문횟수 |
| sum_sales | number | 매출 합계 |

