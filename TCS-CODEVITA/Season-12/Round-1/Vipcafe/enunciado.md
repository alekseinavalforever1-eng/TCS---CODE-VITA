# Vipcafe

## Problem Description
VIPCafe
Problem Description
Raj is running the busiest cafe in the city. It is also the most visited cafe by VIPs.
VIPs buys costly Beverages. It gives Raj's Cafe high profit. Raj asked his workers to prefer serving VIPs first, because VIPs don't like to wait much time. Whenever a person orders something, Raj gives priority values to the orders and adds it to the queue. The greater the value more important the order is.
The workers start to serve the orders with high priority in queue ensuring that the VIPs get theirs orders quickly. However, those orders having low priority have to wait for a long time in queue,upsetting those people. This reduces the total number of people visiting the cafe and reducing the profit. But, making first come first serve basis reduces the VIPs visiting the cafe. This also reduces the profit.
Raj came up with a new idea to keep the profit high. He introduced a new concept called dynamic priority. The priority of orders changes while in the queue. Raj will maintain a queue of orders with assigned priority,adding new orders at end. The order with high priority in the queue will be served first .When an order got served due to its high priority, the priority of orders in the queue before this will be increased by one. If two orders having same priority ,then the order which was en-queued first will be served first. This strikes a balance between reducing the waiting time of VIPs and also serving other people without much delay.
One day, his friend visited the cafe and ordered something. As usual his order got some priority and got added in the queue. After some time his friend lost his patience and asked when will his order be served. After that, Raj stopped adding new orders to the queue and started calculating after how many orders his friend will get served, considering only orders currently in the queue. Given the queue, can you find after how many orders will Raj's friend get served?
Constraints
2 <= N <= 25
1 <= Priority <= 100
1 <= K <= N
Input
First line contains a Integer 'N' denoting the total orders in cafe which are needed to served.
Second line consist 'N' space separated Integers indicating the priority of orders present in the queue.
Third line consist of integer 'K' indicating the position of his friend in the queue.

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
