Isha And Nisha
Problem Description
Isha joined a custom online IQ challenge with a prize of ₹1 lakh. Unsure about solving it alone, she sought help from her twin sister Nisha.

In this challenge, the participant is presented with an N × M letter grid containing both uppercase and lowercase alphabets. A path has been formed through the grid to create a specific word. The movement rules are such that at each time unit, the individual can step into one of the adjacent cells - specifically, from cell (2,2) at time T = 1, the next position at T = 2 can be any of {(2,1), (2,3), (1,2), (3,2)}, assuming those cells exist.

The objective is to reconstruct a given word based on provided clues. Each clue specifies that, at a particular time T, the individual will not occupy a specified sub grid. While the task may appear straightforward, some clues might be inaccurate.

If the target word cannot be traced within the grid, the solution is deemed impossible. If the word exists within the grid, the task is to identify any incorrect clues and report their count. If all clues are accurate and allow the reconstruction of the word, the output should be "All clues are correct."

Importantly, the individual must not revisit any cell during the traversal.

Nisha is diligently working on this problem because if Isha succeeds, she benefits as well, since they are twins.

Constraints
1 <= N, M <= 25

1 <= T <= 25

0 < The length of the word <= 30

The grid will have only alphabets of any case.

Input
The first line contains two integers, N and M, representing the number of rows and columns in the grid.

The next N lines each contain M space-separated alphabets, representing the grid which the person used to travel.

The next line contains an integer I, representing the number of clues Isha has received.

Each clue consists of two lines:

The first line contains the time T at which the clue is given.
The second line contains four space-separated integers: x₁, y₁, x₂, y₂, representing the top-left and bottom-right coordinates of a sub grid where the person is not located at that corresponding time.
Last line consists of the word that is formed by concatenating the letters that are present in the cells travelled by the person. Isha needs to track this word with the help of the given clues.

All indexes are based on a one-based numbering system.

Output
If all given clues are correct and the word can be found -> Print "All clues are correct".

If some clues are wrong -> Print the minimum number of faulty clues.

If it's impossible to form the word even without any clues, i.e., word is not present in the grid -> Print "Impossible".

Time Limit (secs)
1

Examples
Example 1

Input

4 4

t C s C

O d e V

i T a b

e g a N

8

1

1 1 1 4

1

1 1 4 1

1

2 1 4 4

1

2 4 4 4

2

1 1 4 3

3

1 1 4 3

3

3 1 4 4

4

1 1 4 3

sCVb

Output

1

Explanation

The word formed by concatenating the letters from the cells traversed by the person is "sCVb." The path can be outlined as follows:

At time 1, the person is positioned at (1,3) with the letter 's' and moves right to (1,4), containing the letter 'C,' at time 2. The next letter, 'V,' is encountered at (2,4) at time 3, followed by a downward movement to 'b' at (3,4) at T = 4.

Upon cross-checking these steps with the given clues, it is evident that only the first clue does not align, indicating it is faulty. As there are no alternative ways to construct the word without this discrepancy, the final answer is 1.

Example 2

Input

3 3

v a i

s h n

a v i

2

1

1 1 2 2

3

1 2 2 3

nivas

Output

All clues are correct

Explanation

The word "nivas" can be clearly traced in the grid by moving step by step in the allowed directions. At each timing, the chosen letters fit perfectly with the given clues, and no contradictions are found. Hence print "All clues are correct".

Example 3

Input

3 3

a d j

a c e

n c y

1

1

1 1 2 2

jecy

Output

Impossible

Explanation

Here, the target word is "jecy". But when looking at the grid, it is not possible to connect these letters in the required order by moving only up, down, left, or right. Since the word cannot be formed at all in the grid, regardless of the clues, the answer is "Impossible".