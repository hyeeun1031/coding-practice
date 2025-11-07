SELECT
    mentee.employee_id AS mentee_id,
    mentee.name AS mentee_name,
    mentor.employee_id AS mentor_id,
    mentor.name AS mentor_name
FROM employees AS mentee
LEFT JOIN employees AS mentor
    ON mentor.department <> mentee.department
   AND mentor.join_date <= '2019-12-31'    -- 멘토: 2년 이상 근무
WHERE mentee.join_date >= '2021-10-01'     -- 멘티: 3개월 이내 입사
ORDER BY mentee.employee_id, mentor.employee_id;
