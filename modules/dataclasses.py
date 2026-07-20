# Пока нигде не используется!

from dataclasses import dataclass, field
from typing import Optional, List

# Хрен его знает, зачем мне он будет нужен.
# Если в будущем будет нужна подобная организация, тогда буду использовать это.


# Список ивентов которые я получаю. Тут описаны в классах их данные
# которые я собираю и буду работать.
@dataclass
class CommonMessage:
    platform: str
    message_id: int
    text: str
    channel_id: int
    author_id: int

    reply_to: Optional[ReplyInfo] = None



# def parse_OnMessage(message):
#     return OnMessage(
#         event_name="raw_message",
#         user_id=message.author.id,
#             username=message.author.name`,
#             display_name=message.author.d`isplay_name,
#         channel=message.channel,
#         message=message.content
#     )
