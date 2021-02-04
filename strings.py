#!/usr/bin/env python3
"""
Kenzie assignment: Strings!
"""
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Instructions:
# Complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'OK'
# for each function once it returns the correct result.
# The starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "Benjamin Feder"

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Example:
#   donuts(5) returns 'Number of donuts: 5'
#   donuts(23) returns 'Number of donuts: many'


def donuts(count):
    if count < 10:
        return 'Number of donuts: ' + str(count)
    else:
        return 'Number of donuts: many'


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 characters of the original string.
# However, if the string length is less than 2, return
# an empty string instead.
# Example:
#   'spring' -> 'spng'


def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]


# C. fix_start
# Given a string s, return a string where all occurrences
# of its first character have been changed to '*', except
# do not change the first character itself.
# Example:
#   'babble' -> 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.


def fix_start(s):
    if len(s) == 1:
        return s
    elif len(s) > 1:
        return s[0] + s[1:].replace(s[0], "*")


# D. mix_up
# Given strings a and b, return a single string with a and
# b separated by a space '<a> <b>', except swap the first
# 2 characters of each string.
# Example:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a + " " + new_b


# E. verbing
# Given a string, if its length is at least 3, add 'ing' to its
# end unless it already ends in 'ing', in which case add 'ly'
# instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.


def verbing(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s


# F. not_bad
# Given a string, find the first occurrence of the substrings
# 'not' and 'bad'. If the 'bad' follows the 'not', replace
# the whole 'not'...'bad' substring with 'good'.
# Return the resulting string.
# Example:
#   'This dinner is not that bad!' -> 'This dinner is good!'


def not_bad(s):
    bad_spot = s.find("bad")
    not_spot = s.find("not")
    if not_spot != -1 and bad_spot > not_spot:
        new_string = s[:not_spot] + "good" + s[bad_spot+3:]
        return new_string
    else:
        return s


# G. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same
# length. If the length is odd, we'll say that the extra
# character goes in the front half.
#   e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form:
#   a-front + b-front + a-back + b-back


def front_back(a, b):
    a_length = len(a)
    b_length = len(b)
    if a_length % 2 == 0 and b_length % 2 == 0:
        a_front = a[:a_length//2]
        a_back = a[a_length//2:]
        b_front = b[:b_length//2]
        b_back = b[b_length//2:]
    elif a_length % 2 == 0 and b_length % 2 == 1:
        a_front = a[:a_length//2]
        a_back = a[a_length//2:]
        b_front = b[:(b_length//2)+1]
        b_back = b[(b_length//2)+1:]
    elif a_length % 2 == 1 and b_length % 2 == 0:
        a_front = a[:(a_length//2)+1]
        a_back = a[(a_length//2)+1:]
        b_front = b[:b_length//2]
        b_back = b[b_length//2:]
    elif a_length % 2 == 1 and b_length % 2 == 1:
        a_front = a[:(a_length//2)+1]
        a_back = a[(a_length//2)+1:]
        b_front = b[:(b_length//2)+1]
        b_back = b[(b_length//2)+1:]
    return a_front + b_front + a_back + b_back
