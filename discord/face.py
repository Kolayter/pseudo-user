import asyncio
import llm
import discord
from discord.ext import commands

async def _write(msg, channel):
    async with channel.typing():
        await channel.send(msg)``