import asyncio
from dotenv import load_dotenv
import os
# ================================
# >>>        My modules        <<<
from modules.llm import text_to_ai
from modules.event_manager import EventManager
from modules.discord_stuff import DiscordOut, bot
from modules.logging_settings import setup_logging
# ================================
# >>>          Start           <<<
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# ================================
# >>>   The main cycle logic   <<<
async def main():

    event_manager = EventManager()
    discord_out = DiscordOut(bot=bot, manager=event_manager)

    async with bot:
        await bot.start(DISCORD_TOKEN)


# ===============================
# -------------------------------
if __name__ == "__main__":
    asyncio.run(main())