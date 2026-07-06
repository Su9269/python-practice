select first_name,
    last_name,
    department,
    salary
from techcorp_workforce
where (
        department = "HR"
        or department = "Admin"
    )
    and salary > 80000Workers With The Highest Salaries