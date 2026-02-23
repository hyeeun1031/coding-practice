SELECT ar.name AS artist,
       aw.title AS title
FROM artists ar
JOIN artworks_artists aa
  ON ar.artist_id = aa.artist_id
JOIN artworks aw
  ON aa.artwork_id = aw.artwork_id
WHERE ar.nationality = 'Korean'
  AND aw.classification LIKE 'Film%';
