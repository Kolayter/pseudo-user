import asyncio
from dotenv import load_dotenv
import os
import logging
import discord
from discord.ext import commands

# >>>        My modules        <<<
from modules.llm import text_to_ai
from modules.event_manager import EventManager
from modules.discord_stuff import DiscordEvents, DiscordOut
from modules.logging_settings import setup_logging
# >>>          Start           <<<
# .env stuff
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")  

# -------- Disocrd stuff ---------
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# Damn, Discord spams all my console with DEBUG logs, I can't read it. There's the fix:
logging.getLogger('discord').setLevel(logging.INFO)

# -------- Logging stuff ---------
setup_logging()
logger = logging.getLogger(__name__)


# >>>   The main cycle logic   <<<
async def main():
    logger.info(f"psuedo-user started!")


    event_manager = EventManager()
    discord_in = DiscordEvents(bot=bot, event_manager=event_manager)
    discord_out = DiscordOut(bot=bot, event_manager=event_manager)

    async with bot:
        await bot.start(DISCORD_TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(f"Psuedo-user stopped by user (KeyboardInterrupt!).")