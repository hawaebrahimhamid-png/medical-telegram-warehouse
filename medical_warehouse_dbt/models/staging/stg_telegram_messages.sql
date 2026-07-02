select
    message_id,
    channel_name,
    cast(message_date as timestamp) as message_date,
    message_text,
    views as view_count,
    forwards as forward_count,
    length(message_text) as message_length,

    case
        when image_path is not null then true
        else false
    end as has_image

from raw.telegram_messages

where message_text is not null
