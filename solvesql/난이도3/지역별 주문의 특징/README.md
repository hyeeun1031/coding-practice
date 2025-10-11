# 지역별 주문의 특징

US E-Commerce Records 2020 데이터베이스는 미국 이커머스 웹사이트의 판매 데이터를 담고 있습니다. <br>
records 테이블은 주문 번호, 주문 날짜, 주문 지역, 카테고리 등 주문의 상세 정보가 들어 있습니다. <br>
이 데이터를 이용하여 미국의 각 지역별로 어떤 카테고리의 상품이 많이 판매되는지 알아보려고 합니다. <br>
region, category 별 주문량을 계산해 출력하는 쿼리를 작성해주세요.

### 결과 데이터 형식
결과 데이터는 아래와 같은 테이블 형태로 출력되어야 하고, Region 컬럼 기준 오름차순으로 정렬되어 있어야 합니다.

| Region  | Furniture | Office Supplies | Technology |
|----------|------------|----------------|-------------|
| Central  |            |                |             |
| East     |            |                |             |
| South    |            |                |             |
| West     |            |                |             |

결과 데이터의 각 컬럼은 다음과 같은 의미를 갖습니다.

- Region - 주문 지역
- Furniture - 해당 지역 내 가구(’Furniture’) 주문 수
- Office Supplies - 해당 지역 내 오피스 물품(’Office Supplies’) 주문 수
- Technology - 해당 지역 내 전자기기(’Technology’) 주문 수

### records 테이블
| 컬럼명         | 데이터 타입 | 설명         |
|----------------|--------------|--------------|
| order_date     | date         | 주문 날짜     |
| order_id       | string       | 주문 ID       |
| ship_mode      | string       | 배송 타입     |
| customer_id    | string       | 고객 ID       |
| segment        | string       | 고객 타입     |
| country        | string       | 국가          |
| city           | string       | 도시          |
| state          | string       | 주(State)     |
| postal_code    | integer      | 우편번호       |
| region         | string       | 지역          |
| product_id     | string       | 상품 ID       |
| category       | string       | 카테고리       |
| sub_category   | string       | 서브 카테고리  |
| product_name   | string       | 상품명         |
| sales          | number       | 매출           |
| quantity       | integer      | 수량           |
| discount       | number       | 할인           |
| profit         | number       | 이익           |

### customer_stats 테이블
| 컬럼명             | 데이터 타입 | 설명         |
|--------------------|--------------|--------------|
| customer_id        | string       | 고객 ID       |
| first_order_date   | date         | 첫 주문일     |
| last_order_date    | date         | 마지막 주문일 |
| cnt_orders         | integer      | 주문 횟수     |
| sum_sales          | number       | 매출 합계     |

