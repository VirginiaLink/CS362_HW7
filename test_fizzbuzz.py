# Virginia Link
# CS 362
# 03/05/2021

import unittest
import io
import sys


class Test(unittest.TestCase):

    def test_check_5(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        fizzbuzz.fb()
        sys.stdout = sys.__stdout__
        self.assertNotIn('5', capturedOutput)
    def test_check_3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        fizzbuzz.fb()
        sys.stdout = sys.__stdout__
        self.assertNotIn('3', capturedOutput)
    def test_check_15(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        fizzbuzz.fb()
        sys.stdout = sys.__stdout__
        self.assertNotIn('15', capturedOutput)




if __name__ == '__main__':
    unittest.main()
