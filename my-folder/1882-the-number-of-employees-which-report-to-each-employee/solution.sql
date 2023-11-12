# Write your MySQL query statement below
select a1.employee_id, a1.name, count(a2.reports_to) as reports_count, round(avg(a2.age*1.00),0) as average_age
from Employees a1
join Employees a2
on a1.employee_id = a2.reports_to
group by employee_id,a1.name
order by a1.employee_id;
