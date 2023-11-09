# Write your MySQL query statement below
select id, movie, description, rating
from Cinema
where Cinema.id % 2 = 1 and Cinema.description != 'boring'
order by rating desc;
