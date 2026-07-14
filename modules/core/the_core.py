import logging

logger = logging.getLogger(__name__)

class TheCore:
    def __init__(self, input_queue, output_queue):
        self.input_queue = input_queue
        self.output_queue = output_queue
    
    async def start(self):
        logger.info("The core has started.")
        while True:
            message = await self.input_queue.get()

            logger.info("Message delivered into the Core.")
            self.input_queue.task_done()