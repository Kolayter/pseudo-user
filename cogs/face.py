import asyncio
import llm
import discord
from discord.ext import commands

class Face(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def send_msg(self, channel, text: str):
        async with channel.typing():
            pass
        await channel.send(msg)

async def setup(bot):
    await bot.add_cog(Face(bot))