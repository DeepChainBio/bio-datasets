"""Configure the logger for the whole project.

To use it, add the following lines at the top of your file:

from biodatasets.utils import logger

log = logger.get(__name__)

The logger can be used in the file by calling :
- log.debug('My debug message')
- log.info('My info message')
- log.warning('My warning message')
- log.critical('My critical message')
- log.exception('My exception message')

The last log can be used in try / except statement and it will log the full traceback

By default the log level is set to INFO, if you want to run as DEBUG you can do the following:
LOGLEVEL=DEBUG python ....
"""
import logging
import os


def get(name: str) -> logging.Logger:
    """Create a logger for the given module name.

    Args:
        name: module name used to called the 'get' method

    Returns:
        the logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(os.environ.get("LOGLEVEL", "INFO").upper())

    return logger
