from json_logger import Logger
import os

event = Logger(file_id=__name__, log_root=os.path.join(os.path.dirname(__file__), 'LOGS'))


def refer_test_case():
    event.info("testEg")
