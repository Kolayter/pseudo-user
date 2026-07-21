import logging
from modules.dataclasses import MessageOut

logger = logging.getLogger(__name__)

class TheCore:
    def __init__(self, discord_input_queue, discord_output_queue):
        self.discord_input_queue = discord_input_queue
        self.discord_output_queue = discord_output_queue
    
    async def start(self):
        logger.info("The core has started.")
        while True:
            message = await self.discord_input_queue.get()

            logger.info("Discord message delivered into the Core.")
            self.discord_input_queue.task_done()
            self.discord_output_queue.put(MesssageOut(

            )) # idk, review after sleep
