'''
The River I
Source: https://www.codingame.com/ide/puzzle/the-river-i-

STATEMENT
Goal
A digital river is a sequence of numbers where every number is followed by
the same number plus the sum of its digits. In such a sequence 123 is followed
by 129 (since 1 + 2 + 3 = 6), which again is followed by 141.

We call a digital river river K, if it starts with the value K.

For example, river 7 is the sequence beginning with {7, 14, 19, 29, 40, 44, 52, ... }
and river 471 is the sequence beginning with {471, 483, 498, 519, ... }.

Digital rivers can meet. This happens when two digital rivers share the same values.
River 32 meets river 47 at 47, while river 471 meets river 480 at 519.

Given two meeting digital rivers print out the meeting point.

Goal
A digital river is a sequence of numbers where every number is followed by the same
number plus the sum of its digits. In such a sequence 123 is followed by 129
(since 1 + 2 + 3 = 6), which again is followed by 141.

We call a digital river river K, if it starts with the value K.

For example, river 7 is the sequence beginning with {7, 14, 19, 29, 40, 44, 52, ... }
and river 471 is the sequence beginning with {471, 483, 498, 519, ... }.

Digital rivers can meet. This happens when two digital rivers share the same values.
River 32 meets river 47 at 47, while river 471 meets river 480 at 519.

Given two meeting digital rivers print out the meeting point.

Input
Line 1: The first river r1.
Line 2: The second river r2.

Output
Line 1 : The meeting point of the rivers given.

Constraints
0 < r1 ≤ 20000000
0 < r2 ≤ 20000000

Example
Input
32
47
Output
47

'''

import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# maxValue = 20000000

def calcFollowingValue(val):
    valStr = str(val)
    digits = list(valStr)
    # print(digits, file=sys.stderr)
    for i in range(len(digits)):
        digits[i] = int(digits[i])
    return val + sum(digits)


r_1 = int(input())
r_2 = int(input())

isMet = False

# firstArr = []
# secondArr = []

while isMet == False:
    # print("r_1: " + str(r_1) + " r_2: " + str(r_2), file=sys.stderr)
    if r_1 == r_2:
        isMet = True
        print(r_1)
    # elif r_1 in secondArr:
    # isMet = True
    # print(r_1)
    # elif r_2 in firstArr:
    # isMet = True
    # print(r_2)
    elif r_1 > r_2:
        r_2 = calcFollowingValue(r_2)
        # secondArr.append(r_2)
    else:
        r_1 = calcFollowingValue(r_1)
        # firstArr.append(r_1)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# print("42")
