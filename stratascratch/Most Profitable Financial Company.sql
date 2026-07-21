---Find the most profitable company from the financial sector. Output the result along with the continent.
select company,
    continent
from forbes_global_2010_2014
order by profits desc
limit 1