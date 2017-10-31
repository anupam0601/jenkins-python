import unittest

from json_logger import log
from module_to_import import refer_test_case

# log.info("testing current module")

class TestDemo(object):

    def testcase_one(self):
        log.info("test case one executing")

    def testcase_two(self):
        log.info("Not an error")

    def testcase_three(self):
        # anupam()
        log.info("====== TestCase 3 Executing =====")
        # log.error("three error ====================?")
        refer_test_case()
        log.info("====== TestCase 3 Ended ======")
