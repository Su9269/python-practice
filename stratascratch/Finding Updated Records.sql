SELECT id,
    first_name,
    last_name,
    department_id,
    salary
FROM (
        select *,
            ROW_NUMBER() OVER (
                PARTITION BY id
                ORDER BY salary DESC,
                    department_id DESC
            ) as rn
        from ms_employee_salary
    ) s
where rn = 1
order by id asc