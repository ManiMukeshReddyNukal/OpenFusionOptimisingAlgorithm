# Write your MySQL query statement below
select P.product_name, S.year,S.price as price 
from Sales S
LEFT JOIN Product P 
ON S.product_id=P.product_id;
