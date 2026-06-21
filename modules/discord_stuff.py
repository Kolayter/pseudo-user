import asyncio
import logging
import discord
from discord.ext import commands
# ===============================

logger = logging.getLogger(__name__)

#  _____________________________
# |=============================|
# >>>         Events          <<<

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class DiscordEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Get messages and send data to the event manager
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return

        logger.info("Detected a new message.")
        await event_manager.emit(
            "raw_message",
            user_id=msg.author.id,
            username=msg.author.name,
            display_name=msg.author.display_name,
            channel=msg.channel,
            message=msg.content
        )

    @commands.Cog.listener()
    async def on_ready(self):
        pass

#  _____________________________
# |=============================|
# >>>      Output stuff       <<<

class DiscordOut:
    def __init__(self, bot, manager):
        self.bot = bot
        self.manager = manager
        self.manager.listen("discord_answer", self.send_to_chat)

    async def send_to_chat(self, msg, channel):
        channel = self.bot.get_channel(channel)
        
        if channel:
            await channel.send(msg)
