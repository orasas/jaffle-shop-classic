
  {{ config(materialized = 'view', tags = ['staging']) }}

select
  order_id,
  user_id,
  cast(order_time as timestamp) as order_time,
  cast(order_date as date)      as order_date,
  revenue
from {{ source('raw', 'orders') }}
