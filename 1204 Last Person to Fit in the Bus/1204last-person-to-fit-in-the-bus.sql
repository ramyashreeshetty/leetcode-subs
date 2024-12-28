-- Write your PostgreSQL query statement below
with cte as(
select *
from(
    select
        turn,
        person_id as ID,
        person_name as Name,
        weight as Weight,
        sum(weight) over(order by turn) as Total_Weight
    from queue
)
where total_weight <= 1000
)
select name as person_name
from cte
where total_weight in (select max(total_weight) from cte)