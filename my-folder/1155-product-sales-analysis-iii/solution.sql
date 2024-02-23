# Write your MySQL query statement below
select product_id,
year as first_year ,
 quantity,
 price 
 from sales
where (product_id,year) in 
(
select p.product_id,
min(s.year) as year
from product p
left join sales s
on s.product_id=p.product_id
where year is not null
group by product_id
); 




