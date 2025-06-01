{{
  config(
    materialized = 'view',
    tags = ['staging']
  )
}}

select
  id               as event_id,
  user_id,
  event_name,
  cast(event_time as timestamp)   as event_time,
  cast(event_date as date)        as event_date
from {{ source('raw', 'events') }}
where event_name in ('page_view','signup','purchase')
