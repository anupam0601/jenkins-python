#!/usr/bin/env python

#####################
# logger module     #
#####################

import datetime
import logging
import logging.handlers
import os
import socket
import logmatic
import sys

# Constants:
LOG_ROOT = os.path.join(os.path.dirname(__file__), 'LOGS')


class Logger(object):
    """
    Logger class for logging events from each action
    """

    def __init__(self, logger=None, date_tag=None,
                 filehandler=None, consolehandler=None,
                 file_id=None):
        """
        Description:
            constructor for all the default params for the logger
        Params:
            logger - logger object
            date_tag - date time stamp
            filehandler - To write to a file
            consolehandler - To display logs in console
            file_id - file name prefix
        """

        if date_tag is None:
            date_tag = datetime.datetime.now()\
                .strftime("%Y-%b-%d-%H-%M-%S")

        if file_id is None:
            # file_id = LOG_ID
            file_id = "test_logs"

        if logger is None:
            # logger = logging.getLogger(file_id)
            logger = logging.getLogger(file_id)

            # Add handlers and set log level

        if filehandler is None:
            logname = '-'.join([str(file_id), date_tag, '.json'])
            if not os.path.exists(LOG_ROOT):
                os.makedirs(LOG_ROOT)
            filehandler = logging.FileHandler(
                os.path.join(LOG_ROOT, logname))
            filehandler.setFormatter(logmatic.JsonFormatter(
                extra={"hostname": socket.gethostname()}))

        if consolehandler is None:
            consolehandler = logging.StreamHandler(stream=sys.stdout)
            consolehandler.setFormatter(logmatic.JsonFormatter(
                extra={"hostname": socket.gethostname()}))

        logger.addHandler(filehandler)
        logger.addHandler(consolehandler)
        logger.setLevel(logging.DEBUG)

        self.logger = logger
        self.info = logger.info
        self.debug = logger.debug
        self.date_tag = date_tag
        self.filehandler = filehandler
        self.consolehandler = consolehandler
        self.file_id = file_id

    def info(self, message):
        """
        Description:
            Logs info message
        Params:
            message - message want to sent to method to log
        Returns:
            self.logger.info(message) - info message
        """

        return self.logger.info(message)

    def debug(self, message):
        """
        Description:
            Logs debug message
        Params:
            message - message want to sent to method to log
        Returns:
            self.logger.debug(message) - debug message
        """
        return self.logger.debug(message)

    def error(self, message):
        """
        Description:
            Logs error message
        Params:
            message - message want to sent to method to log
        Returns:
            self.logger.error(message) - error message
        """
        return self.logger.error(message)

log = Logger()
