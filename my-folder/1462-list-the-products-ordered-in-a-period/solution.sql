# Write your MySQL query statement below
select p.product_name , SUM(t.unit) as unit from (
    select product_id , unit, order_date from orders having MONTH(order_date)=2 and YEAR(order_date)=2020
) t
left join products p on p.product_id=t.product_id group by t.product_id having SUM(t.unit)>=100;


