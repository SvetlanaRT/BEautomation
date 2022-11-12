import logging
import pytest

from util import *


@pytest.mark.usefixtures("setup")
class BaseClass:

  def log_error(self, e):
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logs/logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.critical(e)

  def log(self, msg):
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('logs/logfile.log')

    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.warning(msg)

