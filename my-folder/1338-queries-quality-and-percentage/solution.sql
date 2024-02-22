# Write your MySQL query statement below
select query_name,
ROUND(AVG(rating/position),2) as quality,
ROUND(SUM(IF(rating<3,1,0))*100/COUNT(*),2) as poor_query_percentage 
from Queries 
WHERE query_name is not Null
 group by query_name;
