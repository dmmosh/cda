'''
============================================================================
| Assignment: pa01 - Encrypting a plaintext file using the Hill cipher
|
| Author: Dmytro Moshkovskyi
| Language: python
| To Compile: javac pa01.java
| gcc -o pa01 pa01.c
| g++ -o pa01 pa01.cpp
| go build pa01.go
| rustc pa01.rs
| To Execute: java -> java pa01 kX.txt pX.txt
| or c++ -> ./pa01 kX.txt pX.txt
| or c -> ./pa01 kX.txt pX.txt
| or go -> ./pa01 kX.txt pX.txt
| or rust -> ./pa01 kX.txt pX.txt
| or python -> python3 pa01.py kX.txt pX.txt
| where kX.txt is the keytext file
| and pX.txt is plaintext file
| Note:
| All input files are simple 8 bit ASCII input
| All execute commands above have been tested on Eustis
|
| Class: CIS3360 - Security in Computing - Summer 2024
| Instructor: McAlpin
| Due Date: September 15th 11:59pm
+===========================================================================
'''

import sys
from sys import argv
import os 

# converts the txt file to 2d list 
#1st element (data[0][0]) is the matrix size (x by x)
key = [list(map(int,line.split())) for line in open(argv[1])]


plain = ''.join(ch for ch in open(argv[2]).read().lower() if ch.isalnum())  # the plaintext, lowercase and alpha only
plain += str('x'*(key[0][0]-(len(plain)%key[0][0]))) # adds padding (key length - (plain length % key length ))

#sys.stdout.write(data) debug

#sys.stdout.write(data)


# sys.stdout.writes the key matrix
sys.stdout.write('\nKey matrix:\n')
sys.stdout.write('\t')
sys.stdout.write('\t'.join(str(x) for x in open(argv[1]).readlines()[1:]))

#sys.stdout.writes the plaintext
sys.stdout.write('\n')
sys.stdout.write('\nPlaintext:\n')


# 80 chars per sys.stdout.write line total
i = 0 # inclusive, start of char sys.stdout.write
j = 80 # exclusive, end of char sys.stdout.write
while(i < len(plain)): # while i is smaller than length of the plaintext
    sys.stdout.write(plain[i:j], '\n') # sys.stdout.write the range of chars
    # note: python checks for index out of bounds, so program wont crash if j is longer than the string
    i+=80 # increment i 
    j+=80 # increment j 

sys.stdout.write('\n\nCyphertext:\n')


#os.system('cat ' + argv[1] + ' | sed \'1d\'')


'''
=============================================================================
| I Dmytro Moshkovskyi (dm361167) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+=============================================================================*
'''