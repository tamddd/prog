-- アルゴ式 SQL
select st.name as `氏名`, su.name as `科目名`, g.score as `点数`
from students as st
left join grades as g on st.id = g.student_id
left join subjects as su on g.subject_id = su.id
