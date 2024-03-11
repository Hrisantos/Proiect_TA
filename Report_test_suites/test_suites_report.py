"""
This file is for creating testing reports.
"""
import unittest
import HtmlTestRunner
from Tests import *


class TestingSuite(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestNegativeLogin),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestPositiveLogin)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Result Test Login',
            report_title='Positive and Negative Login Tests'
        )

        runner.run(test_suite)
