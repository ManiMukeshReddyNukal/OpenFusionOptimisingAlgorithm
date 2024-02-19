# Write your MySQL query statement below
select U.unique_id as unique_id , 
E.name as name from Employees E
left join EmployeeUNI U on U.id=E.id;
