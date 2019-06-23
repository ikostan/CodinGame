'''

SELF-DRIVING CAR TESTING
Source: https://www.codingame.com/training/easy/self-driving-car-testing

STATEMENT

Goal
Display the trajectory of a self-driving car on the road, from its log file.

The self driving car is represented by a hash mark # and the pattern of the road
to display is given in the log file.
On an ASCII vertical scrolling, you display the car on each portion of the road.

Each command logged by the car is represented by an integer and a char
(L for left, R for right, S for straight).
For example: 4S;3R means the car is moving four times straight ahead, then three
times to the right (from a sky point of view)

Input
Line 1: The number N of lines describing the road pattern
Line 2: The position X (starting from 1) of the car at the beginning,
then a list of command separated by a semi-colon ;
N next lines: The number R of similar consecutive patterns, then, separated
with a semi-colon ; the pattern of the road to be repeated R times.

Output
The road, line by line, with the character X representing the self driving
car at its current position

Example

Input
1
2;10S
10;|     |     |

Output
|#    |     |
|#    |     |
|#    |     |
|#    |     |
|#    |     |
|#    |     |
|#    |     |
|#    |     |
|#    |     |
|#    |     |

'''


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
# print("n: " + str(n), file=sys.stderr) #  debug only

x_then_commands = input()
# print("x_then_commands: " + str(xthen_commands), file=sys.stderr) #  debug only

road_pattern = []

x_then_commands_arr = x_then_commands.split(';')

# Car's initial position
carPosition = {'iteration': 0, 'carPosition': int(x_then_commands_arr[0]) - 1, 'xthen': x_then_commands_arr[1:]}
# print(carPosition['xthen'], file=sys.stderr) #  debug only


# Extract number from direction string
def extractNumber(string):
    indx = 0
    result = ''

    while string[indx].isdigit():
        result += string[indx]
        indx += 1

    return int(result)


# Update Car Position object
def updateCarPosition(carPosition, newPosition):
    carPosition['iteration'] += 1  # Count number of iterations
    carPosition['carPosition'] = newPosition
    leadingNumber = extractNumber(carPosition['xthen'][0])

    if leadingNumber - 1 > 0:
        leadingNumber -= 1

        if 'S' in carPosition['xthen'][0]:
            carPosition['xthen'][0] = str(leadingNumber) + 'S'

        if 'R' in carPosition['xthen'][0]:
            carPosition['xthen'][0] = str(leadingNumber) + 'R'

        if 'L' in carPosition['xthen'][0]:
            carPosition['xthen'][0] = str(leadingNumber) + 'L'
    else:
        if len(carPosition['xthen']) > 0:
            carPosition['xthen'] = carPosition['xthen'][1:]

    # print(carPosition['xthen'], file=sys.stderr)


# Draw car on the road
def drawCar(xthen_commands, road, carPosition):
    car = '#'

    resultRoad = ''

    newPosition = 0
    if 'S' in carPosition['xthen'][0]:
        newPosition = carPosition['carPosition']

    if 'L' in carPosition['xthen'][0]:
        newPosition = carPosition['carPosition'] - 1

    if 'R' in carPosition['xthen'][0]:
        newPosition = carPosition['carPosition'] + 1

    updateCarPosition(carPosition, newPosition)

    for i in range(len(road)):
        if i == carPosition['carPosition']:
            resultRoad += car
        else:
            resultRoad += road[i]

    # print(resultRoad, file=sys.stderr)

    print(resultRoad)


# Draw road
def drawRoad(roadpattern):
    for rItem in roadpattern:
        pattern = rItem.split(';')
        repeatN = int(pattern[0])
        for i in range(repeatN):
            # print(pattern[1], file=sys.stderr)
            drawCar(x_then_commands, pattern[1], carPosition)


# Main loop - get road data
for i in range(n):
    rthen_roadpattern = input()
    # print("rthen_roadpattern: " + str(rthen_roadpattern), file=sys.stderr)
    road_pattern.append(rthen_roadpattern)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


drawRoad(road_pattern)
#print("Total iterations: " + str(carPosition['iteration']), file=sys.stderr)

# print("answer")
