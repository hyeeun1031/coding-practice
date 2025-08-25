# [Advanced] Top Competitors

[문제 링크](https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true) 

### 구분

Advanced > Basic Join (Medium)

### 제출 일자

2025년 08월 26일 02:41

### 문제 설명

Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

**Input Format**
The following tables contain contest data:

- Hackers: The hacker_id is the id of the hacker, and name is the name of the hacker. 
<img width="169" height="117" alt="image" src="https://github.com/user-attachments/assets/024167c7-0c9c-4dfc-af85-7cae4ffed09e" />

- Difficulty: The difficult_level is the level of difficulty of the challenge, and score is the maximum score that can be achieved for a challenge at that difficulty level.
<img width="196" height="121" alt="image" src="https://github.com/user-attachments/assets/52557ebe-75d8-4fdd-9dc0-cf81fe8a4e38" />

- Challenges: The challenge_id is the id of the challenge, the hacker_id is the id of the hacker who created the challenge, and difficulty_level is the level of difficulty of the challenge.
<img width="194" height="152" alt="image" src="https://github.com/user-attachments/assets/3a16de4f-6131-44f9-b413-5038d9ec6c2e" />

- Submissions: The submission_id is the id of the submission, hacker_id is the id of the hacker who made the submission, challenge_id is the id of the challenge that the submission belongs to, and score is the score of the submission.
<img width="196" height="187" alt="image" src="https://github.com/user-attachments/assets/9b793693-36ce-43de-8d6c-5e925385df1a" />

**Sample Input**
<br>
- Hacekrs Table:
<img width="185" height="402" alt="image" src="https://github.com/user-attachments/assets/35c675f4-0a98-419a-8088-f83d27e6b3f6" />

- Difficulty Table:
<img width="199" height="295" alt="image" src="https://github.com/user-attachments/assets/ab6dcce2-ddf4-4afb-a2f7-93ca67a2b872" />

- Challenges Table:
<img width="342" height="223" alt="image" src="https://github.com/user-attachments/assets/e87fb02f-d099-46c6-92f3-d5429dd84331" />

- Submissions Table:
<img width="408" height="784" alt="image" src="https://github.com/user-attachments/assets/0048b715-43b2-4693-9066-351c66d84f3c" />

**Sample Output**
```
90411 Joe
```

**Explanation**

Hacker 86870 got a score of 30 for challenge 71055 with a difficulty level of 2, so 86870 earned a full score for this challenge.

Hacker 90411 got a score of 30 for challenge 71055 with a difficulty level of 2, so 90411 earned a full score for this challenge.

Hacker 90411 got a score of 100 for challenge 66730 with a difficulty level of 6, so 90411 earned a full score for this challenge.

Only hacker 90411 managed to earn a full score for more than one challenge, so we print the their hacker_id and name as  space-separated values.

