'''

JACK SILVER: THE CASINO
Source: https://www.codingame.com/training/easy/jack-silver-the-casino

STATEMENT

Goal
Jack Silver is a spy from the international spy agency.

In his current mission he observes his targets at a roulette table at the
Great Grand Casino in Villan City. He needs to know how much money his targets
have at the end of the game.

The target plays as follows:
- He always bets 1/4 of the cash he currently has. If it is a fractional value,
he always rounds up.
- The target's calls, CALL, can be one of the three possibilities:
-- EVEN - He bets on an EVEN (non-zero) number
-- ODD - He bets on an ODD number
-- PLAIN - He bets on a specific number: NUMBER

NOTE: Since the odds of winning are much lower for PLAIN bets,
the payout for a win is higher: 35 to 1. For EVEN and ODD, the payout is 1 to 1.
As an example, if the ball comes up as 23, and the target bets 100,
the payouts would be as follows:

- If he called EVEN, then he would lose his 100 bet.
- If he called ODD, then he would get his 100 bet back, plus an extra 100.
- If he called PLAIN and specified any number other than 23, he would lose his 100 bet.
- If he called PLAIN and specified 23 as his number,
he would get back his 100 bet plus an extra 3500.

Input
Line 1: An integer, ROUNDS, for the number of rounds the target is playing
Line 2: An integer, CASH, for the amount of cash the target starts with
Next ROUNDS lines: The target's PLAY for that round, consisting of either
2 or 3 space separated variables:
1) an integer, BALL, which represents the roulette table result
2) a string, CALL, which represents the call the target made
3) (optional) an optional integer, NUMBER, which represents the selected number
when the target's call is PLAIN

Output
The amount of money, MONEY, the target has after ROUNDS of playing

Constraints
1 ≤ ROUNDS ≤ 100
50000 ≤ CASH ≤ 100000
CALL can be the text EVEN, ODD or PLAIN with an integer NUMBER
If NUMBER is set 0 ≤ NUMBER ≤ 36

1 ≤ MONEY ≤ 1 000 000

Example

Input
57
70545
31 PLAIN 30
18 PLAIN 35
14 PLAIN 32
25 ODD
13 PLAIN 9
14 PLAIN 34
32 ODD
26 PLAIN 9
29 EVEN
7 PLAIN 21
32 PLAIN 29
0 PLAIN 7
7 PLAIN 34
13 PLAIN 14
22 PLAIN 8
25 PLAIN 28
11 PLAIN 20
14 ODD
23 ODD
13 PLAIN 22
2 ODD
23 EVEN
17 ODD
30 EVEN
28 PLAIN 28
5 PLAIN 36
13 EVEN
22 PLAIN 11
5 EVEN
32 PLAIN 25
13 ODD
10 EVEN
28 ODD
15 PLAIN 2
33 EVEN
29 ODD
1 EVEN
19 PLAIN 12
0 PLAIN 34
24 EVEN
16 PLAIN 36
4 EVEN
35 PLAIN 13
14 PLAIN 34
30 ODD
13 EVEN
29 ODD
7 EVEN
18 PLAIN 20
33 ODD
24 PLAIN 28
34 PLAIN 34
33 EVEN
32 EVEN
10 EVEN
13 ODD
35 PLAIN 26

Output
1153

'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

rounds = int(input())
print("rounds: " + str(rounds), file=sys.stderr)

cash = int(input())
print("cash: " + str(cash), file=sys.stderr)

player = {'cash': cash}


def calcCash(sysInput, player):
    # He always bets 1/4 of the cash he currently has.
    # If it is a fractional value, he always rounds up.
    bet = math.ceil(float(player['cash']) / 4.)
    # player['cash'] = player['cash'] - bet
    print("bet: " + str(bet), file=sys.stderr)

    # an integer, BALL, which represents the roulette table result
    BALL = int(sysInput[0])

    if BALL == 0:
        print("********************************", file=sys.stderr)

    # a string, CALL, which represents the call the target made
    CALL = sysInput[1]

    # 1
    if CALL == 'EVEN':
        print("even>", file=sys.stderr)

        # 0 is not even
        if BALL == 0:
            player['cash'] = player['cash'] - bet
        elif BALL % 2 > 0:
            # If he called EVEN, then he would lose his bet.
            player['cash'] = player['cash'] - bet
        else:
            # Win
            player['cash'] = player['cash'] + bet
            # 2
    if CALL == 'ODD':
        # print("odd>", file=sys.stderr)
        # 0 is not even
        # if BALL == 0:
        # player['cash'] = player['cash'] + bet
        if BALL % 2 > 0:
            # If he called ODD, then he would get his bet back, plus an extra bet.
            player['cash'] = player['cash'] + bet
        else:
            # Lost
            player['cash'] = player['cash'] - bet
    # 3
    if CALL == 'PLAIN':
        # print("plain>", file=sys.stderr)
        # (optional) an optional integer, NUMBER,
        # which represents the selected number when the target's call is PLAIN
        NUMBER = int(sysInput[2])

        if NUMBER == BALL:
            # If he called PLAIN and specified 23 as his number,
            # he would get back his bet plus an extra bet * 35.
            # NOTE: Since the odds of winning are much lower for PLAIN bets,
            # the payout for a win is higher: 35 to 1. For EVEN and ODD, the payout is 1 to 1.
            player['cash'] = player['cash'] + (bet * 35)
        else:
            # If he called PLAIN and specified any number other than 23,
            # he would lose his bet.
            player['cash'] = player['cash'] - bet


for i in range(rounds):
    play = input()
    print("play: " + play, file=sys.stderr)
    sysInput = play.split(' ')
    print(sysInput, file=sys.stderr)
    calcCash(sysInput, player)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# The amount of money, MONEY, the target has after ROUNDS of playing
print(player['cash'])