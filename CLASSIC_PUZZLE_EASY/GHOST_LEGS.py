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
turnsHistory = {'leftTurn': False, 'rightTurn': False}


def moveDown(h, ghost, inputChars, turnsHistory):
    if ghost['row'] + 1 <= h:
        ghost['row'] += 1
        turnsHistory['leftTurn'] = False
        turnsHistory['rightTurn'] = False
        print("DOWN", file=sys.stderr)
        # print(str(turnsHistory['leftTurn']) + " : " + str(turnsHistory['rightTurn']), file=sys.stderr)
        return True
    return False


def moveLeft(ghost, inputChars, turnsHistory):
    if ghost['col'] - 3 >= 0:
        # print(str(turnsHistory['leftTurn']) + " : " + str(turnsHistory['rightTurn']), file=sys.stderr)
        if inputChars[ghost['row']][ghost['col'] - 1] == '-' and turnsHistory['leftTurn'] == False:
            ghost['col'] -= 3
            turnsHistory['leftTurn'] = True
            turnsHistory['rightTurn'] = True
            print("LEFT", file=sys.stderr)
            # print(str(turnsHistory['leftTurn']) + " : " + str(turnsHistory['rightTurn']), file=sys.stderr)
            return True
    return False


def moveRight(w, ghost, inputChars, turnsHistory):
    if ghost['col'] + 3 <= w:
        # print(str(turnsHistory['leftTurn']) + " : " + str(turnsHistory['rightTurn']), file=sys.stderr)
        if inputChars[ghost['row']][ghost['col'] + 1] == '-' and turnsHistory['rightTurn'] == False:
            ghost['col'] += 3
            turnsHistory['leftTurn'] = True
            turnsHistory['rightTurn'] = True
            print("RIGHT", file=sys.stderr)
            # print(str(turnsHistory['leftTurn']) + " : " + str(turnsHistory['rightTurn']), file=sys.stderr)
            return True
    return False


def makeMove(w, h, ghost, inputChars, ghostFinishes, turnsHistory):
    # print(inputChars[ghost['row']][ghost['col']], file=sys.stderr)

    if inputChars[ghost['row']][ghost['col']] in ghostFinishes:
        ghost['ghostFinish'] = inputChars[ghost['row']][ghost['col']]
        return False

    if moveLeft(ghost, inputChars, turnsHistory):
        return True

    if moveRight(w, ghost, inputChars, turnsHistory):
        return True

    if moveDown(h, ghost, inputChars, turnsHistory):
        return True


for item in inputChars[0]:
    if item in ghostNames:
        ghost['ghostName'] = item
        ghost['row'] = 0
        ghost['col'] = inputChars[0].index(item)

        isTrue = True
        while isTrue == True:
            isTrue = makeMove(w, h, ghost, inputChars, ghostFinishes, turnsHistory)

        print(ghost['ghostName'] + ghost['ghostFinish'])

# print(ghostName + ghostFinish)
