She has been provided with a custom 7-segment representation of digits, basic mathematical operators, and brackets, along with an equation to evaluate. She can toggle exactly one LED, that is, switch it from ON to OFF or from OFF to ON.

However, toggling an LED from ON to OFF incurs a cost of X rupees, while toggling it from OFF to ON costs Y rupees. Additionally, if the toggle transforms a number into an operator, it costs P rupees, and if it changes an operator into a number, it costs Q rupees. This is called Cost of toggling (COT).

Now comes the real task. You must toggle any one of the LED in the entire equation. Then evaluate the equation based on the priority of operators given in the input (highest to lowest). This is called Value of equation (VOE).

Goal is to find the maximum possible value of VOE / COT.

Constraints
3 <= Number of characters in the provided equation <= 50

1 <= X, Y, P, Q <= 50

The equation is said to be valid only if all the operands are positive, thus result will never be negative.

Input
First line consists of an integer N denoting the number of characters in the given equation.

Next three lines consists of the digital display of the equation Deol received.

Next line consists of a string denoting the priority order of the operators.

Last line consists of four space separated integers denoting the value of X, Y, P, Q respectively.

Output
Print the maximum possible ratio (VOE/COT) up to two decimal places.

Time Limit (secs)
1

Examples
Example 1

Input

5


| _|| ||_||_|

| || ||_|| |

+-*/

1 2 3 4

Output

91.00

Explanation

The given equation is -

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@10ec523c:image5.png

The given display represents the mathematical equation 1 + 2 × 3. By toggling the LED in the '+' symbol, it is transformed into the number 8. The resulting equation after toggling is 182 x 3.

The total cost for this transformation is the sum of the cost for switching an LED from OFF to ON (Y) and the cost of toggling which convert an operator to a number (Q), which equals 2 + 4 = 6.

When the toggled equation is evaluated according to the given operator precedence, the result obtained is 546. Therefore, dividing the result by the total cost gives 546 ÷ 6 = 91. As the output should be displayed up to two decimal places, the final answer is 91.00.

Example 2

Input

11

_ _ _ _

|_||_| | _|| | _|| | _| ||_|| |

| ||_| _| || | _|| | | ||_||_|

/+-*

7 3 4 2

Output

52.67

Explanation

The given equation is -

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@10ec523c:image6.png

The given display represents the mathematical equation 3 * 6 + 4 / 2 + 1 * 0. By toggling the LED in the second '*' operator, it is transformed into number 5. The resulting equation after toggling is 3 * 6 + 4 / 2 + 150. The total cost for this transformation is the sum of the cost for switching an LED from ON to OFF (X) and the cost of toggling which convert an operator to a number (Q), which equals 7 + 2 = 9.

When the toggled equation is evaluated according to the given operator precedence, the result obtained is 474. Therefore, dividing the result by the total cost gives 474 ÷ 9 = 52.66666. As the output should be displayed up to two decimal places, the final answer is 52.67.