# E Minimum Distance

## Problem Description
For current cell (r,c) and candidate neighbour (nr,nc), compute minimal
    non-negative integer to add to grid[nr][nc] temporarily so that
    grid[nr][nc] becomes strictly greater than all other unblocked neighbours
    of (r,c). Also compare against current cell's value (per problem note).

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
