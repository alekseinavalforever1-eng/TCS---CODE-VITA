# Crosswords

## Problem Description
Solution Approach:

- Pick one word at a time from the list of words given in the question
- For that word, find all the possible clues it could be an answer to
- For each clue, guess that the current word is the answer
    - Fetch the current characters in the grid at the clue position
    - If the word chosen overlaps with the current characters, it means it can
        be placed on the grid.
    - Set the word as the answer to the clue
    - Recursively call solve on the next word
    - If that call returns False, it means that by placing the chosen word as
        the answer to the current clue, other words cannot be placed correctly.
        Thus, we have made a mistake and this is not the correct clue for the
        chosen word.
    - Choose the next clue, and repeat this process.
    - When we end up placing the word in its current position, the recursive
        call to solve(...) will have generated `True` (since it would have found
        a way to place all the remaining words in their correct positions; since
        our chosen word is in its correct position)

---

## Constraints
- $1 \le N \le 10^5$ (o límites de dimensión equivalentes)
- Los valores numéricos de entrada caben en tipos estándar de 64 bits (`long long` en C++, `long` en Java, enteros de precisión arbitraria en Python).
- Límite de Tiempo de Ejecución: 1.0 a 2.0 segundos
- Límite de Memoria: 256 MB

---

## Input Format
- La primera línea contiene dos enteros `R` y `C`, indicando las dimensiones de la matriz (filas y columnas).
- Las siguientes `R` líneas contienen `C` elementos enteros o caracteres separados por espacio.

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
