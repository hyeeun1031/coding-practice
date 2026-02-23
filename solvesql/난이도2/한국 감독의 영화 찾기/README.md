# 한국 감독의 영화 찾기

Museum of Modern Art Collection 데이터베이스는 미국 뉴욕의 근현대 미술관인 MoMA의 작품과 작가 정보를 담고 있습니다. <br>
MoMA는 미술품이나 조각상과 같은 물리적인 형태가 있는 작품 이외에도 비디오 아트나 영화 같은 무형의 작품도 소장하고 있습니다. <br>

데이터베이스를 조회해 MoMA가 소장하고 있는 작품 중 한국 감독의 영화를 찾아, 감독 이름과 작품명을 출력하는 쿼리를 작성해주세요. <br>
영화는 artworks 테이블의 classification 컬럼이 Film으로 시작하는 작품입니다. <br>

쿼리 결과에는 아래 컬럼이 포함되어 있어야 합니다. <br>

- artist - 감독 이름
- title - 작품명

### artists

| 컬럼명         | 자료형     | 설명      |
| ----------- | ------- | ------- |
| artist_id   | integer | 아티스트 ID |
| name        | string  | 아티스트 이름 |
| nationality | string  | 국적      |
| gender      | string  | 성별      |
| birth_year  | integer | 출생연도    |
| death_year  | integer | 사망연도    |


### artworks

| 컬럼명              | 자료형     | 설명       |
| ---------------- | ------- | -------- |
| artwork_id       | integer | 작품 ID    |
| title            | string  | 제목       |
| date             | string  | 작품 완성연도  |
| medium           | string  | 재료       |
| dimensions       | string  | 크기       |
| acquisition_date | date    | 소장 일시    |
| credit           | string  | 소장 경로    |
| catalogue        | boolean | 카탈로그 유무  |
| department       | string  | 담당 부서    |
| classification   | string  | 분류       |
| object_number    | string  | 작품 고유번호  |
| diameter         | number  | 지름 (cm)  |
| circumference    | number  | 원둘레 (cm) |
| height           | number  | 높이 (cm)  |
| length           | number  | 길이 (cm)  |
| width            | number  | 너비 (cm)  |
| depth            | number  | 깊이 (cm)  |
| weight           | number  | 무게 (kg)  |
| duration         | number  | 재생시간 (초) |


### artworks_artists

| 컬럼명        | 자료형     | 설명      |
| ---------- | ------- | ------- |
| artwork_id | integer | 작품 ID   |
| artist_id  | integer | 아티스트 ID |
