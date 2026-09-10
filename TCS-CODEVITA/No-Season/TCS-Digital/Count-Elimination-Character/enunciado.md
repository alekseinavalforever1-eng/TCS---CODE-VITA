# Count Elimination Character

## Problem Description
Find how many characters must be removed in a string of a character series to get a common difference of the count 
of different characters. If no characters need to remove then print "NA".

Input
----------------
aaaaabbc
1

Output
----------------
2

Process
----------------
Number of a : 5
Number of b : 2
Number of c : 1
Common difference : 1

5(a) - 2(b) = 3(extra 3 a are there), so we should remove 3-1= 2(a)
2(b) - 1(c) = 1, no charactres should remove
Hence the output = 2.

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
