select a1.person_name
from Queue a1
join Queue a2 on a1.turn >= a2.turn
group by a1.turn
having sum(a2.weight) <= 1000
order by sum((a2.weight)) desc
limit 1

