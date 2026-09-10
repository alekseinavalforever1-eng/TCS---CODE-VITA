# Round 2 Bonus

## Problem Description
-------------------------
Robust Brick Breaker solver
-------------------------
Assumptions:
- Each non-dot grid cell is a single brick with color letter.
- Dependency rules:
* same-color orthogonally adjacent bricks are mutually dependent (connected component)
* vertical stacking: upper -> lower directed dependency (breaking upper breaks lower)
- Shooter moves in 45-degree diagonal steps between cell centers.
- Starts at row = R-2, column = start_col, direction up-left (-1,-1).
- Bounce counted when hitting a brick (breaking event) or hitting a wall (top/side) or hitting paddle.
- When positive hit-score, we choose to increase paddle length by 2 (if possible) to maximize final length.
- When negative hit-score, we choose to NOT shrink (0) to maximize final length.
- Paddle can be placed arbitrarily before each catch to force left/center/right as available.
- We search all options up to K bounces (K <= 6).
-------------------------

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
