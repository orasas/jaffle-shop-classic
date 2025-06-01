{{ config(
    materialized = 'incremental',
    unique_key = 'order_id'
) }}

with base as (
  select
    order_id,
    user_id,
    order_date,
    revenue
  from {{ ref('stg_orders') }}
)

select
  order_id,
  user_id,
  order_date,
  revenue
from base

{% if is_incremental() %}
  where order_date > (select max(order_date) from {{ this }})
{% endif %}
