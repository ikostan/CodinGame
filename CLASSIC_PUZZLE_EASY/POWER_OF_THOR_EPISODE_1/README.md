# Power of Thor - Episode 1

### The Goal
Your program must allow Thor to reach the light of power.

### Rules
Thor moves on a map which is 40 wide by 18 high. Note that the coordinates (X and Y) start at the top left! This means the most top left cell has the coordinates "X=0,Y=0" and the most bottom right one has the coordinates "X=39,Y=17".

Once the program starts you are given:
the variable lightX: the X position of the light of power that Thor must reach.
the variable lightY: the Y position of the light of power that Thor must reach.
the variable initialTX: the starting X position of Thor.
the variable initialTY: the starting Y position of Thor.

At the end of the game turn, you must output the direction in which you want Thor to go among:<br/>
- N (North)<br/>
- NE (North-East)<br/>
- E (East)<br/>
- SE (South-East)<br/>
- S (South)<br/>
- SW (South-West)<br/>
- W (West)<br/>
- NW (North-West)<br/>

**Note:**
Do not forget to execute the tests from the "Test cases" panel.
Beware: the tests given and the validators used to compute the score are slightly different in order to avoid hard coded solutions.

### Game Input
The program must first read the initialization data from the standard input, then, in an infinite loop, provides on the standard output the instructions to move Thor.

**Initialization input**<br/>
Line 1: 4 integers lightX lightY initialTX initialTY. (lightX, lightY) indicates the position of the light. (initialTX, initialTY) indicates the initial position of Thor.

**Input for a game round**<br/>
Line 1: the number of remaining moves for Thor to reach the light of power: remainingTurns. You can ignore this data but you must read it.

**Output for a game round**<br/>
A single line providing the move to be made: N NE E SE S SW W ou NW

**Constraints**<br/>
0 ≤ lightX < 40<br/>
0 ≤ lightY < 18<br/>
0 ≤ initialTX < 40<br/>
0 ≤ initialTY < 18<br/>
Response time for a game round ≤ 100ms<br/>

### Source: 
https://www.codingame.com/ide/puzzle/power-of-thor-episode-1