import asyncio
import logging
import discord
from discord.ext import commands
# ===============================

logger = logging.getLogger(__name__)

#  _____________________________
# |=============================|
# >>>         Events          <<<

class DiscordEvents:
    def __init__(self, bot: commands.Bot, event_manager):
        self.bot = bot
        self.manager = event_manager
    
        self._register_discord_events()

    def _register_discord_events(self):

        @self.bot.event
        async def on_ready():
            logger.info(f"Discord bot started sucses succesful!")

        # Get messages and send data to the event manager
        @self.bot.event
        async def on_message(msg):
            if msg.author == self.bot.user:
                return

            logger.info(f"Detected a new message in {msg.channel}")
            await self.manager.emit(
                "raw_message",
                user_id=msg.author.id,
                username=msg.author.name,
                display_name=msg.author.display_name,
                channel=msg.channel,
                message=msg.content
            )


#  _____________________________
# |=============================|
# >>>      Output stuff       <<<

class DiscordOut:
    def __init__(self, bot, event_manager):
        self.bot = bot
        self.manager = event_manager
        self.manager.listen("discord_answer", self.send_to_chat)

    async def send_to_chat(self, msg, written_channel):
        channel = self.bot.get_channel(written_channel)
        
        if channel:
            await channel.send(msg)
