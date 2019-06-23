'''

ASCII ART
Source: https://www.codingame.com/training/easy/ascii-art

WHAT WILL I LEARN?
LoopsArraysStrings
Solving this puzzle teaches how to manage strings and array arithmetics.

You'll know how to split a string into separate parts and concatenate them into a new one.

You can use indexes of arrays

External resources LoopsStringsLet's Play ASCII Art

STATEMENT
The goal of the problem is to simulate an old airport terminal display:
your program must display a line of text in ASCII art.

You have to split strings, store them and recreate others.
You can use data structures like arrays or hash tables.

Rules
ASCII art allows you to represent forms by using characters.
To be precise, in our case, these forms are words. For example,
the word "MANHATTAN" could be displayed as follows in ASCII art:


# #  #  ### # #  #  ### ###  #  ###
### # # # # # # # #  #   #  # # # #
### ### # # ### ###  #   #  ### # #
# # # # # # # # # #  #   #  # # # #
# # # # # # # # # #  #   #  # # # #

​Your mission is to write a program that can display a line of text in ASCII
art in a style you are given as input.

Game Input
Line 1: the width L of a letter represented in ASCII art. All letters are the same width.

Line 2: the height H of a letter represented in ASCII art. All letters are the same height.

Line 3: The line of text T, composed of N ASCII characters.

Following lines: the string of characters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Represented in ASCII art.

Constraints
0 < L < 30
0 < H < 30
0 < N < 200

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'

l = int(input())
h = int(input())
t = input()
print(t, file=sys.stderr)

rows = []

for i in range(h):
    row = input()
    # print(row, file=sys.stderr)
    rows.append(row)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


for row in rows:
    result = ''
    for itemT in t:
        # print(itemT, file=sys.stderr)
        if itemT.upper() in chars:
            result += row[(chars.index(itemT.upper()) * l):(chars.index(itemT.upper()) * l) + l]
            # print(itemT + ": " + result, file=sys.stderr)
        else:
            itemT = '?'
            result += row[(chars.index(itemT.upper()) * l):(chars.index(itemT.upper()) * l) + l]
    print(result)
