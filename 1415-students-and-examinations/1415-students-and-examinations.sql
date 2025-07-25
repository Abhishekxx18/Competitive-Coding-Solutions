/*
# Write your MySQL query statement below
SELECT s.student_id,s.student_name,su.subject_name,COUNT(e.subject_name) as attended_exams
FROM Students s
CROSS JOIN Subjects su
LEFT JOIN Examinations e 
on s.student_id = e.student_id AND su.subject_name = e.subject_name
GROUP BY s.student_id,s.student_name,su.subject_name
ORDER BY s.student_id,su.subject_name;



*/

SELECT s.student_id,s.student_name,su.subject_name,COUNT(e.subject_name) as attended_exams
FROM students s
CROSS JOIN subjects su
LEFT JOIN Examinations e
ON s.student_id = e.student_id AND su.subject_name = e.subject_name
GROUP BY s.student_id,s.student_name,su.subject_name
ORDER BY s.student_id,su.subject_name;