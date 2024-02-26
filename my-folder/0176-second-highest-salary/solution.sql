# Write your MySQL query statement below
select t.salary as SecondHighestSalary
 from (
     (select salary, DENSE_RANK() over(order by salary desc) as ra
     from employee)
     union all
     ( select null as salary, 2 as ra limit 1 )
     ) t 
where t.ra=2 order by salary desc limit 1;

