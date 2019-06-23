'''
Source: https://www.codingame.com/training/easy/temperatures

WHAT WILL I LEARN?
ConditionsLoopsArrays
Solving this puzzle validates that the loop concept is understood and that you can compare a list of values.

This puzzle is also a playground to experiment the concept of lambdas in different programming languages.
It's also an opportunity to discover functional programming.

STATEMENT
Your program must analyze records of temperatures to find the closest to zero.

Rules
Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero,
positive integer has to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).

Game Input
Your program must read the data from the standard input and write the result on the standard output.
Input
Line 1: N, the number of temperatures to analyze

Line 2: A string with the N temperatures expressed as integers ranging from -273 to 5526

Output
Display 0 (zero) if no temperatures are provided. Otherwise, display the temperature closest to 0.
Constraints
0 ≤ N < 10000
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

minTemp = 10000
# print("the number of temperatures to analyse: " + str(n), file=sys.stderr)

if n == 0:
    minTemp = 0

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if abs(t) < abs(minTemp):
        minTemp = t
    elif abs(t) == abs(minTemp):
        if t > minTemp:
            minTemp = t

    # print("#" + str(index) + ": " + str(i), file=sys.stderr)
    # index += 1

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(minTemp)