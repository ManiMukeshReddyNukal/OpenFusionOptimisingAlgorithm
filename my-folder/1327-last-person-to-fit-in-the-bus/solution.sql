# Write your MySQL query statement below
select T.person_name
from ( 
    select person_name, 
turn,
sum(weight) over (order by turn) as bus_weight
from Queue 
order by turn
) T
where T.bus_weight<=1000 
order by T.bus_weight DESC
limit 1 ;
