# 언더스코어(_)가 포함되지 않은 데이터 찾기

데이터리안 블로그 GA 로그 (2022년 1월) 데이터베이스는 2022년 1월 데이터리안 웹사이트에서 Google Analytics 4 (GA4)를 이용해 수집한 사용자 행동 데이터입니다.

ga 테이블의 page_location 컬럼은 페이지 뷰, 클릭, 스크롤 등의 사용자 행동이 수집된 페이지 경로를 담고 있습니다. <br>
page_location 컬럼의 값이 언더스코어('_')를 포함하지 않는 경우만 출력하는 쿼리를 작성해주세요. <br>
쿼리 결과에는 page_location 컬럼만 있어야 하고, 중복되는 값은 1번만 나와야 하며 오름차순으로 정렬되어 있어야 합니다.

| Column              | Type      | Description                  |
|---------------------|-----------|------------------------------|
| event_timestamp_kst | datetime  | 이벤트 시각 (KST)            |
| user_pseudo_id      | string    | 사용자의 가명처리된 ID       |
| ga_session_id       | string    | GA 세션 ID                   |
| event_name          | string    | 이벤트 이름                  |
| page_location       | string    | 이벤트가 발생한 페이지 경로  |
| page_title          | string    | 이벤트가 발생한 페이지 제목  |
| source              | string    | 사용자를 획득한 트래픽 소스  |
| medium              | string    | 사용자를 획득한 트래픽 매체  |
| continent           | string    | 이벤트가 보고된 대륙         |
| country             | string    | 이벤트가 보고된 국가         |
| device_category     | string    | 사용자가 사용한 기기 종류    |
