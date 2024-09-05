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
| Class: CIS3360 - Security in Computing - Fall 2024
| Instructor: McAlpin
| Due Date: September 15th 11:59pm
+===========================================================================
'''

import sys
from sys import argv
import os 

def out(input:str): #outputs in the 80 chars limit
    i = 0 # inclusive, start of char sys.stdout.write
    j = 80 # exclusive, end of char sys.stdout.write
    while(i < len(input)): # while i is smaller than length of the plaintext
        sys.stdout.write(input[i:j]) # sys.stdout.write the range of chars
        sys.stdout.write('\n')
        # note: python checks for index out of bounds, so program wont crash if j is longer than the string
        i+=80 # increment i 
        j+=80 # increment j 

if len(argv) == 1:
    exit()

# note: sys stdout instead of print ( just in case )


# converts the txt file to 2d list 
#1st element (data[0][0]) is the matrix size (x by x)
key = [list(map(int,line.split())) for line in open(argv[1])][1:] # the key (cut off by first element )
block_len = len(key) # block length, same as cutoff element



# sys.stdout.writes the key matrix
sys.stdout.write('\nKey matrix:\n') # the key matrix
sys.stdout.write('\t') 
sys.stdout.write('\t'.join(str(x) for x in open(argv[1]).readlines()[1:])) # prints the key matrix from argv 




sys.stdout.write('\nPlaintext:\n') # plaintext
plain = ''.join(ch for ch in open(argv[2]).read().lower() if (ch.isalpha() and ord(ch) < 123))  # the plaintext, lowercase and alpha only
plain += str('x'*(block_len-(len(plain)%block_len))) # adds padding (key length - (plain length % key length ))
out(plain)




sys.stdout.write('\nCiphertext:\n') # ciphertext portion
# actually cool stuff
cipher = '' #output ciphertext
i = 0 # i to i + block_len ( exclusive)
while(i < len(plain)): # iterate through the plaintext
    # matrix = key
    # note: matrix is square always

    # the vector is plain[i: i+block_len]
    # iterating through it using col is plain[i+col]
    for row in range(0, block_len): # for every row in the matrix ( key)
        sum = 0 # sum 
        for col in range(0, block_len): # for every column in the matrix
            sum+= key[row][col] * (ord(plain[i+col])-97) # adds the product of matrix's rowxcol with the value of vector (starting from a = 0, converted from ascii)
        cipher+=chr(sum%26 + 97) # mods the number by 26 and converts back to ascii, concating to the ciphertext output

    #print(vector)
    i+=block_len # iterates forward

out(cipher) # prints ciphertext


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