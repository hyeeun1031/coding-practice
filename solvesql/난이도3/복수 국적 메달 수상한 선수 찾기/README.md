# 복수 국적 메달 수상한 선수 찾기

역대 올림픽 정보 데이터베이스는 역대 올림픽 경기와 관련된 데이터가 들어있는 테이블로 이루어져 있습니다.

athletes 테이블에는 역대 올림픽 참가 선수의 이름이 들어 있습니다. <br>
events 테이블에는 종목과 경기 이름이 들어 있습니다. <br>
games 테이블에는 올림픽 개최 연도, 개최 도시와 시즌 정보가 기록되어 있습니다. <br> 
records 테이블에는 역대 올림픽 참가 선수들의 신체 정보와 획득한 메달 정보가 기록되어 있습니다. <br> 
이 테이블은 다른 테이블과 매핑할 수 있는 ID 정보도 가지고 있습니다. <br>
teams 테이블에는 국가 정보가 기록되어 있습니다. <br>

2000년 이후의 메달 수상 기록만 고려했을 때, 메달을 수상한 올림픽 참가 선수 중 2개 이상의 국적으로 메달을 수상한 기록이 있는 선수의 이름을 조회하는 쿼리를 작성해주세요.
조회된 선수의 이름은 오름차순으로 정렬되어 있어야 합니다.

예를 들어, Viktor An 선수는 2006년 토리노에서 열린 동계 올림픽과 2014년 소치에서 열린 동계 올림픽에서 메달을 수상했는데, 2006년에는 대한민국(KOR) 국적으로 메달을 수상했고 2014년에는 러시아(RUS) 국적으로 메달을 수상했습니다.

1. athletes (선수 정보)
| 컬럼명  | 타입      | 설명    |
| ---- | ------- | ----- |
| id   | integer | 선수 ID |
| name | string  | 선수 이름 |

2. events (경기 정보)
| 컬럼명   | 타입      | 설명    |
| ----- | ------- | ----- |
| id    | integer | 경기 ID |
| sport | string  | 종목 이름 |
| event | string  | 경기 이름 |

3. games (올림픽 대회 정보)
| 컬럼명    | 타입      | 설명                    |
| ------ | ------- | --------------------- |
| id     | integer | 올림픽 게임 ID             |
| year   | integer | 개최 연도                 |
| season | string  | 시즌 (예: Summer/Winter) |
| city   | string  | 개최 도시                 |

4. records (선수 출전 기록)
| 컬럼명        | 타입      | 설명                               |
| ---------- | ------- | -------------------------------- |
| id         | integer | 기록 ID                            |
| athlete_id | integer | 선수 ID (FK → athletes.id)         |
| sex        | string  | 성별 (M/F)                         |
| age        | integer | 출전 당시 나이                         |
| weight     | number  | 출전 당시 몸무게 (kg)                   |
| height     | number  | 출전 당시 키 (cm)                     |
| game_id    | integer | 출전 올림픽 게임 ID (FK → games.id)     |
| team_id    | integer | 팀 ID (FK → teams.id)             |
| event_id   | integer | 출전 경기 ID (FK → events.id)        |
| medal      | string  | 메달 (Gold/Silver/Bronze, NULL 가능) |

5. teams (팀/국가 정보)
| 컬럼명  | 타입      | 설명         |
| ---- | ------- | ---------- |
| id   | integer | 팀 ID       |
| team | string  | 팀 이름 (국가명) |
