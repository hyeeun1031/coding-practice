# [Basic] Weather Observation Station 5

[문제 링크](https://www.hackerrank.com/challenges/weather-observation-station-5/problem) 

### 구분

Basic > Basic Select (Easy)

### 제출 일자

2025년 08월 28일 02:20

### 문제 설명

Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

The STATION table is described as follows:

<img width="300" height="290" alt="image" src="https://github.com/user-attachments/assets/1de3454c-60ad-420e-b55f-ec341346df07" />

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Sample Input** <br>
For example, CITY has four entries: DEF, ABC, PQRS and WXY.

**Sample Output**
```
ABC 3
PQRS 4
```

**Explanation** <br>
When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . 
The longest name is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.

**Note** <br>
You can write two separate queries to get the desired output. It need not be a single query.
