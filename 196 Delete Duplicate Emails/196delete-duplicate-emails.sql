-- Write your PostgreSQL query statement below

-- delete from person
-- where id in (
-- select id from (
-- select id, row_number() over(partition by email order by id) as rn
-- from person
-- ) where rn > 1
-- )

DELETE FROM PERSON WHERE ID NOT IN (SELECT MIN(ID) FROM PERSON GROUP BY EMAIL);