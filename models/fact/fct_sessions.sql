{{ config(
    materialized = 'incremental',
    unique_key = 'session_id'
) }}

with sessions as (
  select
    user_id,
    event_date,
    countif(event_name = 'page_view')   as page_views,
    countif(event_name = 'signup')      as signups,
    countif(event_name = 'purchase')    as purchases
  from {{ ref('stg_events') }}
  group by user_id, event_date
)

select
  md5(concat(cast(user_id as string), cast(event_date as string))) as session_id,
  user_id,
  event_date,
  page_views,
  signups,
  purchases
from sessions

{% if is_incremental() %}
  where event_date > (select max(event_date) from {{ this }})
{% endif %}
