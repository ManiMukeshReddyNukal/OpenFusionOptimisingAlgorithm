# Write your MySQL query statement below
select s.student_Id ,
s.student_name , 
sub.subject_name , 
COALESCE(e.c,0) as attended_exams 
from students s
CROSS JOIN subjects sub
LEFT JOIN (
    select student_id,
            subject_name,
            COUNT(*) as c
    from Examinations
    group by student_id,
             subject_name
) e
on e.student_id=s.student_id 
and e.subject_name=sub.subject_name 
order by s.student_Id,sub.subject_name ;

