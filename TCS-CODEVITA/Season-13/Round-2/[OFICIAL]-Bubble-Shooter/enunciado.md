Bubble Shooter
Problem Description
Shoot the bubble, Earn the points!

On the screen, multi-colored bubbles with different point values are clustered at the top. At the bottom, a shooter aims to burst bubbles for points.

Bursting Rules:

When the shooter hits a bubble from any direction, it pops along with all attached bubbles of the same color and those dependent on them.
If the shooter strikes a bubble diagonally instead of from the four cardinal directions, the bubble, along with any connected bubbles of the same color and their dependent bubbles, will burst.
Bubbles of different colors that burst due to dependency (not direct targeting) are considered bonus bubbles and grant extra points.
How are the bubbles dependent?

If a bubble touches another above it, the lower bubble depends on the upper one, regardless of color.
Bubbles that touch horizontally are only dependent if they're the same color.
Shooter Movement and Bounce Rule:

The shooter starts at a 45-degree left angle and maintains its trajectory.
Touching a wall or bubble from the top, bottom, left, or right causes the shooter to rebound in a new direction.
Diagonal contact with a bubble (up-left, up-right, down-left, down-right) reverses its path.
Collision with two adjacent sides at once (top & right, top & left, bottom & right, bottom & left) also reverses its path.
If there is no collision, the shooter continues forward.
Bounce Count: Only collisions with bubbles count as bounces; wall-only rebounds do not.
Game Conclusion: The game concludes when either all bubbles have been burst, or all allotted bounces have been expended.

Note: The screen's bottom-left corner will always be (0, 0)

Your Task:

You are provided with 'K' bounces. The objective is to calculate the total bonus points achievable after completing K bounces.

Constraints
10 <= R, C <= 24

M < R

0 < N < C

1 <= K <= 11

The game will get over after at least K bounces complete or all bubbles burst.

Input
First line consists of two space separated integers R and C, denoting the rows and columns of the screen.

Next line consists of one integer M denoting the number of top rows of the screen where bubbles are situated.

Next M lines consist of C space separated characters:

Characters from 'A to Z' define colors of the bubbles.
Character '.' defines empty space, meaning there is nothing at the spot.
Next line consists of all the color characters present above.

Next line consists of the points each color has, respectively.

Second-to-last line consists of an integer N denoting the column number (0-based) from where the shooter is launched.

Last line consists of integer K denoting the quota of bounces allowed.

Output
Single integer defining the total bonus points scored after K bounces gets completed.

Time Limit (secs)
1

Examples
Example 1

Input

10 12

6

O P O G G G G G B B R R

O P O R R O O R Y B B P

O B P B B B B B Y B B Y

O B P B B G G R Y Y O .

. R P B G G R Y Y Y O .

. . B G G G G G G Y . .

O P G B R Y

5 6 8 10 7 4

3

2

Output

7

Explanation

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@37fef327:image1.gif

GIF 1. Illustration of testcase 1

The shooter starts from column 3 (0-based) at 45-degree angle in left. It hit the wall and changes direction. Since the wall is hit, it will not be counted in total bounces.

Bounce 1: When the shooter comes at the position of 4th row, 1st column, it touches the bubbles at up and right direction which results in bursting of those, and bounce will be counted. Since the bubbles are on both sides, the shooter reflects back. There are no dependent bubbles to burst.
Bounce 2: When the shooter comes at the position of 3rd row, 6th column, it bursts the bubble upwards which results in bursts of all the connected bubbles. Since the bubble at row 5 column 6 is dependent, it will fall contributing to bonus point for 1 Red Bubble.
So, after 2 bounces, total bonus points scored is 7.

Example 2

Input

10 12

6

O P O G G G G G B B R R

O P O R R O O R Y B B P

O B P B B B B B Y B B Y

O B P B G G G R Y Y O .

. . P B G R R Y Y Y O .

. . B G G G G G G Y . .

O P G B R Y

9 8 10 15 8 4

3

3

Output

16

Explanation

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@37fef327:image2.gif

GIF 2. Illustration of testcase 2

The shooter starts from column 3 (0-based) at 45-degree angle in left. It hits the wall at 3rd row, 0th column and changes direction.

Bounce 1: When the shooter comes at the position 4th row, 1st column, it touches and bursts the bubble at right. Bounce will be counted, and direction will be changed. No dependent bubbles to burst.
Bounce 2: When the shooter comes at the position of 5th row, 0th column, it touches the wall and bubble as well. Since shooter collides with bubble, it bursts the bubble and bounce will be considered, direction will be changed. No dependent bubble to burst.
Bounce 3: When the shooter comes at the position of 3rd row, 8th column, it touches the bubble upwards, bursts it and all the connected and dependent bubbles burst. The dependent bubbles consist of 2 Red bubbles of 8 points each.
So, after 3 bounces, total bonus points scored: 16

Example 3

Input

10 12

6

O P O G G G G G B B R R

O P O R R O O R Y B B P

O B P P P P P P Y B B Y

O B P B B G G P Y Y O .

. . P B G G R Y Y Y O .

. . . G G G G G G Y . .

O P G B R Y

5 6 8 10 7 4

3

1

Output

0

Explanation

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@37fef327:image3.gif

GIF 3. Illustration of testcase 3

The shooter starts from column 3 (0-based) at 45-degree angle in left, hits the wall at 3rd row, 0th column and changes direction.

Bounce 1: When the shooter comes at the position of 4th row, 1st column, it touches and bursts the bubble at top-right. Since the bubble it touches is in diagonal direction, shooter reflects back in the reverse path. No dependent bubbles to burst.
So, after 1 bounce, total bonus points scored is 0.  


