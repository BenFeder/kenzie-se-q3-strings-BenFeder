#!/usr/bin/env python3
"""
Unit tests for strings

Students should not modify this file.
"""

__author__ = 'madarp'

import sys
import unittest
import importlib
import subprocess

# suppress __pycache__ and .pyc files
sys.dont_write_bytecode = True

# Kenzie devs: change this to 'soln.strings' to test solution
PKG_NAME = 'strings'


class TestStrings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def test_author_string(self):
        """Checking for author string."""
        self.assertIsNotNone(self.module.__author__)
        self.assertNotEqual(
            self.module.__author__, "???",
            "Author string is not completed"
        )

    def test_donuts(self):
        """Check if donuts function is working"""
        donuts = self.module.donuts
        self.assertEqual(donuts(4), 'Number of donuts: 4')
        self.assertEqual(donuts(9), 'Number of donuts: 9')
        self.assertEqual(donuts(10), 'Number of donuts: many')
        self.assertEqual(donuts(99), 'Number of donuts: many')

    def test_both_ends(self):
        """Check if both_ends function is working"""
        both_ends = self.module.both_ends
        self.assertEqual(both_ends('spring'), 'spng')
        self.assertEqual(both_ends('Hello'), 'Helo')
        self.assertEqual(both_ends('a'), '')
        self.assertEqual(both_ends('xyz'), 'xyyz')

    def test_fix_start(self):
        """Check if fix_start function is working"""
        fix_start = self.module.fix_start
        self.assertEqual(fix_start('babble'), 'ba**le')
        self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
        self.assertEqual(fix_start('google'), 'goo*le')
        self.assertEqual(fix_start('donut'), 'donut')

    def test_mix_up(self):
        """Check if mix_up function is working"""
        mix_up = self.module.mix_up
        self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
        self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
        self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
        self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')

    def test_verbing(self):
        """Check if verbing function is working"""
        verbing = self.module.verbing
        self.assertEqual(verbing('hail'), 'hailing')
        self.assertEqual(verbing('swimming'), 'swimmingly')
        self.assertEqual(verbing('do'), 'do')

    def test_not_bad(self):
        """Check if not_bad function is working"""
        not_bad = self.module.not_bad
        self.assertEqual(
            not_bad('This movie is not so bad'), 'This movie is good'
            )
        self.assertEqual(
            not_bad('This dinner is not that bad!'), 'This dinner is good!'
            )
        self.assertEqual(
            not_bad('This tea is not hot'), 'This tea is not hot'
            )
        self.assertEqual(
            not_bad("It's bad yet not"), "It's bad yet not"
            )
        self.assertEqual(
            not_bad('He is bad to the bone!'), 'He is bad to the bone!'
        )
        self.assertEqual(
            not_bad('I am not feeling well'), 'I am not feeling well'
        )

    def test_front_back(self):
        """Check if front_back function is working"""
        front_back = self.module.front_back
        self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
        self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
        self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
