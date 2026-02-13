# DVD 대여점 우수 고객 찾기

DVD Rental Store 데이터베이스에는 어느 한 DVD 대여 프랜차이즈의 고객 정보, DVD 대여 정보, 제공 중인 영화의 정보 등이 들어있습니다. <br>
최근 다양한 OTT 서비스의 흥행으로 고객이 이탈하고 있어 우수 고객 대상 크리스마스 특별 프로모션을 진행하려고 합니다. <br>
우수 고객은 현재 대여점의 유효 고객 중 대여 횟수가 35회 이상인 고객입니다. <br>

데이터베이스를 조회해 프로모션 대상 우수 고객들의 고객 ID를 조회하는 쿼리를 작성해주세요. <br>
쿼리 결과에는 아래 컬럼이 있어야 합니다. <br>

- customer_id: 프로모션 대상 우수 고객의 ID

### customer

| 컬럼명         | 데이터 타입   | 설명            |
| ----------- | -------- | ------------- |
| customer_id | integer  | 고객 ID         |
| store_id    | integer  | 담당 점포 ID      |
| first_name  | string   | 고객 이름 (이름)    |
| last_name   | string   | 고객 이름 (성)     |
| email       | string   | 메일 주소         |
| address_id  | integer  | 주소 정보 ID      |
| active      | boolean  | 유효 고객 여부      |
| create_date | date     | 고객 등록일        |
| last_update | datetime | 고객 정보 업데이트 시점 |


### rental

| 컬럼명          | 데이터 타입   | 설명            |
| ------------ | -------- | ------------- |
| rental_id    | integer  | 대여 기록 ID      |
| rental_date  | datetime | 대여 시각         |
| inventory_id | integer  | 재고 ID         |
| customer_id  | integer  | 대여 고객 ID      |
| return_date  | datetime | 반납 시각         |
| staff_id     | integer  | 점원 ID         |
| last_update  | datetime | 대여 기록 업데이트 시점 |
