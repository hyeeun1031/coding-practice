# 점검이 필요한 자전거 찾기
따릉이를 운영하는 서울시에서는 매달 따릉이 자전거의 정기점검을 진행하고 있습니다. <br>
1달에 주행 거리가 50km 이상인 자전거가 정기점검 대상에 포함됩니다.

2021년 2월 정기점검 대상 자전거를 추출하려고 합니다. <br>
rental_history 테이블을 사용해 2021년 1월 한 달간 총 주행 거리가 50km 이상인 자전거의 ID를 출력하는 쿼리를 작성해주세요.

| Column     | Type    | Description        |
|------------|---------|--------------------|
| station_id | integer | 정류소 ID           |
| name       | string  | 정류소명             |
| local      | string  | 소속 지자체           |
| address    | string  | 주소                |
| lat        | number  | 위도 (deg)          |
| lng        | number  | 경도                |

<br>

| Column              | Type     | Description   |
|---------------------|----------|---------------|
| bike_id             | string   | 자전거 ID       |
| rent_at             | datetime | 대여 시각        |
| rent_station_id     | integer  | 대여 정류소 ID    |
| rent_slot_position  | integer  | 대여 거치대       |
| return_at           | datetime | 반납 시각        |
| return_station_id   | integer  | 반납 정류소 ID    |
| return_slot_position| integer  | 반납 거치대       |
| distance            | number   | 주행거리 (m)     |

