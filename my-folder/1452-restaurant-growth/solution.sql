WITH cust as (
SELECT c.visited_on,
       SUM(c.amount) OVER (ORDER BY c.visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
       AVG(c.amount) OVER (ORDER BY c.visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount
FROM 
( select visited_on,SUM(amount) as amount from customer group by visited_On) c
ORDER BY c.visited_on
)
select visited_on,amount,ROUND(average_amount,2) as average_amount  from cust 
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM customer)) >= 6
;
