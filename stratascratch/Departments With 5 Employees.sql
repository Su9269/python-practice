---Find departments with at more than or equal 5 employees.
select employee_title as department
from employee
group by employee_title
having count(employee_title) >= 5