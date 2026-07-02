select
    message_id,
    channel_name,
    message_date,
    message_text,
    view_count,
    forward_count,
    message_length,
    has_image
from {{ ref('stg_telegram_messages') }}

