---Find the hour with the highest gasoline cost. Assume there's only 1 hour with the highest gas cost.
select hour
from lyft_rides
order by gasoline_cost desc
limit 1