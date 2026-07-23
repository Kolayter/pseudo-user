# modules/telegram_adapter.py
# Не, я типа реально не знаю чё тут писать. Этот файл пока на будущее.

class TelegramIn:
    def __init__(self, token, telegram_input_queue):
        self.bot_like = token
        self.telegram_input_queue = telegram_input_queue

    async def start(self):
        pass

class TelegramOut:
    def __init__(self, token, telegram_output_queue):
        self.bot_like = token
        self.telegram_output_queue = telegram_output_queue

    async def start(self):
        pass