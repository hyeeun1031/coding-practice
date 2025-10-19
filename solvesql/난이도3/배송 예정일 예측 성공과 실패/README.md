# 배송 예정일 예측 성공과 실패
Brazilian E-Commerce Public Dataset by Olist 데이터베이스는 브라질의 이커머스 웹사이트인 Olist Store의 판매 데이터 입니다. <br>
그 중 olist_orders_dataset 테이블에는 주문 ID, 고객 ID, 주문 상태, 구매 시각 등 주문 내역 데이터가 들어있습니다. <br>
Olist의 주문부터 배송까지 프로세스는 다음 단계를 통해 이루어지고, 각 단계마다 시각을 기록하고 있습니다.

1. 고객의 구매
- order_purchase_timestamp 컬럼에 구매 시점이 저장됨

2. 판매자가 주문을 승인
- order_approved_at 컬럼에 승인 시점이 저장됨

3. 택배사에 도착하여 배송 시작
- order_delivered_carrier_date 컬럼에 배송 시작 시점이 저장됨

4. 배송 완료
- order_delivered_customer_date 컬럼에 배송 완료 시점이 저장됨

추가로 order_estimated_delivery_date 컬럼에는 주문 시점에 계산한 배송 예정 시각이 저장되어 있습니다. <br>
예를 들어, 컬럼에 값이 ‘2017-02-24 00:00:00’로 들어있는 경우, 배송을 2017년 2월 24일 자정까지 완료하겠다는 의미를 담고 있습니다.

2017년 1월 한 달 동안 발생한 주문의 배송 예측이 정확했는지 분석을 하려고 합니다. <Br>
고객의 구매 일자별로 배송 예정 시각 안에 고객에게 도착한 주문과, 배송 예정 시각이 지나서 고객에게 도착한 주문을 각각 집계하는 쿼리를 작성해주세요. <br>
배송 완료 또는 배송 예정 시각 데이터가 없는 경우는 계산에서 제외합니다. <br>
계산 결과는 구매 날짜를 기준으로 오름차순 정렬되어야 하고, 아래 컬럼을 포함해야 합니다.

- purchase_date - 구매 날짜 (예: 2017-01-01)
- success - 배송 예정 시각 안에 고객에게 도착한 주문 수
- fail - 배송 예정 시각이 지나 고객에게 도착한 주문 수

### 결과 데이터 예시
| purchase_date | success | fail |
|----------------|----------|------|
| 2017-01-06     | 4        | 0    |
| 2017-01-07     | 3        | 1    |

- 2017년 1월 6일 구매된 주문은 총 4건이고 모두 배송 예정일 안에 배송 완료됨
- 2017년 1월 7일 구매된 주문은 총 4건이고 그 중 3건은 배송 예정일 안에 배송 완료되었으나, 1건은 배송 예정일 이후에 배송 완료됨

### olist_closed_deals_dataset
| Column | Type | Description |
|---------|------|-------------|
| mql_id | string | Marketing Qualified Lead (잠재 판매자) ID |
| seller_id | string | 판매자 ID |
| sdr_id | string | SDR (Sales Development Representative) ID |
| sr_id | string | SR (Sales Representative, 영업 사원) ID |
| won_date | datetime | 판매자 계약 성사 시각 |
| business_segment | string | 잠재 판매자 분야 |
| lead_type | string | 잠재 판매자 타입 |
| lead_behaviour_profile | string | 잠재 판매자 프로파일 |
| has_company | boolean | 잠재 판매자가 회사인지 여부 |
| has_gtin | boolean | 잠재 판매자가 GTIN을 갖고 있는지 여부 |
| average_stock | string | 평균 재고 |
| business_type | string | 비즈니스 종류 (리셀러, 제조업 등) |
| declared_product_catalog_size | number | 상품 카탈로그 크기 |
| declared_monthly_revenue | number | 월 수익 |


### olist_customers_dataset
| Column | Type | Description |
|---------|------|-------------|
| customer_id | string | 주문 별 고객 ID |
| customer_unique_id | string | 고객 ID |
| customer_zip_code_prefix | string | 고객 우편번호 앞 5자리 |
| customer_city | string | 고객 주소 (도시) |
| customer_state | string | 고객 주소 (주) |


### olist_geolocation_dataset
| Column | Type | Description |
|---------|------|-------------|
| geolocation_zip_code_prefix | string | 우편번호 앞 5자리 |
| geolocation_lat | number | 위도 |
| geolocation_lng | number | 경도 |
| geolocation_city | string | 도시 |
| geolocation_state | string | 주 |


### olist_marketing_qualified_leads_dataset
| Column | Type | Description |
|---------|------|-------------|
| mql_id | string | Marketing Qualified Lead (잠재 판매자) ID |
| first_contact_date | date | 첫 계약 (SDR과의 계약) 시각 |
| landing_page_id | string | 랜딩 페이지 ID |
| origin | string | 유입 경로 |


### olist_order_items_dataset
| Column | Type | Description |
|---------|------|-------------|
| order_id | string | 주문 ID |
| order_item_id | integer | 주문 내 상품 순서 |
| product_id | string | 상품 ID |
| seller_id | string | 판매자 ID |
| shipping_limit_date | datetime | 발송 제한 일자 |
| price | number | 가격 |
| freight_value | number | 운송료 |


### olist_order_payments_dataset
| Column | Type | Description |
|---------|------|-------------|
| order_id | string | 주문 ID |
| payment_sequential | integer | 연속 결제 횟수 |
| payment_type | string | 결제 방법 |
| payment_installments | integer | 할부 개월 수 |
| payment_value | number | 결제 금액 |


### olist_order_reviews_dataset
| Column | Type | Description |
|---------|------|-------------|
| review_id | string | 리뷰 ID |
| order_id | string | 주문 ID |
| review_score | integer | 평점 |
| review_comment_title | string | 리뷰 코멘트 제목 (포르투갈어) |
| review_comment_message | string | 리뷰 코멘트 (포르투갈어) |
| review_creation_date | datetime | 리뷰 요청 일자 |
| review_answer_timestamp | datetime | 리뷰 답변 일자 |


### olist_orders_dataset
| Column | Type | Description |
|---------|------|-------------|
| order_id | string | 주문 ID |
| customer_id | string | 주문 별 고객 ID |
| order_status | string | 주문 상태 |
| order_purchase_timestamp | datetime | 구매 시각 |
| order_approved_at | datetime | 주문 승인 시각 |
| order_delivered_carrier_date | datetime | 배송 시작 시각 |
| order_delivered_customer_date | datetime | 배송 완료 시각 |
| order_estimated_delivery_date | datetime | 배송 예정 시각 |


### olist_products_dataset
| Column | Type | Description |
|---------|------|-------------|
| product_id | string | 상품 ID |
| product_category_name | string | 상품 카테고리 |
| product_name_lenght | integer | 상품명 길이 |
| product_description_lenght | integer | 상품 설명 길이 |
| product_photos_qty | integer | 상품 사진 개수 |
| product_weight_g | integer | 상품 무게 (g) |
| product_length_cm | integer | 상품 길이 (cm) |
| product_height_cm | integer | 상품 높이 (cm) |
| product_width_cm | integer | 상품 너비 (cm) |


### olist_sellers_dataset
| Column | Type | Description |
|---------|------|-------------|
| seller_id | string | 판매자 ID |
| seller_zip_code_prefix | string | 판매자 우편번호 앞 5자리 |
| seller_city | string | 판매자 위치 (도시) |
| seller_state | string | 판매자 위치 (주) |


### product_category_name_translation
| Column | Type | Description |
|---------|------|-------------|
| product_category_name | string | 상품 카테고리 |
| product_category_name_english | string | 상품 카테고리 (영어) |
