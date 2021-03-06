# Virginia Link
# CS 362
# 03/06/2021

import unittest

class Test(unittest.TestCase):

    def test_easy1(self):
        self.assertTrue(calc(4))
    def test_easy2(self):
        self.assertFalse(calc(5))
    def test_hard1(self):
        self.assertFalse(calc(1700))
    def test_hard2(self):
        self.assertTrue(calc(2012))


if __name__ == '__main__':
    unittest.main()
