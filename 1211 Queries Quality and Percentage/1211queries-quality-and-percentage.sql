# Write your MySQL query statement below
select distinct query_name,
ROUND(sum(rating/position)/(select count(*) from queries q where q.query_name=q1.query_name),2) as quality,
ROUND(((select count(r.rating) from queries r where r.query_name=q1.query_name and r.rating<3)/(select count(*) from queries s where s.query_name=q1.query_name))*100,2) as poor_query_percentage
from  queries q1
where q1.query_name is not null
group by q1.query_name