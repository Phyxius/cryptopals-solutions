#!/usr/bin/env python3
"""
Solution for Problem 1 of Set 1 of the Cryptopals Challenges
(C) Shea Polansky, licensed under GPLv3
2017-06-24

Usage: ./problem1.py <hexdata>
Output: base64 representation of the argument
"""

import sys, base64
print(base64.encodestring(base64.b16decode(sys.argv[1], True)).decode("utf8"))