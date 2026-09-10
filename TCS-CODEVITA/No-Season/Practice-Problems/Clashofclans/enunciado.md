# Clashofclans

## Problem Description
Question - Clash of Clans
In Clash of Clans, you as a village chief is gearing up for a raid on an enemy village. The success of this
mission depends on assembling the most potent raiding army by selecting troops from various categories.
Each troop type has distinct strengths and weaknesses, and your goal is to create a formidable army that
maximizes overall damage.
To build an army you first need to train them in the "Barracks" which has some capacity (B). Each troop has
some size (S) it occupies in the barrack that trains and increases some amount of damage per second (D)
for each troop.
There are various troops (for e.g. Barbarian, Archer, Giant, Goblin and so on) which belong to some
category C (for e.g. Elixir Troop, Temporary Troop, Super Troops and so on).
To train them you decided to have a versatile army where you select at most one or no troops from each
category of the troops such that it has maximum damage per second and the troops fit within the barrack
size for training.
Constraints
Length of S = D = C
1 <= length of S, D <= 100
1 <= Number of categories <= 20
1 <= B <= Sum of S
Size of the troop <= Size of the Barrack i.e. Si <= B
Input
The first line contains the list of integers denoting damage per second capability Di of the troop.
The second line contains the list of integers denoting the size Si of the troop.
The third line contains a list of integers denoting the category Ciof the troop.
Last line contains an integer denoting the size of the barrack.
Output

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
