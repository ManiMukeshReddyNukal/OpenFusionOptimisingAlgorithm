# Write your MySQL query statement below
-- select count(DISTINCT A1.player_id) / (select count(DISTINCT player_id) from Activity) as fraction
select ROUND( COUNT(DISTINCT A1.player_id)/(select count(DISTINCT player_id) from Activity) ,2) as fraction
from Activity A1 
join (select player_id,MIN(event_date) as event_date from Activity group by player_id) A2
ON A1.player_id=A2.player_id and DATEDIFF(A1.event_date,A2.event_date)=1;  


-- SELECT 
--     ROUND(
--         COUNT(DISTINCT A1.player_id) / 
--         (SELECT COUNT(DISTINCT player_id) FROM Activity), 
--         2
--     ) AS fraction
-- FROM 
--     Activity A1
-- JOIN 
--     (SELECT player_id, MIN(event_date) AS event_date FROM Activity GROUP BY player_id) A2
-- ON 
--     A1.player_id = A2.player_id AND DATEDIFF(A1.event_date, A2.event_date) = 1;

