# AB테스트를 위한 버킷 나누기 2

Store Sales in Winter 데이터베이스는 어떤 쇼핑몰 프랜차이즈의 2018년부터 2023년까지의 11월, 12월 상품 판매 기록을 담은 데이터베이스 입니다. <br>

당신은 A/B 테스트를 위해 사용자 ID가 10으로 나누어 떨어지는 사용자를 A 버킷으로, 나누어 떨어지지 않는 사용자를 B 버킷으로 나눈 후 A 버킷에 할당된 사용자에게만 변경을 주어 지표를 추적하는 실험을 계획하고 있습니다. <br>

커머스 서비스에서 사용자를 기준으로 버킷을 나눌 때는 사전에 버킷이 균등하게 나뉘어져 있는지 확인하는 절차가 필요합니다. <br>
특정 버킷에 큰 손 고객이 몰려 있는 경우 테스트 결과가 왜곡 될 수 있기 때문입니다. <br>

이를 확인하기 위해 버킷별 사용자 수, 평균 주문 수, 평균 주문 금액을 확인하려고 합니다. <br>
아래 데이터를 추출하는 쿼리를 작성해주세요. <br>

- bucket: 사용자 버킷
- user_count: 버킷에 포함된 사용자 수
- avg_orders: 버킷에 포함된 사용자들의 평균 주문 수
- avg_revenue: 버킷에 포함된 사용자들의 평균 주문 금액 ($)

평균 집계에 사용되는 주문에는 최종적으로 반품된 주문은 제외해야 하고, 모든 평균값은 소수점 아래 셋째 자리에서 반올림 해 둘째 자리까지 표현되어야 합니다.

### transactions

| 컬럼명 | 타입 | 정의 |
|------|------|-------------|
| transaction_id | integer | 거래 ID |
| purchased_at | datetime | 상품 구매 시각 |
| customer_id | integer | 고객 ID |
| age | integer | 고객 나이 |
| gender | string | 고객 성별 (Male / Female / Other) |
| city_id | integer | 고객 도시 ID |
| store_id | integer | 오프라인 상점 ID |
| is_online_order | boolean | 온라인 구매 여부 |
| product_id | integer | 상품 ID |
| category | string | 상품 카테고리 |
| quantity | integer | 구매 수량 |
| unit_price | number | 상품 단가 ($) |
| total_price | number | 주문 금액 ($) |
| payment_type | string | 결제 방식 (Online Payment / Debit Card / Cash / Credit Card) |
| is_promotion_applied | boolean | 프로모션 적용 여부 |
| discount_amount | number | 할인 금액 ($) |
| is_gift_wrap | boolean | 선물 포장 여부 |
| shipping_method | string | 배송 방법 (Standard / Overnight / Express) |
| days_delivery | integer | 배송 기간 (일) |
| special_event | string | 이벤트 (Black Friday / Christmas Market) |
| satisfaction_score | integer | 고객 만족 점수 (1–5) |
| is_returned | boolean | 상품 반품 여부 |
