# [Basic] The Report

[문제 링크](https://www.hackerrank.com/challenges/select-all-sql/problem?isFullScreen=true) 

### 구분

Basic > Basic Join (Medium)

### 제출 일자

2025년 08월 23일 01:49

### 문제 설명

You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.

<img width="313" height="181" alt="image" src="https://github.com/user-attachments/assets/cc1d6ee5-0d93-4f22-844e-b66564801d26" />

Grades contains the following data:

<img width="317" height="470" alt="image" src="https://github.com/user-attachments/assets/13cb65e4-3bec-4a2f-afbc-25911b3db3a3" />

Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Write a query to help Eve.

**Sample Input**

<img width="313" height="302" alt="image" src="https://github.com/user-attachments/assets/00454a9e-3377-47c7-aec9-b32b13bdf572" />

**Sample Output**

```
Maria 10 99
Jane 9 81
Julia 9 88 
Scarlet 8 78
NULL 7 63
NULL 7 68
```

**Note**
Print "NULL"  as the name if the grade is less than 8.

**Explanation**
Consider the following table with the grades assigned to the students:

<img width="314" height="304" alt="image" src="https://github.com/user-attachments/assets/76a7d66f-01ed-4bf9-8b53-8e179fd571cf" />

So, the following students got 8, 9 or 10 grades:

- Maria (grade 10)
- Jane (grade 9)
- Julia (grade 9)
- Scarlet (grade 8)
