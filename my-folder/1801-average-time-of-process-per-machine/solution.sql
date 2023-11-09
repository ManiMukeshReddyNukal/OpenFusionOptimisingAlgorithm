# Write your MySQL query statement below
with process_times as (
    select start.machine_id, start.process_id, (end.timestamp- start.timestamp) as process_time
    from Activity start
    inner join Activity end
    on start.machine_id = end.machine_id
    and start.process_id = end.process_id
    and start.activity_type = 'start'
    and end.activity_type = 'end'
)
select machine_id, round(avg(process_time),3) as processing_time
from process_times 
group by machine_id

