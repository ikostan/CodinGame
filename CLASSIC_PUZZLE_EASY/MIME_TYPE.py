'''
MIME TYPE
Source: https://www.codingame.com/training/easy/mime-type

WHAT WILL I LEARN?
ConditionsLoopsHash TablesStrings
In this puzzle, you have to split a string into separate parts, compare them,
and recognize similar strings using a case-insensitive algorithm.

You also have to create and use an associative array and go through a large
dataset of elements.

External resources LoopsStringsAssociative arrayHash Table
STATEMENT
Back to basics with this puzzle where you have to associate file names with their MIME type.

The Goal
MIME types are used in numerous internet protocols to associate a media type
(html, image, video ...) with the content sent. The MIME type is generally inferred
from the extension of the file to be sent.

You have to write a program that makes it possible to detect the MIME type of a file
based on its name.

Rules
You are provided with a table which associates MIME types to file extensions.
You are also given a list of names of files to be transferred and for each one of
these files, you must find the MIME type to be used.

The extension of a file is defined as the substring which follows the last occurrence,
if any, of the dot character within the file name.
If the extension for a given file can be found in the association table
(case insensitive, e.g. TXT is treated the same way as txt), then print the
corresponding MIME type. If it is not possible to find the MIME type corresponding to a file,
or if the file doesn’t have an extension, print UNKNOWN.

Game Input
Input
Line 1: Number N of elements which make up the association table.

Line 2: Number Q of file names to be analyzed.

N following lines: One file extension per line and the corresponding MIME type
(separated by a blank space).

Q following lines: One file name per line.

Output
For each of the Q filenames, display on a line the corresponding MIME type.
If there is no corresponding type, then display UNKNOWN.
Constraints
0 < N < 10000
0 < Q < 10000
File extensions are composed of a maximum of 10 alphanumerical ASCII characters.
MIME types are composed of a maximum 50 alphanumerical and punctuation ASCII characters.
File names are composed of a maximum of 256 alphanumerical ASCII characters and dots
(full stops).
There are no spaces in the file names, extensions or MIME types.

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

types = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    types.append(['.' + ext.lower(), mt])

#types.sort()
#print(types, file=sys.stderr)

#files = []
#results = []
for i in range(q):
    fname = input()  # One file name per line.
    #files.append(fname)
    #print(fname, file=sys.stderr)
    isDetected = False
    fname = fname.lower()
    for typeF in types:
        if typeF[0] in fname:
            #results.append(typeF[1])
            extLen = len(typeF[0])
            #print(fname[-extLen:].lower(), file=sys.stderr)
            if fname[-extLen:] == typeF[0]:
                isDetected = True
                #print(fname, file=sys.stderr)
                print(typeF[1])
                break
    if isDetected == False:
        #results.append('UNKNOWN')
        #print(fname, file=sys.stderr)
        print('UNKNOWN')


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
#for i in results:
    #print(i)



