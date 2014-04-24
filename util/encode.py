#!/usr/bin/env python
# encoding: utf-8

"""
encode.py

A simple calculator for doing basic transformation functions that are regularly
useful for XSS, inspired by Rsnake(http://ha.ckers.org/xsscalc.html).

"""

import sys
import string

def a2d(s):
    """Convert ascii to decimal value.
    """
    return str(int(a2x(s), 16))

def a2x(s):
    """Convert ascii to hex value.
    """
    return s.encode('hex')

def htmla2d(s, semicolon=True, padding=False):
    """Convert string to decimal HTML character.
    """
    r = ""
    for i in s:
        if padding:
            r += "&#%s%s" % ((7 - len(a2d(i))) * str(0), a2d(i))
        else:
            r += "&#%s" % (a2d(i))
        r = "%s;" % (r) if semicolon else r
    return r

def htmla2x(s, semicolon=True):
    """Convert string to hexdecimal HTML character.
    """
    r = ""
    for i in s:
        r += "&#x%s" % (string.upper(a2x(i)))
        r = "%s;" % (r) if semicolon else r
    return r

def urla2x(s):
    """Convert string to hexdecimal URL character. 
    """
    r = ""
    for i in s:
        r += "%%%s" % (string.upper(a2x(i)))
    return r

if __name__ == '__main__':
    s = sys.argv[1]
    print htmla2d(s)
    print htmla2d(s, semicolon=False)
    print htmla2d(s, semicolon=True, padding=True)
    print htmla2d(s, semicolon=False, padding=True)
    print htmla2x(s)
    print htmla2x(s, semicolon=False)
    print urla2x(s)

