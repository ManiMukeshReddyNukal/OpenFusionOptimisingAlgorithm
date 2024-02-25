# Write your MySQL query statement below
(
    select u.name AS results
from movierating m
left join users u
on m.user_id=u.user_id
group by m.user_id
order by count(*) desc, u.name limit 1
)
UNION ALL
( 
    select title as results from 
movies m 
left join (
    select movie_id,AVG(rating) as avg_rating from movierating
    where MONTH(created_at)=2 AND YEAR(created_at)=2020
    group by movie_id
) t
on m.movie_id=t.movie_id 
order by avg_rating desc, title limit 1
);
