#!/usr/bin/env python

#####################
# logger module     #
#####################

import datetime
import logging
import logging.handlers
import os
import colorlog
import socket
import sys
import logmatic
import watchtower


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
                 file_id=None, formatter=None, log_root=None):
        """
        Description:
            constructor for all the default params for the logger
        Params:
            logger - logger object
            date_tag - date time stamp
            filehandler - To write to a file
            consolehandler - To display logs in console
            file_id - file name prefix
            formatter - format of logs
            log_root - log path directory name
        """

        if date_tag is None:
            date_tag = datetime.datetime.now()\
                .strftime("%Y-%b-%d-%H-%M-%S")

        if file_id is None:
            # file_id = LOG_ID
            file_id = file_id

        if logger is None:
            """
            Adding custom log level STEP.
            Adding 'step' as func name to custom log level STEP
            """
            logging.addLevelName(STEP, "STEP")
            logger = logging.getLogger(file_id)
            setattr(logger, 'step', lambda *args: logger.log(STEP, *args))

        if formatter is None:
            formatter = logging.Formatter(fmt='%(asctime)-4s.%(msecs)-2s\
            %(levelname)-4s %(name)s:%(funcName)s:%(lineno)-3s %(message)s',
                                          datefmt='%Y-%m-%d %H:%M:%S')

        if log_root is None:
            log_root = log_root

        if filehandler is None:
            logname = '-'.join(['test_desc', date_tag, '.log'])
            if not os.path.exists(log_root):
                os.makedirs(log_root)
            filehandler = logging.FileHandler(
                os.path.join(log_root, logname))
            filehandler.setFormatter(formatter)
            # filehandler.setFormatter(logmatic.JsonFormatter())

        if consolehandler is None:
            consolehandler = colorlog.StreamHandler()
            consolehandler.setFormatter(colorlog.ColoredFormatter(
                fmt='%(log_color)s%(asctime)-s\
                %(levelname)-s %(name)s:%(funcName)s:%(lineno)-s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'))
            # consolehandler.setFormatter(logmatic.JsonFormatter(
            #     extra={"hostname": socket.gethostname()}))

        # if cloudwatch_handler is None:
        #     """
        #     Description:
        #         Handler for AWS cloudwatch logs
        #     Params:
        #         log_group - log group name in cloudwatch
        #         stream_name - file name from where logs would
        #         be streamed
        #     """
        #     cloudwatch_handler = watchtower.CloudWatchLogHandler(log_group="automation_logs",
        #                                                          stream_name=file_id)
        logger.addHandler(filehandler)
        logger.addHandler(consolehandler)
        # logger.addHandler(cloudwatch_handler)
        logger.setLevel(logging.DEBUG)

        self.logger = logger
        self.date_tag = date_tag
        self.filehandler = filehandler
        self.consolehandler = consolehandler
        # self.cloudwatch_handler = cloudwatch_handler
        self.file_id = file_id
        self.log_root = log_root
        self.info = logger.info
        self.error = logger.error
        self.debug = logger.debug
        self.step = logger.step
        self.exception = logger.exception


    # def info(self, message):
    #     """
    #     Description:
    #         Logs info message
    #     Params:
    #         message - message want to sent to method to log
    #     Returns:
    #         self.logger.info(message) - info message
    #     """

    #     return self.logger.info(message)

    # def debug(self, message):
    #     """
    #     Description:
    #         Logs debug message
    #     Params:
    #         message - message want to sent to method to log
    #     Returns:
    #         self.logger.debug(message) - debug message
    #     """
    #     return self.logger.debug(message)

    # def error(self, message):
    #     """
    #     Description:
    #         Logs error message
    #     Params:
    #         message - message want to sent to method to log
    #     Returns:
    #         self.logger.error(message, exc_info=True) - error message
    #         with stack trace, exc_info=True gives us the stack trace
    #     """
    #     return self.logger.error(message, exc_info=True)

    # def step(self, message):
    #     """
    #     Description:
    #         Logs step names for each test step
    #         that would be used for test cases
    #     Params:
    #         message - message want to sent to method to log
    #     Returns:
    #         self.logger.step(message) - step message
    #     """
    #     step_msg = ("============ {} ===========").format(message)
    #     return self.logger.step(step_msg)


if __name__ == '__main__':
    event_logger = Logger(log_root=os.path.join(os.path.dirname(__file__), 'LOGS'))
    event_logger.logger.error("Error....")
    event_logger.exception("Info..................")
