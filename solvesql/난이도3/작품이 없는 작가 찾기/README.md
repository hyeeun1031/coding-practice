# 작품이 없는 작가 찾기

Museum of Modern Art Collection 데이터베이스는 미국 뉴욕의 근현대 미술관인 MoMA의 작품과 작가 정보를 담고 있습니다. <br>
artists 테이블에는 MoMA에 등록된 작가들의 정보가 있고, artworks_artists 테이블에는 각 작품에 참여한 작가들의 정보가 들어있습니다. <br>
하나의 작품에 여러 명의 작가가 참여할 수 있기 때문에, artworks_artists 테이블의 artwork_id 컬럼과 artist_id 컬럼은 N:M 관계입니다. <br>

MoMA에 등록된 작가이지만 전시된 작품이 없는 작가들의 마지막 작품을 전시하는 기획전을 준비하려 합니다. <br>
MoMA에 등록되어있고, 현재 살아있지 않은 작가 중 MoMA에 등록된 작품이 없는 작가의 ID와 이름을 출력하는 쿼리를 작성해주세요. <br>
쿼리 결과에는 아래 컬럼이 있어야 합니다. <br>

- artist_id - 작가 ID
- name - 작가 이름

### artists 테이블
| 컬럼명 | 데이터 타입 | 설명 |
|--------|--------------|------|
| artist_id | integer | 아티스트 ID |
| name | string | 아티스트 이름 |
| nationality | string | 국적 |
| gender | string | 성별 |
| birth_year | integer | 출생연도 |
| death_year | integer | 사망연도 |

### artworks 테이블
| 컬럼명 | 데이터 타입 | 설명 |
|--------|--------------|------|
| artwork_id | integer | 작품 ID |
| title | string | 제목 |
| date | string | 작품 완성연도 |
| medium | string | 재료 |
| dimensions | string | 크기 |
| acquisition_date | date | 소장 일시 |
| credit | string | 소장 경로 |
| catalogue | boolean | 카탈로그 유무 |
| department | string | 담당 부서 |
| classification | string | 분류 |
| object_number | string | 작품 고유번호 |
| diameter | number | 지름 (cm) |
| circumference | number | 원둘레 (cm) |
| height | number | 높이 (cm) |
| length | number | 길이 (cm) |
| width | number | 너비 (cm) |
| depth | number | 깊이 (cm) |
| weight | number | 무게 (kg) |
| duration | number | 재생시간 (초) |

### artworks_artists 테이블
| 컬럼명 | 데이터 타입 | 설명 |
|--------|--------------|------|
| artwork_id | integer | 작품 ID |
| artist_id | integer | 아티스트 ID |
