# Collegerank

## Problem Description
Problem Description
**Question -:** College Admissions are done by allocating a seat to a student based on his/her preference and percentage scored. Students are asked to provide three colleges of their choice. Each college will have a quota of S seats (S can vary per college). Admissions will be processed based on ‘percentage scored’ and availability of seats as per ‘choice of preference’.
Admissions will first be granted based on percentage scored. If there is a tie, on percentage scored, then admission will be granted based on student Id i.e. student with a lower Id will be given preference over student with higher Id.
In Round 1 all admissions will be processed based on students’ choice i.e. if a student is eligible to get admitted in any of the 3 colleges, s/he will have to be admitted. Similarly, it will be binding on the student to get admitted. Obviously, first choice will get first preference, second choice will get second preference and so on.
Round 2 will process all the remaining students (those who didn’t get admitted in Round 1) according to their percentages and in order of maximum availability of seats in colleges.
For E.g.
<college, vacant seats>
C-1, 15
C-22, 14
C-32, 13
C-43, 12
<student-id, percentage>
Student-88, 64.0
Student-103, 63.7
Student-128, 58.28
Here, now Student-88 will get admitted to C-1.
Now, Student-103 could potentially get admitted to C-1 or C-22. Suppose we mandate that ties should be broken in favour of college with least ID, then again Student-103 will get admitted to C-1. Now C-1 has 13 vacant seats whereas C-22 has 14 vacant seats.
Next, Student-128 will get admitted to C-22. Now again C-1, C-22 and C-32 have 13 vacant seats. So, the next three students (hypothetically) will get admitted to C-1, C-22 and C-32 respectively.
**Constraints :**
3<=C<=25
1<=N<=10000
1<=S<=120

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
