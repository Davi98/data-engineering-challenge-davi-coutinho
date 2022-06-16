select distinct
   region 
from
   `streamingsdata.challenge.trips` 
where
   datasource = "cheap_mobile"