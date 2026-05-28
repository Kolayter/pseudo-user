import asyncio
import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(message):
        if message.author == self.bot.user:
            return
        
        if bot.user.mentioned_in(message):
            pass

async def setup(bot):
    await bot.add_cog(Fisherman(bot))