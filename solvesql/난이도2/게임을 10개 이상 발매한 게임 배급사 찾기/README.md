# 게임을 10개 이상 발매한 게임 배급사 찾기

Video Game Sales with Ratings 데이터베이스에는 2016년까지 발매된 게임의 주요 정보와 판매량, 평점 정보를 담고 있습니다.  <br>
처음 개발한 게임의 출시를 앞두고 있는 당신은 경험 많은 게임 배급사와 협업하기 위해 게임 배급사로 참여한 게임이 10개 이상인 회사에게 협업 제안을 보내려고 합니다.

데이터베이스를 조회해 게임 배급사로 참여한 게임이 10개 이상인 회사의 이름을 출력하는 쿼리를 작성해주세요. <br>
쿼리 결과는 아래 컬럼을 포함하고 있어야 합니다.

| Column    | Type    | Description |
|-----------|---------|-------------|
| genre_id  | integer | 장르 ID     |
| name      | string  | 장르 이름   |

| Column       | Type    | Description    |
|--------------|---------|----------------|
| platform_id  | integer | 게임 플랫폼 ID |
| name         | string  | 게임 플랫폼 이름 |

| Column     | Type    | Description |
|------------|---------|-------------|
| company_id | integer | 회사 ID     |
| name       | string  | 회사명      |

| Column        | Type    | Description           |
|---------------|---------|-----------------------|
| game_id       | integer | 게임 ID               |
| name          | string  | 게임 이름             |
| year          | integer | 출시 연도             |
| platform_id   | integer | 게임 플랫폼 ID        |
| genre_id      | integer | 장르 ID               |
| publisher_id  | integer | 게임 배급사 ID        |
| developer_id  | integer | 게임 개발사 ID        |
| sales_na      | number  | 북미 지역 판매량 (백만) |
| sales_eu      | number  | 유럽 지역 판매량 (백만) |
| sales_jp      | number  | 일본 지역 판매량 (백만) |
| sales_other   | number  | 기타 지역 판매량 (백만) |
| critic_score  | number  | 평론가 평균 점수 (0-10) |
| critic_count  | integer | 평가에 참여한 평론가 수 |
| user_score    | number  | 사용자 평균 점수 (0-10) |
| user_count    | number  | 평가에 참여한 사용자 수 |
