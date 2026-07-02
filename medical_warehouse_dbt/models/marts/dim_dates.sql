select distinct
    message_date::date as date_day
from {{ ref('stg_telegram_messages') }}
