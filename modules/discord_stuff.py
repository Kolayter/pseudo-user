import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class DiscordEvents(commands.Cog):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return

        """
        - короче, я закидываю сюда функцию от парсера и преобразовываю данные.
        - Дальше мне нужно закинуть данные в очередь моих ивентов.
        """

        await event_manager.emit(
            "raw_message",
            user_id=msg.author.id,
            username=msg.author.name,
            display_name=msg.author.display_name,
            channel=msg.channel,
            message=msg.content
        )

# ===============================

class DiscordOut:
    def __init__(self, bot, manager):
        self.bot = bot
        self.manager = manager
        self.manager.listen("discord_answer", self.send_to_chat)

    async def send_to_chat(self, msg, channel):
        channel = self.bot.get_channel(channel)
        
        if channel:
            await channel.send(msg)
