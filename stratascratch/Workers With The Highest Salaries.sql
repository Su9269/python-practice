---Management wants to analyze only employees with official job titles. 
---Find the title(s) of the worker(s) with the highest salary among workers who have a corresponding record in the  title  table. 
---If multiple employees have the same highest salary, include all their job titles.
select t.worker_title as best_paid_title
from worker as w
    join title as t on w.worker_id = t.worker_ref_id
where w.salary =(
        select max(a.salary)
        from worker a
            join title b on a.worker_id = b.worker_ref_id
        where b.worker_title is not null
    )
order by best_paid_title desc