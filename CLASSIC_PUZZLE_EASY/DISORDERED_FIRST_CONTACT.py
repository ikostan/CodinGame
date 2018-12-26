'''
DISORDERED_FIRST_CONTACT
Source: https://www.codingame.com/training/easy/disordered-first-contact

Goal
Finally, we have received the first messages from aliens! Unfortunately we cannot understand them because they have a very unique way of speaking.

Here is how their messages are encoded:
abcdefghi
becomes
ghibcadef

First you take the first 1 character :
a

Then you take the following 2 characters and place it in the front of the string:
bc -> a

Then you take the following 3 characters and place it in the end of the string:
bca <- def

Repeat by taking more and more characters then complete with what remains:
ghi -> bcadef


Some messages have been transformed using the above method more than once.

Your job here is to decode or encode the messages to discuss with aliens.

Input
Line 1: An integer N indicating the number of times the message was transformed. If N is positive you have to decode i.e. retrieve the original message. If N is negative you have to encode i.e. transform the message.
Line 2: A string message to be decoded or encoded.

Output
One line: The original message (if N is positive) or the transformed message (if N is negative).
Constraints
-10 ≤ N ≤ 10
0 < message length < 1024

Example

Input
1
ghibcadef

Output
abcdefghi

'''