---Find the inspection date and risk category (pe_description) of facilities named 'STREET CHURROS' that received a score below 95.
select activity_date,
    pe_description
from los_angeles_restaurant_health_inspections
where facility_name = "STREET CHURROS"
    and score < 95