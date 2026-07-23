# modules/dataclasses.py
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum, auto


class Platform(Enum):
    DISCORD = auto()
    TELEGRAM = auto()


@dataclass
class MessageIn:
    platform: Platform
    message_id: int
    text: str
    channel_id: int
    author_id: int

    reply_to: Optional[ReplyInfo] = None

@dataclass
class MessageOut:
    platform: Platform
    text: str
    channel_id: int

    reply_to: Optional[ReplyInfo] = None

