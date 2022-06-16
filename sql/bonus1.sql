with top2 as 
(
   select
      count(*) as count,
      region 
   from
      `streamingsdata.challenge.trips` 
   group by
      region 
   order by
      count desc limit 2 
)
select
   sct.datetime,
   sct.datasource 
from
   `streamingsdata.challenge.trips` sct 
   inner join
      top2 
      on sct.region = top2.region 
order by
   sct.datetime desc limit 1