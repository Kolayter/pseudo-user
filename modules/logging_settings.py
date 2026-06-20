import logging

class ConsoleFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    cyan = "\x1b[36;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    log_format = "%(asctime)s [%(levelname)-8s] %(name)s: %(message)s"

    FORMATS = {
        logging.DEBUG: cyan + log_format + reset,
        logging.INFO: grey + log_format + reset,
        logging.WARNING: yellow + log_format + reset,
        logging.ERROR: red + log_format + reset,
        logging.CRITICAL: bold_red + log_format + reset
    }
    
    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)

logger = logging.getLogger("psuedo-user")
logger.setLevel(logging.DEBUG)

stdout_handler = logging.StreamHandler()
stdout_handler.setFormatter(ConsoleFormatter())
logger.addHandler(stdout_handler)

def setup_logging():
    # Получаем корневой логгер, который управляет ВСЕМИ логами в приложении
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    # Проверяем, чтобы не дублировать хендлеры, если модуль импортируется дважды
    if not root_logger.handlers:
        stdout_handler = logging.StreamHandler()
        stdout_handler.setFormatter(ConsoleFormatter())  # Твой красивый цветной формат
        root_logger.addHandler(stdout_handler)