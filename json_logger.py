#!/usr/bin/env python

#####################
# logger module     #
#####################

import datetime
import logging
import logging.handlers
import os
import colorlog
# import socket
# import sys
# import logmatic


# Constants:
LOG_ROOT = os.path.join(os.path.dirname(__file__), 'LOGS')

# Custom log level
STEP = 25

class Logger(object):
    """
    Logger class for logging events from each action
    """

    def __init__(self, logger=None, date_tag=None,
                 filehandler=None, consolehandler=None,
                 file_id=None, formatter=None):
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
            """
            Adding custom log level STEP.
            Adding 'step' as func name to custom log level STEP
            """
            logging.addLevelName(STEP, "STEP")
            logger = logging.getLogger(file_id)
            setattr(logger, 'step', lambda *args: logger.log(STEP, *args))

        if formatter is None:
            handler = colorlog.StreamHandler()
            formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                          datefmt='%Y-%m-%d %H:%M:%S')

        if filehandler is None:
            logname = '-'.join([str(file_id), date_tag, '.json'])
            if not os.path.exists(LOG_ROOT):
                os.makedirs(LOG_ROOT)
            filehandler = logging.FileHandler(
                os.path.join(LOG_ROOT, logname))
            filehandler.setFormatter(formatter)
            # filehandler.setFormatter(logmatic.JsonFormatter(
            #     extra={"hostname": socket.gethostname()}))

        if consolehandler is None:
            consolehandler = colorlog.StreamHandler()
            consolehandler.setFormatter(colorlog.ColoredFormatter(
                fmt='%(log_color)s%(levelname)s:%(name)s:%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'))
            # consolehandler.setFormatter(logmatic.JsonFormatter(
            #     extra={"hostname": socket.gethostname()}))

        logger.addHandler(filehandler)
        logger.addHandler(consolehandler)
        logger.setLevel(logging.DEBUG)

        self.logger = logger
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

    def step(self, message):
        """
        Description:
            Logs step names for each test step
            that would be used for test cases
        Params:
            message - message want to sent to method to log
        Returns:
            self.logger.step(message) - step message
        """
        step_msg = ("============ {} ===========").format(message)
        return self.logger.step(step_msg)

log = Logger()

if __name__ == '__main__':
    log.step("Test case 1 starts")
    log.info("Test case 1 info")
    log.error("Test case 1 error")
