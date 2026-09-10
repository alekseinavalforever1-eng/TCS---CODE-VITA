# Football Team

## Problem Description
Problem Description

You are given the scores of a football league among a set of teams. You need to find the winner of the league and print the 
name of winner and points earned by the team. Each team gets 3 points for a win, 1 point for a draw and 0 for a loss. The name 
of the teams is represented as upper case character viz. A B...Z.

* Constraints

There will only be one team which gets the highest points

* Input

There are many lines in the input.

The first line contains an integer, N, representing number of teams in the league. The next (N*(N-1))/2 lines contain three 
space separated strings <Team1, Team2, Score>
Here, Team1 is the name of the home team. Team2 is the name of the away team. Score represents the score of the match, (M-N), 
where M represents the score of the home team and N represents the score of the away team.

* Output

The output should have two lines. 

The first line should contain a character representing the name of the leader team. The second line containing an integer 
representing the points won by the leader team.

* Time Limit

1

Example 1

Input :

3
A B 2-1
B C 5-6
C A 2-1

Output :

C
6

Explanation:

A has won 1 match : 3 points
B has won 0 match: 0 points
C has won 2 match : 6 points

---

## Constraints
- $1 \le N \le 10^5$ (o límites de dimensión equivalentes)
- Los valores numéricos de entrada caben en tipos estándar de 64 bits (`long long` en C++, `long` en Java, enteros de precisión arbitraria en Python).
- Límite de Tiempo de Ejecución: 1.0 a 2.0 segundos
- Límite de Memoria: 256 MB

---

## Input Format
- La primera línea contiene una cadena de texto `S` compuesta por caracteres alfanuméricos.

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
