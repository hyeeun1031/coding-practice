SELECT a.artist_id,
       a.name
FROM artists AS a
LEFT JOIN artworks_artists AS aa
  ON a.artist_id = aa.artist_id
WHERE aa.artist_id IS NULL       -- 작품에 참여한 기록이 없는 작가
  AND a.death_year IS NOT NULL;  -- 사망한(살아있지 않은) 작가
