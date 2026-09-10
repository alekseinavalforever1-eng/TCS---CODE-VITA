# Bus Count

## Problem Description
BUS COUNT

Description:
-> M * M matrix : represents distance between each locations.
-> Value of i th row & j th column represents distance between i th & j th places.
-> All locations are connected by roads.
-> 1 st location is office (top left element) [0,0].
-> Distance between i th & j th place = Distance between j th & i th place.
-> Number of people on bus is limited.
-> Bus can start from any location.
-> Bus must take only shortest path to office.
-> Bus can pick up employees along it's route.
-> Assume, there is only 1 shortest path between office and each remaining locations.
-> Determine the minimum number of buses required to pick up all employees

Constraints:
1 < M < 12
0 < Distance between locations < 300
0 < Total number of employees < 500

Time Limit:
1 sec

Input:
M                                                -> Number of locations, including office.
M lines consits of M integers seperated by space -> distance matrix.
M-1 space seperated integers                     -> Number of employees at each location, except office.
An integer representing maximum number of people that can travel in bus at 1 time.

Output:
Minimum number of buses required to pick up all employees to the office.

Example:
I/p:
4
0 10 10 30
10 0 30 20
10 30 0 10
30 20 10 0
23 52 11
25

O/p:
4

Explanation:

(Office [0,0])    ----- 10 -----> (Location 1 (23))
   |          \                    /       |
   10          -------- 30 --------        20
   |          /                    \       |
(Location 2 (52)) ----- 10 -----> (Location 3 (11))

Shortest routes:
Location 1: 1 -> 0 (office)
Location 2: 2 -> 0 (office)
Location 3: 3 -> 2 -> 0 (office)

Bus Count:
Location 1: (23) -> 1 bus (23)
Location 2: (52) -> 25 + 25 + 2 -> 2 bus (50) + remaining 2
Location 3: (11) -> 11 -> 11 + remaining 2 at location 2 is picked up along the bus route of Location 3 -> 1 bus (13)

1 + 2 + 1 = 4
Thus, 4 buses are required to pick up all employees to the office.

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
