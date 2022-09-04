#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Unit tests for logger.

@author   Hank Adler
@version  0.1.0
@license  MIT
"""


import datetime
import os
import unittest

import header
import logger as _logger


class Test(unittest.TestCase):
    """Tests all logger functions."""

    result = unittest.TestResult()
    name = 'logger'
    version = header.getVersion(''.join(_logger.__path__) + '/' + name + '.py')
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    logger = _logger.get(__name__, '%s-%s-unittest-%s' % (name, version, date))

    # Override
    def setUp(self):
        print()
        self.logger.info('%s' % '-' * 70)

    # Override
    def tearDown(self):
        if self.result.wasSuccessful():
            self.logger.info('RESULT: PASS')
        else:
            self.logger.info('RESULT: FAIL')
        os.remove(__file__.replace('.py', '.log'))

    def testGet(self):
        self.logger.info('  TEST: logger.get(__name__, __file__)')
        self.logger.info("Checks that 'logger_tests.log' gets created.")
        logger = _logger.get(__name__, __file__)
        self.assertTrue(os.path.exists(__file__.replace('.py', '.log')))


if __name__ == '__main__':
    print(__doc__, end='')
    unittest.main()
