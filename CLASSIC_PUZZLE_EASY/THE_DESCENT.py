'''
Source: https://www.codingame.com/training/easy/the-descent

WHAT WILL I LEARN?
Loops
Solving this puzzle makes you understand the concept of loops and the ways of retrieving the maximum value from a list of integers.

This puzzle can also be a playground to experiment the concept of lambdas in different programming languages. It's also an opportunity to discover functional programming.

The Goal
Destroy the mountains before your starship collides with one of them. For that, shoot the highest mountain on your path.

Rules
At the start of each game turn, you are given the height of the 8 mountains from left to right.
By the end of the game turn, you must fire on the highest mountain by outputting its index (from 0 to 7).

Firing on a mountain will only destroy part of it, reducing its height. Your ship descends after each pass.

'''

import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:

    maxH = 0
    index = 0

    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        # print("Debug messages: " + str(mountain_h), file=sys.stderr)
        if maxH < mountain_h:
            maxH = mountain_h
            index = i

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(index)