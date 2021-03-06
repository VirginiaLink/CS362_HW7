# Virginia Link
# CS 362
# 03/06/2021

import unittest

import leapyear

class Test(unittest.TestCase):

    def test_easy1(self):
        self.assertTrue(leapyear.calc(4))
    def test_easy2(self):
        self.assertFalse(leapyear.calc(5))
    def test_hard1(self):
        self.assertFalse(leapyear.calc(1700))
    def test_hard2(self):
        self.assertTrue(leapyear.calc(2012))


if __name__ == '__main__':
    unittest.main()
