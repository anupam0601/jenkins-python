import unittest
from test_eg import testEg
from json_logger import log


# log.info("testing current module")

class TestLogger(unittest.TestCase):

    def setUp(self):
        pass

    def testcase_one(self):
        log.info("test case one executing")

    def testcase_two(self):
        log.info("Not an error")

    def testcase_three(self):
        # anupam()
        log.info("====== TestCase 3 Executing =====")
        # log.error("three error ====================?")
        testEg()
        log.info("====== TestCase 3 Ended =====")


    def tearDown(self):
        pass