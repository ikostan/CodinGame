'''

THE RIVER II
Source: https://www.codingame.com/training/easy/the-river-ii-

STATEMENT
 	Goal
A digital river is a sequence of numbers where every number is followed
by the same number plus the sum of its digits. In such a sequence 123 is
followed by 129 (since 1 + 2 + 3 = 6), which again is followed by 141.

We call a digital river river K, if it starts with the value K.

For example, river 7 is the sequence beginning with {7, 14, 19, 29, 40, 44, 52, ... }
and river 471 is the sequence beginning with {471, 483, 498, 519, ... }.

Digital rivers can meet. This happens when two digital rivers share the same values.
River 32 meets river 47 at 47, while river 471 meets river 480 at 519.

Given a number decide, whether it can be a meeting point of two or more digital rivers.
For example, it is easy to check that only river 20 contains the number 20 in its sequence
(as a starting point).

Input
Line 1: An integer r1.

Output
Line 1 : YES if r1 can be a meeting points of two digital rivers, NO otherwise.

Constraints
1 ≤ r1 < 100000

Example

Input
20
Output
NO

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# maxValue = 100000
tested = {}


def calcFollowingValue(val):
    # print(val, file=sys.stderr)
    valStr = str(val)
    digits = list(valStr)
    # print(digits, file=sys.stderr)
    for i in range(len(digits)):
        digits[i] = int(digits[i])
    return val + sum(digits)


# the maximum number of steps any river advances is (length_of_number)*9
# def calcMaxSteps(num):
# return num * 9

r_1 = int(input())
# print("r_1: " + str(r_1), file=sys.stderr)
# print("Max steps: " + str(calcMaxSteps(r_1)), file=sys.stderr)

result = 'NO'

for b in range(1, r_1):
    tested[b] = False

for i in range(1, r_1):
    if tested[i] == False:
        tested[i] == True
        test = calcFollowingValue(i)
        if test == r_1:
            result = 'YES'
            break
        else:
            continue

print(result)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
