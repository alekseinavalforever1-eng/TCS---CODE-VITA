# Path Through Graph

## Problem Description
Path Through Graph
Problem Description
You are given two natural numbers. Imagine these natural numbers as nodes on a graph. On this graph, a number is connected to its largest factor other than itself. You have to find the shortest path between them and print the number of edges on that path.
If the two numbers do not have any common factor, then construct a path through 1. For better understanding refer to the examples below:
Example 1: Input numbers: 2 4
The numbers are directly connected as follows on the graph. 2 is the largest factor of 4, other than itself.
We can also see that there is only on edge between them.
4 <--> 2
Hence the number of edges in shortest path is 1.
Output: 1
Example 2: Input numbers: 18 19
The graph for number 18 and 19 will look like this. Here we have 4 edges in the path.
18 <--> 9 <--> 3 <--> 1 <--> 19
Output: 4
Example 3: Input numbers: 9 9
The number of edges in shortest path is zero since the numbers correspond to the same node.
Output: 0
Constraints
0 < M, N <= 10 ^ 9

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
