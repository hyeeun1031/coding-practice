# [Basic] Higher Than 75 Marks

[문제 링크](https://www.hackerrank.com/challenges/more-than-75-marks/problem) 

### 구분

Basic > Basic Select (Easy)

### 제출 일자

2025년 08월 28일 02:25

### 문제 설명

Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. 

If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

**Input Format** <br>
The STUDENTS table is described as follows: <br> 
<img width="321" height="191" alt="image" src="https://github.com/user-attachments/assets/6ef5242e-9306-4c67-bd6b-2a28119b33f4" /> <br> 
The Name column only contains uppercase (A-Z) and lowercase (a-z) letters.

**Sample Input** <br> 
<img width="318" height="223" alt="image" src="https://github.com/user-attachments/assets/63005873-107e-4c4d-bde4-2de1a8cd1e5b" />

**Sample Output**
```
Ashley
Julia
Belvet
```

**Explanation** <br> 
Only Ashley, Julia, and Belvet have Marks > 75.

If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.
