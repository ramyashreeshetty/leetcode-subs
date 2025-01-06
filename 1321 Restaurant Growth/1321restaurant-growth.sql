-- Write your PostgreSQL query statement below
with daysum as(
select 
    visited_on,
    sum(amount) as amount
from customer 
group by 1
)
select
    a.visited_on,
    sum(b.amount) as amount,
    round(avg(b.amount),2) as average_amount
from daysum a, daysum b
where b.visited_on BETWEEN a.visited_on - 6 AND a.visited_on
group by 1
order by 1
offset 6
