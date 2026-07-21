import asyncio
import logging
import discord
from discord.ext import commands

from modules.dataclasses import MessageIn, MessageOut
# ===============================

logger = logging.getLogger(__name__)

#  _____________________________
# |=============================|
# >>>         Events          <<<

class DiscordIn:
    def __init__(self, bot: commands.Bot, token, input_queue) -> None:   
        self.bot = bot
        self.token = token
        self.input_queue = input_queue
    
        self._register_discord_events()

    def _register_discord_events(self) -> None:

        @self.bot.event
        async def on_ready():
            logger.info("Discord bot started successfully!")

        # Get messages and send data to the event manager
        @self.bot.event
        async def on_message(msg):
            if msg.author == self.bot.user:
                return

            logger.info(f"Detected a new message in \'{msg.channel}\'.")
            await self.input_queue.put(MessageIn(
                platform=DISCORD,
                message_id=msg.id,
                text=msg.content,
                channel_id=msg.channel.id,
                author_id=msg.author.id

            ))
    
    async def start(self):
        logger.info("Starting the bot...")
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
        self.output_queue = output_queue

    async def start(self):
        logger.info("DiscordOut object has started.")

        queue_gotten = await self.output_queue.get()
        self.output_queue.task_done()

        while True:
            pass
