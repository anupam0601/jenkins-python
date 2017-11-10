from json_logger import Logger
import os

event = Logger(file_id=__name__)


def refer_test_case():
    event.info("testEg")
