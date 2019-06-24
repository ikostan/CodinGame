import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'

l = int(input())
h = int(input())
t = input()
print(t, file=sys.stderr)

rows = []

for i in range(h):
    row = input()
    # print(row, file=sys.stderr)
    rows.append(row)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


for row in rows:
    result = ''
    for itemT in t:
        # print(itemT, file=sys.stderr)
        if itemT.upper() in chars:
            result += row[(chars.index(itemT.upper()) * l):(chars.index(itemT.upper()) * l) + l]
            # print(itemT + ": " + result, file=sys.stderr)
        else:
            itemT = '?'
            result += row[(chars.index(itemT.upper()) * l):(chars.index(itemT.upper()) * l) + l]
    print(result)
