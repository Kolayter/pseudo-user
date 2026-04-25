import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

# --- My modules ---
import llm

# Load variables from .evn
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#Discord settings
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


# _____________________________
# The code

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        async with message.channel.typing():
            answer = await asyncio.to_thread(llm.TextToAI, [{'role': 'user', 'content': message.content}])
            await message.channel.send(answer)

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)