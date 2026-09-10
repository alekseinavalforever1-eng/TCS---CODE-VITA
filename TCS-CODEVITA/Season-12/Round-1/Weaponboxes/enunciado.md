# Weaponboxes

## Problem Description
WeaponBoxes
Problem Description
In the border of India, there is a military camp where soldiers stay. The soldiers need weapons during the wars and some weapons are made in India while the others are imported from other countries. One day many boxes of weapons arrived from different countries. These boxes have different numbers assigned to it. These numbers denotes the weight of the boxes. Larger the number on the box, the more will be the weapons inside it. All these boxes are arranged in a line starting from the camp. One day the commander wanted to test the weapons in all the boxes one by one. But he wanted to prioritize the boxes with more weight because when he open that box, the number of weapons will be more. So he will followed the below steps.
He will carry this process in cycles. In each cycle, he will select the first N boxes. From those, every time he will pick the first two boxes and compare them and send the box with lower weight to the end of the line.
At last one box will remain from those N boxes, then the cycle is said to be complete.
He halts this process when the same box remains un-shifted to the end of the line in K consecutive cycles.
For shifting these boxes, he hired labors and they will charge an amount which is equal to the sum of weights of all those boxes except those which are having triangular number weights.
Given an array consisting of weights of all the boxes, two integers N and K, print the amount of money that the commander have to give to workers.
Constraints
1 <= weight of each box <= 10^5
1 <= number of boxes <= 10^4
1 <= N,K <= 10^3
All the elements in the array are distinct.
Input
First line consists of an array denoting the weight of all the boxes.
Second line consists of two space separated integers N and K, denoting the number of boxes he selects in each cycle and number of times a box should remain un-shifted to halt the process.
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
