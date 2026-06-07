#region not main stuff
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

# --------- My modules ----------
import llm
import discord.fisherman
import discord.face
# -------------------------------

#region Load variables from .evn
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

#Discord settings
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)
#endregion

#endregion
# _______________________________
# The code

bot.run(DISCORD_TOKEN)