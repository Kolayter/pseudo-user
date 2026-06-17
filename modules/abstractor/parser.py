from dataclasses import dataclass

# Хрен его знает, зачем мне он будет нужен.
# Если в будущем будет нужна подобная организация, тогда буду использовать это.


# Список ивентов которые я получаю. Тут описаны в классах их данные
# которые я собираю и буду работать.
@dataclass
class OnMessage:
    event_name: str
    user_id: int
    username: str
    display_name: str
    channel: Channel
    message: str

def parse_OnMessage(message):
    return OnMessage(
        event_name="raw_message",
        user_id=message.author.id,
        username=message.author.name,
        display_name=message.author.display_name,
        channel=message.channel,
        message=message.content
    )

"""
Условно тут дальше будут остальные функции для для ивентов.
"""
