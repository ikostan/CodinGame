'''

DEFIBRILLATORS
Source: https://www.codingame.com/training/easy/defibrillators

WHAT WILL I LEARN?
LoopsDistancesTrigonometry
This puzzle makes you split a string into substrings,
replace a character of a string and convert it into floats.
You also have to convert degrees into radians and use mathematical
operations like square root or cosinus.

Finally you have to apply multiple computations (addition, multiplication...)
on floating numbers.

STATEMENT
The goal of this exercise is to make you find the closest point to given
geographic coordinates (latitude and longitude). Your program must print
the associated location name.

In this puzzle you will play a lot with conversion (degree to radian,
coordinates to distance, string to float).

The Goal
The city of Montpellier has equipped its streets with defibrillators to
help save victims of cardiac arrests. The data corresponding to the position
of all defibrillators is available online.

Based on the data we provide in the tests, write a program that will
allow users to find the defibrillator nearest to their location using their mobile phone.

Rules
The input data you require for your program is provided in text format.
This data is comprised of lines, each of which represents a defibrillator.
Each defibrillator is represented by the following fields:
A number identifying the defibrillator
Name
Address
Contact Phone number
Longitude (degrees)
Latitude (degrees)
These fields are separated by a semicolon (;).

Beware: the decimal numbers use the comma (,) as decimal separator.
Remember to turn the comma (,) into dot (.) if necessary in order
to use the data in your program.

'''

import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def calcDistance(longUser, longDefib, latitUser, latitDefib):
    longDefib = float(longDefib)
    latitDefib = float(latitDefib)
    x = (longDefib - longUser) * math.cos((latitUser + latitDefib) / 2.)
    y = (latitDefib - latitUser)

    # Note: In this formula, the latitudes and longitudes are expressed in radians.
    # 6371 corresponds to the radius of the earth in km.

    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2)) * 6371.

    return distance


lon = input()
# print("Lon: " + str(lon), file=sys.stderr)

lat = input()
# print("Lat: " + str(lat), file=sys.stderr)

userLocation = {'lon': float(lon.replace(',', '.')), 'lat': float(lat.replace(',', '.'))}
# print(userLocation, file=sys.stderr)

n = int(input())
# print("N: " + str(n), file=sys.stderr)

defibLocation = []

for i in range(n):
    defib = input()
    # print(defib, file=sys.stderr)
    defTempData = defib.split(';')
    defibLocation.append(defTempData)

# print(defibLocation, file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

distances = []

# print(defibLocation[0][5].replace(',','.'), file=sys.stderr)

index = 0
for defibItem in defibLocation:
    # print("index: " + str(index), file=sys.stderr)
    distances.append(calcDistance(userLocation['lon'], defibLocation[index][4].replace(',', '.'), userLocation['lat'],
                                  defibLocation[index][5].replace(',', '.')))
    index += 1

# rint(distances, file=sys.stderr)

answer = 'N/A'
if len(distances) > 0:
    minDist = min(distances)
    minIndx = distances.index(minDist)
    answer = defibLocation[minIndx][1]

print(answer)
