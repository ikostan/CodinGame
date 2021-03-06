'''

WHAT WILL I LEARN?
ConditionsLoopsEncodingStrings
Solving this puzzle makes you convert characters into their digital values and also
digits into binary values.

You have to go through a list of bits of a digital value.

External resources Bit maskBit shiftsAscii table
STATEMENT
Your program must encode a string into a series of zeros.

A string is an encoded form of digital values and you have to transform those values
into a new format.

The Goal
Binary with 0 and 1 is good, but binary with only 0, or almost, is even better!
Originally, this is a concept designed by Chuck Norris to send so called unary messages.

Write a program that takes an incoming message as input and displays as output the
message encoded using Chuck Norris’ method.

Rules
Here is the encoding principle:

The input message consists of ASCII characters (7-bit)
The encoded output message consists of blocks of 0
A block is separated from another block by a space
Two consecutive blocks are used to produce a series of same value bits (only 1 or 0 values):
- First block: it is always 0 or 00. If it is 0, then the series contains 1, if not,
it contains 0
- Second block: the number of 0 in this block is the number of bits in the series

Example
Let’s take a simple example with a message which consists of only one character:
Capital C. C in binary is represented as 1000011, so with Chuck Norris’ technique this gives:

0 0 (the first series consists of only a single 1)
00 0000 (the second series consists of four 0)
0 00 (the third consists of two 1)
So C is coded as: 0 0 00 0000 0 00


Second example, we want to encode the message CC (i.e. the 14 bits 10000111000011) :

0 0 (one single 1)
00 0000 (four 0)
0 000 (three 1)
00 0000 (four 0)
0 00 (two 1)
So CC is coded as: 0 0 00 0000 0 000 00 0000 0 00

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

binaryMessage = ''
print(message, file=sys.stderr)

for t in message:
    # print(bin(ord(t))[2:], file=sys.stderr)
    tempMsg = bin(ord(t))[2:]
    if len(tempMsg) < 7:
        tempMsg = '0' + tempMsg
    binaryMessage += tempMsg

# print(binaryMessage, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

result = ''

for i in range(len(binaryMessage)):
    if i == 0:
        if binaryMessage[i] == '1':
            result += '0 0'
        else:
            result += '00 0'
    elif binaryMessage[i] != binaryMessage[i - 1]:
        if binaryMessage[i] == '1':
            result += ' 0 0'
        else:
            result += ' 00 0'
    else:
        result += '0'

print(result)