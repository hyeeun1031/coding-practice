# 연도별 배송 업체 이용 내역 분석하기

Store Sales in Winter 데이터베이스는 어떤 쇼핑몰 프랜차이즈의 2018년부터 2023년까지의 11월, 12월 상품 판매 기록을 담은 데이터베이스 입니다. <br>

최근 온라인 쇼핑몰의 판매량이 오프라인 지점들의 판매량을 추월했기에 배송 업체와 계약을 유리한 조건으로 하는 것이 실적 개선에 중요한 부분이 되었습니다. <br>
현재 온라인 쇼핑몰에서 제공하고 있는 배송 옵션은 일반 배송(Standard), 빠른 배송(Express), 익일 특급(Overnight) 세 종류 입니다.<Br>

내년도 배송 업체 계약을 위해 연도별 배송 업체 이용 건수의 통계를 집계하려고 합니다. <br>
온라인 쇼핑몰의 판매 내역에서 반품이 발생할 경우, 반품 회수를 위해 '일반 배송(Standard)' 서비스가 추가로 1회 이용됩니다. <br>
데이터베이스에는 반품된 거래에 대한 추가 배송 기록이 없기 때문에 고객이 선택한 원래 배송 옵션과 별개로 반품 건수를 일반 배송 이용 실적에 합산하여 집계해야 합니다. <br>

데이터베이스를 조회해 배송 업체 이용 건수를 배송 옵션 별로 집계하는 쿼리를 작성해주세요. 쿼리 결과는 아래 컬럼이 있어야 하고, 연도 기준 오름차순 정렬이 되어있어야 합니다. <br>

- year: 연도
- standard: 일반 배송 이용 건수
- express: 빠른 배송 이용 건수
- overnight: 익일 배송 이용 건수

### transactions

| 컬럼명 | 데이터 타입 | 설명 |
|------|-----------|------|
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
