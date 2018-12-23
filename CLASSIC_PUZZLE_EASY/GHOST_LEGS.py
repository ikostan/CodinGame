'''

GHOST LEGS
Source: https://www.codingame.com/training/easy/ghost-legs

WHAT WILL I LEARN?
ConditionsLoopsAscii Art

STATEMENT

Goal
Ghost Legs is a kind of lottery game common in Asia. It starts with a number of vertical lines.
Between the lines there are random horizontal connectors binding all lines into a connected diagram,
like the one below.

A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3

To play the game, a player chooses a line in the top and follow the line downwards.
When a horizontal connector is encountered, he must follow the connector to turn
to another vertical line and continue downwards. Repeat this until reaching the bottom
of the diagram.

In the example diagram, when you start from A, you will end up in 2.
Starting from B will end up in 1. Starting from C will end up in 3.
It is guaranteed that every top label will map to a unique bottom label.

Given a Ghost Legs diagram, find out which top label is connected with which bottom label.
List all connected pairs.

Input
Line 1: Integer W and H for width and height of the diagram below.
Next H lines: Containing a Ghost Legs diagram as your input.

The diagram itself is composed of characters: '|' and '-', (and space).
The top line in the diagram has a number of labels T.
The bottom line contains labels B.

Each T and B is a single ascii character that can be of any random value.
Do not assume they will always be ABC or 123.

As a rule of the game, left and right horizontal connectors will never appear at the same point.

Output
List all connected pairs between top and bottom labels, TB, in the order of the top
labels from Left to Right. Write each pair in a separate line.

Constraints
3 < W, H ≤ 100

Example

Input

7 7
A  B  C
|  |  |
|--|  |
|  |--|
|  |--|
|  |  |
1  2  3

Output

A2
B1
C3

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]

# print('w: ' + str(w), file=sys.stderr)
# print('h: ' + str(h), file=sys.stderr)

inputChars = []  # Holds diagram data

for i in range(h):
    line = input()
    # print(line, file=sys.stderr)
    inputChars.append(line)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# All possible ghost names
ghostNames = []
for name in inputChars[0]:
    if name != ' ':
        ghostNames.append(name)
# print(ghostNames, file=sys.stderr)

# All possible ghost end points
ghostFinishes = []
for finish in inputChars[h - 1]:
    if finish != ' ':
        ghostFinishes.append(finish)
# print(ghostFinishes, file=sys.stderr)

# Ghost initial data
row = 0
col = 0
ghostName = ''
ghostFinish = ''

# Ghost entity
ghost = {}
ghost['row'] = row
ghost['col'] = col
ghost['ghostName'] = ghostName
ghost['ghostFinish'] = ghostFinish


# Ghost functions
def moveLeft(ghost, inputChars):
    if ghost['col'] - 1 >= 0:
        if inputChars[ghost['row']][ghost['col'] - 1] == '-':
            ghost['col'] -= 1
            return True
    return False


def moveRight(w, ghost, inputChars):
    if ghost['col'] + 1 <= w:
        if inputChars[ghost['row']][ghost['col'] + 1] == '-':
            ghost['col'] += 1
            return True
    return False


def moveDown(h, ghost, inputChars):
    if ghost['row'] + 1 <= h:
        ghost['row'] += 1
        return True
    return False

# print(ghostName + ghostFinish)
