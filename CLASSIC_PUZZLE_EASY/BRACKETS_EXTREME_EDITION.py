'''

BRACKETS, EXTREME EDITION
Source: https://www.codingame.com/training/easy/brackets-extreme-edition

STATEMENT

Goal
You must determine whether a given expression has valid brackets.
This means all the parentheses (), square brackets [] and curly brackets {}
must be correctly paired & nested.

The expression does not contain whitespace characters.

Input
A single line: expression.

Output
A single line: true if each kind of bracket (), [] and {} in expression are paired correctly,
false otherwise.

Constraints
expression contains less than 2048 characters.

Example:

Input
{([]){}()}

Output
true

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

expression = input()
# print(expression, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

validBracket = ['(', ')', '[', ']', '{', '}']


def findPare(bracket):
    if bracket == '(':
        return ')'

    if bracket == '[':
        return ']'

    if bracket == '{':
        return '}'


exp = list(expression)


def removeBrkt(arr, exp):
    i = len(arr) - 1
    while i >= 0:
        print("Removing: " + exp[arr[i]], file=sys.stderr)
        exp.pop(arr[i])
        i -= 1


while len(exp) > 0:

    print(exp, file=sys.stderr)
    i = 0
    arr = []
    arr.append(i)

    if exp[i] in validBracket:
        b = i + 1
        pair = findPare(exp[i])

        while b <= len(exp):
            if exp[b] == pair:
                print("Found pair: " + exp[i] + " " + exp[b], file=sys.stderr)
                print("i: " + str(i) + " b: " + str(b), file=sys.stderr)
                arr.append(b)
                removeBrkt(arr, exp)
                break
            b += 1
    else:
        removeBrkt(arr, exp)

if len(exp) > 0:
    print("false")
else:
    print("true")