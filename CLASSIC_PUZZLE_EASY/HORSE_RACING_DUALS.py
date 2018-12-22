'''
HORSE-RACING DUALS
Source: https://www.codingame.com/training/easy/horse-racing-duals

WHAT WILL I LEARN?
Loops
This puzzle shows that sometimes, the simplest solution is not performant enough.
You will also learn to handle large arrays and gain experience with their processing time.

External resources SortingLists
STATEMENT
In this problem you have to find the two numbers that are closest to each other among a
list of numbers. The list might be really large and force you to search for the
best possible algorithmic complexity for your solution.

The Goal
Casablanca’s hippodrome is organizing a new type of horse racing: duals. During a dual,
only two horses will participate in the race. In order for the race to be interesting, it is necessary to try to select two horses with similar strength.

Write a program which, using a given number of strengths, identifies the two closest
strengths and shows their difference with an integer (≥ 0).

Game Input
Input
Line 1: Number N of horses

The N following lines: the strength Pi of each horse. Pi is an integer.

Output
The difference D between the two closest strengths. D is an integer greater than or equal to 0.
Constraints
1 < N  < 100000
0 < Pi ≤ 10000000

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
horses = []
answer = 10000000

for i in range(n):
    pi = int(input())
    # print(pi, file=sys.stderr)
    horses.append(pi)

horses.sort()
answer = max(horses)

for h in range(len(horses) - 1):
    dif = abs(horses[h] - horses[h + 1])
    if dif < answer:
        answer = dif

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


print(answer)