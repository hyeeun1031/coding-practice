<img width="242" height="152" alt="1458534973-6548194998-ScreenShot2016-03-21at8 50 21AM" src="https://github.com/user-attachments/assets/005ccb86-a4ed-4515-821c-a6eb1904ebf6" /># [Advanced] New Companies

[문제 링크](https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true) 

### 구분

Advanced > Advanced Select (Medium)

### 제출 일자

2025년 08월 22일 02:15

### 문제 설명

Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:

<img width="113" height="199" alt="image" src="https://github.com/user-attachments/assets/69b03a8d-c4dd-4724-93da-5d6fce4b1902" />

Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

**Note:**

- The tables may contain duplicate records.
- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.

**Input Format**

The following tables contain company data:

- Company: The company_code is the code of the company and founder is the founder of the company.
<img width="196" height="117" alt="image" src="https://github.com/user-attachments/assets/4143a826-d225-4a78-8270-2e1d8f4d1497" />

- Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.
<img width="230" height="119" alt="1458534960-2c6d764e3c-ScreenShot2016-03-21at8 50 12AM" src="https://github.com/user-attachments/assets/c4d79951-f3ed-41b5-b5b8-3754448b1793" />

- Senior_Manager: The senior_manager_code is the code of the senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
<img width="242" height="152" alt="1458534973-6548194998-ScreenShot2016-03-21at8 50 21AM" src="https://github.com/user-attachments/assets/2a471fd1-124e-48e1-9875-9bdfafea0bf2" />

- Manager: The manager_code is the code of the manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
<img width="243" height="190" alt="1458534988-7fc0af46ce-ScreenShot2016-03-21at8 50 29AM" src="https://github.com/user-attachments/assets/e91d4441-24d9-4535-a184-680b3589b37a" />

- Employee: The employee_code is the code of the employee, the manager_code is the code of its manager, the senior_manager_code is the code of its senior manager, the lead_manager_code is the code of its lead manager, and the company_code is the code of the working company.
<img width="242" height="223" alt="1458535002-d47f63cbb4-ScreenShot2016-03-21at8 50 41AM" src="https://github.com/user-attachments/assets/a0baf068-e4d4-4ace-b826-845a436648a1" />

**Sample Input**
Company Table:
<img width="232" height="117" alt="1458535049-2a207c44b3-ScreenShot2016-03-21at8 50 52AM" src="https://github.com/user-attachments/assets/7cabe372-86d7-464f-9ae6-59955a356a74" />

Lead_Manager Table:
<img width="299" height="116" alt="1458535073-919107f639-ScreenShot2016-03-21at8 51 03AM" src="https://github.com/user-attachments/assets/63926b3b-3a83-4464-a768-86120fa7d5c2" />

Senior_Manager Table:
<img width="478" height="152" alt="1458535111-b1c48335b3-ScreenShot2016-03-21at8 51 15AM" src="https://github.com/user-attachments/assets/b6990281-edc8-4cdc-ac8d-b39df5090266" />

Manager Table: 
<img width="604" height="152" alt="1458535122-888f4bf340-ScreenShot2016-03-21at8 51 26AM" src="https://github.com/user-attachments/assets/f1d956bd-30ce-4e3a-910d-541f8d77f995" />

Employee Table:
<img width="738" height="187" alt="1458535134-878767e0d9-ScreenShot2016-03-21at8 51 52AM" src="https://github.com/user-attachments/assets/d9e1c480-e4d3-4c8b-adca-3ca97ec6d391" />


**Sample Output**
```
C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
```

**Explanation**
In company C1, the only lead manager is LM1. There are two senior managers, SM1 and SM2, under LM1. There is one manager, M1, under senior manager SM1. There are two employees, E1 and E2, under manager M1.

In company C2, the only lead manager is LM2. There is one senior manager, SM3, under LM2. There are two managers, M2 and M3, under senior manager SM3. There is one employee, E3, under manager M2, and another employee, E4, under manager, M3.
