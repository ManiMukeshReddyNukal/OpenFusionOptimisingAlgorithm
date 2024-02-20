# Write your MySQL query statement below
select a1.machine_id as machine_id, 
round(avg(a2.timestamp-a1.timestamp),3) as processing_time
from Activity a1 
left join 
Activity a2 
ON a1.machine_id=a2.machine_id 
where a1.activity_type='start'
and a2.activity_type='end'
GROUP BY machine_id;
