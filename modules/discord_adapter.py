import asyncio
import logging
import discord
from discord.ext import commands

from modules.parser import CommonMessage
# ===============================

logger = logging.getLogger(__name__)

#  _____________________________
# |=============================|
# >>>         Events          <<<

class DiscordIn:
    def __init__(self, bot: commands.Bot, token, input_queue):
        self.bot = bot
        self.token = token
        self.queue = input_queue
    
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

            logger.info(f"Detected a new message in \'{msg.channel}\'.")
            await self.queue.put(CommonMessage(
                platform="Discord",
                message_id=msg.id,
                text=msg.content,
                channel_id=msg.channel.id,
                author_id=msg.author.id

            ))
    
    async def start(self):
        logger.info("The bot has started.")
        await self.bot.start(self.token)
    
    async def stop(self):
        logger.info("Stopping the bot.")
        await self.bot.close()


#  _____________________________
# |=============================|
# >>>      Output stuff       <<<

class DiscordOut:
    def __init__(self, bot, output_queue):
        self.bot = bot

