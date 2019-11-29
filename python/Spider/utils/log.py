import logging
import sys
from setting import LOG_FMT, LOG_FILENAME, LOG_DATE_FMT, LOG_LEVEL


class Logger(object):

    def __init__(self):
        self._logger = logging.getLogger()
        self.formatter = logging.Formatter(fmt=LOG_FMT, datefmt=LOG_DATE_FMT)
        self._logger.addHandler(self._get_file_handler())
        self._logger.addHandler(self._get_console_handler())
        self._logger.setLevel(LOG_LEVEL)

    def _get_file_handler(self):
        file_handler = logging.FileHandler(filename=LOG_FILENAME, encoding='utf-8')
        file_handler.setFormatter(self.formatter)
        return file_handler

    def _get_console_handler(self):
        file_handler = logging.StreamHandler(sys.stdout)
        file_handler.setFormatter(self.formatter)
        return file_handler

    @property
    def logger(self):
        return self._logger


logger = Logger().logger
