#Language: MySQL
SELECT s.hacker_id, h.name
FROM Submissions AS s
JOIN Challenges AS c ON s.challenge_id = c.challenge_id
JOIN Difficulty AS d on c.difficulty_level = d.difficulty_level
JOIN Hackers AS h on s.hacker_id = h.hacker_id
WHERE s.score = d.score
GROUP BY s.hacker_id, h.name
HAVING COUNT(DISTINCT s.challenge_id) > 1
ORDER BY COUNT(DISTINCT s.challenge_id) DESC, s.hacker_id ASC;
