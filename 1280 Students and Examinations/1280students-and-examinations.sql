select e.student_id, e.student_name, s.subject_name, COUNT(ex.subject_name) AS attended_exams
from Students e 
cross join Subjects s
left join Examinations ex on e.student_id = ex.student_id and s.subject_name = ex.subject_name
group by e.student_id, e.student_name, s.subject_name
order by e.student_id, s.subject_name;
