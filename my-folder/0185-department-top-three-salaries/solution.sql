select d.name as Department,
t.name as Employee,
t.salary as Salary
from
(SELECT id, name,salary,departmentId,
DENSE_RANK() OVER (partition by departmentId ORDER BY salary DESC) AS `rank`
FROM employee
) t 
left join department d
on t.departmentId=d.id
where `rank`<=3;

