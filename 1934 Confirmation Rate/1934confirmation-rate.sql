# Write your MySQL query statement below

with cte as(
select 
 s.user_id,
 SUM(case c.action when 'confirmed' then 1 else 0 end) totalconfirmed,
 SUM(case c.action when 'timeout' then 1 else 0 end) totaltimeout
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id
)
select 
user_id, 
IFNULL(ROUND(totalconfirmed/(totalconfirmed + totaltimeout),2),0) as confirmation_rate 
from cte;