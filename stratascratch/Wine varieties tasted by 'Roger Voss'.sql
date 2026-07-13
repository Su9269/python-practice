---Find wine varieties tasted by 'Roger Voss' and with a value in the 'region_1' column of the dataset. Output unique variety names only.
select distinct variety
from winemag_p2
where taster_name = "Roger Voss"
    and region_1 is not null