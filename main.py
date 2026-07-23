#!/usr/bin/env python3

import asyncio
from dotenv import load_dotenv
import os
import logging
import discord
from discord.ext import commands

# Just the settings for
from modules.logging_settings import setup_logging
setup_logging()
# My modules
from modules.discord_adapter import DiscordIn, DiscordOut
from modules.core.the_core import TheCore

# Start
# .env stuff
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  

# Disocrd stuff
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# Damn, Discord spams all my console with DEBUG logs, I can't read it. There's the fix:
logging.getLogger('discord').setLevel(logging.INFO)

#Logging stuff
logger = logging.getLogger(__name__)





# The main cycle logic
async def main():
    logger.info(f"psuedo-user started!")

    discord_input_queue = asyncio.Queue()
    discord_output_queue = asyncio.Queue()

    discord_in = DiscordIn(bot=bot, token=DISCORD_TOKEN, input_queue=discord_input_queue)
    discord_out = DiscordOut(bot=bot, output_queue=discord_output_queue)
    the_core = TheCore(discord_input_queue=discord_input_queue, discord_output_queue=discord_output_queue)

    await asyncio.gather(
        discord_in.start(),
        the_core.start(),
        discord_out.start()
    )



 
if __name__ == "__main__":
    # Refactor to a real SAFE closing.
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(f"Psuedo-user stopped by user (KeyboardInterrupt!).")