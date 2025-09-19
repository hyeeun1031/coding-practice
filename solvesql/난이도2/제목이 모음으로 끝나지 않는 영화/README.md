# 제목이 모음으로 끝나지 않는 영화

DVD Rental Store 데이터베이스는 DVD 대여점의 관리 프로그램이 사용하는 데이터베이스입니다. <br>
그 중 film 테이블은 DVD 대여점에서 취급하는 영화 정보를 담고 있습니다.

rating 컬럼에는 미국영화협회(Motion Picture Association, MPA)에서 운영하는 영화 등급 제도 데이터가 들어있습니다. <br>
이는 영화의 내용을 연령대별로 분류하여 관람 적합성을 판단하는 시스템인데 각 등급은 아래 의미를 가집니다.

- G (General Audience): 모든 연령 관람 가능
- PG (Parental Guidance Suggested): 아동 관람 시 부모 지도 필요
- PG-13 (Parents Strongly Cautioned): 13세 미만 관람 시 부모의 주의 필요
- R (Restricted): 17세 미만은 부모 또는 21세 이상과 동반 관람만 가능
- NC-17 (No One 17 and Under Admitted): 18세 미만 관람 불가

17세 미만 학생이 DVD 대여점에 혼자와서는 대여할 수 없는 영화 중 제목이 모음(’A’, ‘E’, ‘I’, ‘O’, ‘U’)로 끝나지 않는 영화를 찾고 싶습니다. <br> 
조건에 맞는 영화 제목(title)을 출력하는 쿼리를 작성해주세요. <br>
다른 컬럼은 출력되지 말아야 합니다.

| Column              | Type      | Description                         |
|---------------------|-----------|-------------------------------------|
| film_id             | integer   | 영화 ID                             |
| title               | string    | 영화 제목                           |
| description         | string    | 설명                                |
| release_year        | integer   | 발매 연도                           |
| language_id         | integer   | 언어 정보 ID                        |
| original_language_id| integer   | 원작 언어 정보 ID                   |
| rental_duration     | integer   | 대여기간 (일)                       |
| rental_rate         | number    | 대여 요금 ($)                       |
| length              | integer   | 영상 길이                           |
| replacement_cost    | number    | 분실 시 교체 비용 ($)               |
| rating              | string    | 등급 분류 (G, PG, PG-13, R, NC-17) |
| special_features    | string    | 추가 트랙 종류                      |
| last_update         | datetime  | 영화 정보 업데이트 시점             |
