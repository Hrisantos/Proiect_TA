"""
This file is for creating testing reports.
"""
import unittest
import HtmlTestRunner
from Tests.test_1 import TestSite
from Tests.test_2 import TestTitle
from Tests.test_3 import TestProduct
from Tests.test_4 import TestLowProduct
from Tests.test_5 import TestHighProduct
from Tests.test_6 import UnlistedProduct
from Tests.test_7 import LoginURL
from Tests.test_8 import LoginErrorMsg
from Tests.test_9 import TestLoginFail
from Tests.test_10 import TestLogin


class TestingSuite(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestSite),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestTitle),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestLowProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestHighProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(UnlistedProduct),
                             unittest.defaultTestLoader.loadTestsFromTestCase(LoginURL),
                             unittest.defaultTestLoader.loadTestsFromTestCase(LoginErrorMsg),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginFail),
                             unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Result Test Login',
            report_title='Positive and Negative Login Tests'
        )

        runner.run(test_suite)
