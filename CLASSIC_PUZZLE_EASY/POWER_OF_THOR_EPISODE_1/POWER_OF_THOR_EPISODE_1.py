'''
Source: https://www.codingame.com/training/easy/power-of-thor-episode-1

WHAT WILL I LEARN?
Conditions
In this puzzle, you need to compare different values. You have to correlate character variables and integer variables.

A straightforward solution uses 8 conditions. There is a way to simplify it and use only 4 conditions.

External resources: Conditions


STATEMENT
A basic problem to go a little bit further with conditions and variables: your program must allow Thor to reach the coordinates of the light of power in a 2D field.


Your program must allow Thor to reach the light of power.

Rules
#Thor moves on a map which is 40 wide by 18 high. Note that the coordinates (X and Y) start at the top left! This means the most top left cell has the coordinates "X=0,Y=0" and the most bottom right one has the coordinates "X=39,Y=17".

Once the program starts you are given:
the variable lightX: the X position of the light of power that Thor must reach.
the variable lightY: the Y position of the light of power that Thor must reach.
the variable initialTX: the starting X position of Thor.
the variable initialTY: the starting Y position of Thor.

Game Input

The program must first read the initialization data from the standard input, then, in an infinite loop, provides on the standard output the instructions to move Thor.
Initialization input

Line 1: 4 integers lightX lightY initialTX initialTY. (lightX, lightY) indicates the position of the light. (initialTX, initialTY) indicates the initial position of Thor.
Input for a game round

Line 1: the number of remaining moves for Thor to reach the light of power: remainingTurns. You can ignore this data but you must read it.
Output for a game round

A single line providing the move to be made: N NE E SE S SW W ou NW

Constraints
0 ≤ lightX < 40
0 ≤ lightY < 18
0 ≤ initialTX < 40
0 ≤ initialTY < 18
Response time for a game round ≤ 100ms
'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:

    direction = ""

    remaining_turns = int(input())  # The remaining amount of turns Thor can move.
    # print("***The remaining amount of turns: " + str(remaining_turns), file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # Y
    if initial_ty < light_y:
        initial_ty += 1
        direction += 'S'

    if initial_ty > light_y:
        initial_ty -= 1
        direction += 'N'

    # X
    if initial_tx < light_x:
        initial_tx += 1
        direction += 'E'

    if initial_tx > light_x:
        initial_tx -= 1
        direction += 'W'

    # A single line providing the move to be made: N NE E SE S SW W or NW
    #print("***Direction: " + direction, file=sys.stderr)
    print(direction)