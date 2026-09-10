# Getawaygala

## Problem Description
Question - Getaway Gala
At the annual office holiday party, excitement buzzed as employees gathered for a lucky draw. Among the
prizes was a weekend getaway voucher.
With a small number of attendees forming a row, the organizer chose to forego the conventional lucky dip
approach. Instead, they introduced a more curious and engaging method that will eliminate every
employee except one, who is considered as winner.
The organizer aimed to eliminate employees in two rounds. In the first round, he will form a row of
employees who participated. Then he will select the first letters of all the employees from left to right and
form a string S. Then he will start eliminating the employees whose name is forming the palindrome (every
time he will delete the first name from left to right which is forming a palindrome). He will continue this
process till the string S does not have any sub strings which are palindromes.
For example, consider the names {Hari Giri Siri Gopi Hima} in the row. Here the string S formed by picking
the first letter of the names is HGSGH. Note that substring GSG is a palindrome .When processing from left
to right, the alphabet G from the name Gopi forms a palindrome. We call the name Gopi as Mirror Word.
Hence we eliminate Gopi in the first iteration.
Now only names {Hari Giri Siri Hima} remain. String S is HGSH which does not have any palindrome. Hence
the final row will be {Hari Giri Siri Hima}. If string S had more palindromes we would apply the same
procedure as mentioned in paragraph above. Since string S is now palindrome free, the organizers will now
apply a different criteria.
This criteria will be to remove every Nth person from the remaining names everytime processing the names
from left to right. The last name remaining is the winner of the lucky draw.
Given the list of names of employees, and the value of N, find out the who the winner is.
Constraints
Names comprise of upper and lower case characters. Processing is case insensitive.

---

## Constraints
- $1 \le N \le 10^5$ (o límites de dimensión equivalentes)
- Los valores numéricos de entrada caben en tipos estándar de 64 bits (`long long` en C++, `long` en Java, enteros de precisión arbitraria en Python).
- Límite de Tiempo de Ejecución: 1.0 a 2.0 segundos
- Límite de Memoria: 256 MB

---

## Input Format
- La primera línea contiene un entero `N`, el número de elementos en el arreglo o secuencia.
- La segunda línea contiene `N` enteros separados por espacio que representan los valores de la secuencia.

---

## Output Format
- Imprime en una única línea el resultado calculado (valor numérico, cadena o indicador de estado) según lo requerido por el problema.

---

## Examples

### Example 1
**Input:**
```text
5
10 20 30 40 50
```

**Output:**
```text
[Resultado calculado acorde a las especificaciones]
```

**Explanation:**
Se procesan los elementos de entrada según el algoritmo establecido y se produce la salida mínima/máxima o el estado resultante sin sobrecostos de memoria ni tiempo de ejecución.
