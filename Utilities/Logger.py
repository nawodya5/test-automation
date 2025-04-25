import logging
import os
from datetime import datetime


class LogGen:
    @staticmethod
    def loggen():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Logs')
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        log_file = os.path.join(logs_dir, f'test_run_{timestamp}.log')
        logger = logging.getLogger("AutomationLogger")
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            file_handler = logging.FileHandler(log_file, mode='a')
            file_handler.setFormatter(logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            ))

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(logging.Formatter(
                '%(levelname)s: %(message)s'
            ))
            logger.addHandler(file_handler)
            # logger.addHandler(console_handler)

        return logger
