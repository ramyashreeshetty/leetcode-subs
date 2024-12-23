-- Write your PostgreSQL query statement below
with temp as
(
select 
    player_id, 
    min(event_date) as min_date
from activity
group by player_id
)
select 
round(sum(case when temp.min_date + 1 = a.event_date then 1 else 0 end)*1.0/count(distinct temp.player_id), 2) as fraction
from temp
join activity a
on temp.player_id = a.player_id