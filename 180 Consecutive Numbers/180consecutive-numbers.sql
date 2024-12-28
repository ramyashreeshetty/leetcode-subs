
with cte as(
select
    id,
    num,
    lag(num,1,-999) over(order by id) as pn,
    lead(num,1,-999) over(order by id) as nn
from logs
)
select distinct num as ConsecutiveNums
from cte
where num=pn and num=nn
