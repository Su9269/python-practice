---Write a query that returns the number of unique users per client for each month. 
---Assume all events occur within the same year, so only month needs to be be in the output as a number from 1 to 12.
select client_id,
    month(time_id) as month,
    count(distinct user_id) as users_num
from fact_events
group by client_id,
    month(time_id)
order by client_id