#!/usr/bin/env python3
"""
Solution for Problem 1 of Set 1 of the Cryptopals Challenges
(C) Shea Polansky, licensed under GPLv3
2017-06-24

Usage: ./problem2.py <hexbuffer> <hexbuffer>
Output: pairwise bitwise XOR of each byte in the buffer, hex encoded
"""

import sys, base64, itertools

lhs = base64.b16decode(sys.argv[1], True)
rhs = base64.b16decode(sys.argv[2], True)

output = [a ^ b for a,b in zip(lhs, rhs)]
print(base64.b16encode(bytes(output)).decode("utf8"))