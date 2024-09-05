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

#print(data) debug

#print(data)


# prints the key matrix
print('\nKey matrix:')
print('\t', end='')
print('\t'.join(str(x) for x in open(argv[1]).readlines()[1:]), end='', sep='')

#prints the plaintext
print('\nPlaintext:')


# 80 chars per print line total
i = 0 # inclusive, start of char print
j = 80 # exclusive, end of char print
while(i < len(plain)):
    print(plain[i:j])
    i+=80
    j+=80

print('\nCyphertext:')


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