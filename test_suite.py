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
        log.step("Test Case 3 Starts")
        refer_test_case()
        log.step("Test Case 3 Ends")
