#!/usr/bin/env python3
"""
Solution for Problem 1 of Set 1 of the Cryptopals Challenges
(C) Shea Polansky, licensed under GPLv3
2017-06-24

Identifies which string of a list is encrypted with single character XOR encryption,
and cracks it. Input each line from STDIN, separated by newlines
Usage: ./problem3.py 
Output: cracked string
"""

import sys, base64, string

candidateLines = []
count = 0

for line in sys.stdin:
	count += 1
	encdata = base64.b16decode(line.strip(), True)
	candidateLines += [(count, key, [chr(char ^ key) for char in encdata]) for key in range(255)]

candidateLines = sorted(candidateLines, reverse = True, key = lambda pair: len(list(filter(lambda elem: elem in string.ascii_letters+' \n', pair[2]))))
number, key, decryption = candidateLines[0]
print("Line:", number)
print("Key:", key)
print("Decryption:", "".join(decryption))