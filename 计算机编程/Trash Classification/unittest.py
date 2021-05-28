# /usr/bin/env python3
# coding=utf-8

"""
This is an unittest file for the package.
Some functions is no necessary to test, because they do not return anything.

"""
__author__ = "Team No.16 in ITPP of Lanzhou University"
__copyright__ = "Copyright 2019, Study Project in Lanzhou University , China"
__license__ = "GPL V3"
__version__ = "0.1"
__maintainer__ = "Yuming Chen, Huiyi Liu, HaoBin Zhang, Haoyu Lin"
__email__ = "Chenym18@lzu.edu.cn"
__status__ = "Experimental"

import unittest

from classify import classify as c,Path


class Trash_classification_test(unittest.TestCase):
    def classify_test(self):
        path = Path('test.jpg')
        test = c(path)
        self.assertEqual(test, 'Organic')

if __name__ == '__main__':
    unittest.main()
