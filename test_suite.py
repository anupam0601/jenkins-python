import pytest
import os
import time

from json_logger import Logger
from module_to_import import refer_test_case
# from module_to_import import refer_test_case

logger = Logger(file_id=__name__, log_root=os.path.join(os.path.dirname(__file__), 'LOGS'))

class TestDemo(object):

    def testcase_three(self):
        try:
            assert 1 == 2
        except AssertionError as exc:
            time.sleep(2)
            logger.exception(exc)
            logger.info(dict(test_id="testcase_three", test_status="FAIL", details={"test has failed"}))
            pytest.fail(exc, pytrace=True)



    def testcase_one(self):
        logger.info("testcase_one starting ============")
        refer_test_case()
        logger.info(dict(test_id="testcase_one", test_status="PASS", details={"test has passed"}))


    def testcase_two(self):
        logger.info("Not an error")
        logger.info(dict(test_id="testcase_two", test_status="PASS", details={"test has passed"}))
#     # def testcase_four(Self):
#     #     assert 1 % 2 == 0, "value was odd, should be even"
