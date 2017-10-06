#!/usr/bin/env python
import unittest
import xmlrunner

# test suite file
import test_suite

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_suite))

# initialize a runner, pass it your suite and run it

# runner = unittest.TextTestRunner(verbosity=3)
runner = xmlrunner.XMLTestRunner(output='test-reports')
result = runner.run(suite)