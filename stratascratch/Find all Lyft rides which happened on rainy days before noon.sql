---Find all Lyft rides which happened on rainy days before noon
select *
from lyft_rides
where weather = "rainy"
    and hour < 12