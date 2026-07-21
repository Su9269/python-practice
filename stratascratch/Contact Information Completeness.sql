---The data quality team is auditing employee records to assess the completeness of contact information. 
--Calculate and return the ratio of employees who have a NULL phone number.
select 1 -(count(phone_number) / count(id)) as null_phone_ratio
from techcorp_workforce