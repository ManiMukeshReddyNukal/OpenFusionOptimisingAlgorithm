# Write your MySQL query statement below
select W1.id from Weather W1, Weather w
WHERE DATEDIFF(W1.recordDate,w.recordDate)=1 and W1.temperature>w.temperature;
