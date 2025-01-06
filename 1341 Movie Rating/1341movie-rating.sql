(
with tot_rate as (
select user_id, count(*) as rate
from MovieRating
group by 1
)
select name as results
from tot_rate tr
join users u
on tr.user_id = u.user_id
order by rate desc, name
limit 1
)
union all
(
with avg_rate as (
select movie_id, avg(rating) as rate
from MovieRating
where created_at::varchar like '2020-02%'
group by 1
)
select title as results
from avg_rate ar
join movies m
on ar.movie_id = m.movie_id
order by rate desc, title
limit 1
)