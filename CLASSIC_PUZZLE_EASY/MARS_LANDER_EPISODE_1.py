'''
Source: https://www.codingame.com/training/easy/mars-lander-episode-1

WHAT WILL I LEARN?
Conditions
This puzzle teaches you how to compare values using a simple condition.

External resources: Conditions

STATEMENT
The goal of this puzzle is to safely land the spaceship on the platform.
It's an simple introduction to the « Mars Lander - Episode 2 ».
Some data is useless and solving this problem only requires a simple condition.


The Goal
The goal for your program is to safely land the "Mars Lander" shuttle,
the landing ship which contains the Opportunity rover.
Mars Lander is guided by a program, and right now the failure rate for
landing on the NASA simulator is unacceptable.

Note that it may look like a difficult problem, but in reality the problem
is easy to solve. This puzzle is the first level among three, therefore,
we need to present you some controls you won't need in order to complete this first level.

The game simulates a free fall without atmosphere. Gravity on Mars is 3.711 m/s² . For a thrust power of X, a push force equivalent to X m/s² is generated and X liters of fuel are consumed. As such, a thrust power of 4 in an almost vertical position is needed to compensate for the gravity on Mars.

For a landing to be successful, the ship must:
land on flat ground
land in a vertical position (tilt angle = 0°)
vertical speed must be limited ( ≤ 40m/s in absolute value)
horizontal speed must be limited ( ≤ 20m/s in absolute value)

Remember that this puzzle was simplified:
the landing zone is just below the shuttle.
You can therefore ignore rotation and always output 0 as the target angle.
you don't need to store the coordinates of the surface of Mars to succeed.
you only need your vertical landing speed to be between 0 and 40m/s – your horizontal speed being nil.
As the shuttle falls, the vertical speed is negative.
As the shuttle flies upward, the vertical speed is positive.
'''

