# Write your MySQL query statement below 
# 


#select customer_id,SUM(if(Min(order_date)= customer_pref_delivery_date,1,0)),SUM(1) from Delivery group by customer_id;

#select customer_id,SUM(if(Min(order_date)= customer_pref_delivery_date,1,0)) as a,SUM(1) as b from Delivery group by customer_id;

#select delivery_id,Min(order_date) as a,SUM(1) as b from Delivery group by customer_id;
select round((sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)/ sum(1) *100) ,2) as immediate_percentage
from delivery
where (customer_id, order_date) in (select customer_id, min(order_date) as order_date 
from Delivery
group by customer_id);




