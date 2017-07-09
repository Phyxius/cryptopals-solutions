#!/usr/bin/env python3
"""
Solution for Problem 1 of Set 1 of the Cryptopals Challenges
(C) Shea Polansky, licensed under GPLv3
2017-06-24

Cracks single character XOR encryption
Usage: ./problem3.py <hexdata>
Output: cracked string
"""

import sys, base64, string

encdata = base64.b16decode(sys.argv[1], True)
candidateDecryptions = [(key, [chr(char ^ key) for char in encdata]) for key in range(255)]
candidateDecryptions = sorted(candidateDecryptions, reverse = True, key = lambda pair: len(list(filter(lambda elem: elem in string.ascii_letters, pair[1]))))
for key, value in candidateDecryptions[:10]:
	print("Key:", chr(key), "Result:", "".join(value))