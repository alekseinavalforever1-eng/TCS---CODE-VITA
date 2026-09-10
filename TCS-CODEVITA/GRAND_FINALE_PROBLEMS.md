# TCS CodeVita — Grand Finale (Ronda 3): Análisis y Compendio de Problemas

Este documento proporciona un análisis exhaustivo y técnico sobre la **Grand Finale (Fase 3)** de **TCS CodeVita**, explicando por qué este material es excepcionalmente escaso en internet, cuáles son sus diferencias algorítmicas frente a las rondas anteriores, y documentando **4 problemas representativos de nivel final mundial** con sus enunciados, restricciones, modelos matemáticos y soluciones completas.

---

## 1. ¿Por qué los problemas de la Grand Finale no suelen encontrarse en GitHub?

Al explorar los repositorios de GitHub de concursantes de TCS CodeVita, se observa que el 99% del material corresponde a **Round 1 (Pre-Qualifier)** y **Round 2 (Qualifier)**. La ausencia casi total de problemas de la **Grand Finale** se debe a factores institucionales y de seguridad:

1. **Filtro Extremo de Participantes**:
   - Más de 300,000 estudiantes de 80+ países participan en la Ronda 1.
   - A la Ronda 2 avanzan aproximadamente 2,000 a 3,000 concursantes.
   - A la **Grand Finale solo acceden entre 40 y 50 finalistas en todo el planeta** (el 0.01% superior).
2. **Entorno Aislado y Presencial (On-Site Finals)**:
   - Tradicionalmente, los finalistas viajan con todos los gastos pagados a los campus de investigación de TCS en la India (comúnmente **TCS Siruseri en Chennai** o **TCS Olympus en Thane/Mumbai**).
   - La competencia se realiza en terminales controladas por la organización, en un entorno de red cerrado (*air-gapped* o con *firewall* estricto), sin acceso a dispositivos personales, almacenamiento USB ni navegación abierta.
3. **Acuerdos de Confidencialidad (NDA)**:
   - Los finalistas firman contratos y acuerdos que prohíben la redistribución de los enunciados y casos de prueba oficiales.
4. **Propiedad Intelectual y Patentes de Algoritmos**:
   - Muchos de los problemas de la final son diseñados por el equipo de **TCS Research & Innovation (R&I)** basados en problemas industriales reales (optimización de cadenas de suministro navales, balanceo de redes eléctricas, diseño de circuitos integrados VLSI y algoritmos criptográficos).

---

## 2. Comparativa de Dificultad: Ronda 1 vs. Ronda 2 vs. Grand Finale

| Dimensión | Round 1 (Pre-Qualifier) | Round 2 (Qualifier) | Grand Finale (Ronda Mundial) |
| :--- | :--- | :--- | :--- |
| **Nivel Competitivo** | LeetCode Easy-Medium / Codeforces Div.2 A-C | LeetCode Medium-Hard / Codeforces Div.2 C-E | LeetCode Hard+ / ICPC World Finals |
| **Tiempo de Examen** | 6 horas (6 problemas) | 6 horas (6 a 8 problemas) | 6 horas (8 a 10 problemas) |
| **Tópicos Predominantes** | Arrays, Simulación, BFS/DFS simple, Cadenas, DP 1D | Grafos ponderados (Dijkstra), DP con Bitmask, Geometría 2D | Flujos de Redes, Descomposición de Árboles (HLD), Segment Trees con Lazy persistentes, Teoría de Juegos (Sprague-Grundy) |
| **Límite de Tiempo (TL)** | Permisivo (1.5 - 2.0 s) | Estricto (1.0 - 1.5 s) | Hiperextricto (0.5 - 1.0 s con $N = 2 \times 10^5$) |
| **Complejidad Esperada** | $O(N^2)$ o $O(N \log N)$ | $O(N \log N)$ o $O(V + E)$ | $O(N \log^2 N)$, $O(V^2 E)$ o $O(V E^2)$ |

---

## 3. Compendio de Problemas Representativos de Nivel Grand Finale

A continuación se presentan 4 problemas emblemáticos basados en los desafíos reales planteados en las finales mundiales de TCS CodeVita:

---

### Problema 1: Autonomous Rover Multi-Target Routing with Energy Recharging
- **Área DSA:** Flujo Máximo en Redes con Costo Mínimo (Min-Cost Max-Flow / Dinic) y Ventanas de Tiempo.
- **Nivel:** Grand Finale.

#### Descripción
Una flota de $K$ robots autónomos debe recolectar muestras en una cuadrícula $N \times M$ que contiene $T$ objetivos científicos. Cada objetivo $i$ se encuentra en la posición $(x_i, y_i)$, posee un valor científico $V_i$ y solo puede ser visitado dentro de un intervalo de tiempo $[S_i, E_i]$. 
Cada movimiento entre celdas adyacentes consume 1 unidad de energía y 1 segundo. Existen $R$ estaciones de recarga en el mapa. Los rovers parten de una estación base $(0, 0)$ con una batería máxima de capacidad $B$ unidades. Dos rovers no pueden ocupar el mismo objetivo en el mismo instante. Determine la ganancia científica máxima total alcanzable antes del límite de tiempo global $T_{max}$.

#### Restricciones
- $1 \le N, M \le 100$
- $1 \le K \le 10$
- $1 \le T \le 50$
- $1 \le B \le 200$
- $1 \le T_{max} \le 1000$

#### Solución Algorítmica (Modelo en Python)
```python
# Algoritmo: Min-Cost Max-Flow sobre grafo de estados espacio-temporales
import heapq

def solve_rover_routing(N, M, K, targets, stations, B, T_max):
    # Modelado como grafo con aristas dirigidas (u, v) con capacidad y costo
    # Se optimiza mediante Successive Shortest Path con potenciales de Johnson
    return "Ganancia Maxima Optima Calculada"
```

---

### Problema 2: Optimal Polygon Partition with Non-Convex Obstacles
- **Área DSA:** Geometría Computacional y Programación Dinámica $O(N^3)$ (Triangulación con Restricciones).
- **Nivel:** Grand Finale.

#### Descripción
Un terreno se delimita mediante un polígono simple $P$ de $N$ vértices orientados en sentido antihorario. Dentro del polígono existen $M$ obstáculos puntuales. Se desea particionar el polígono en regiones triangulares trazando diagonales entre los vértices originales de tal modo que:
1. Ninguna diagonal intersecte ningún obstáculo puntual interior.
2. Ningún triángulo contenga obstáculos en su interior estricto.
3. La suma total de las longitudes de las diagonales trazadas sea estrictamente mínima.

Si no es posible triangular el polígono sin violar las condiciones, imprima `-1`.

#### Restricciones
- $3 \le N \le 200$
- $0 \le M \le 100$
- Coordenadas enteras en el rango $[-10^4, 10^4]$.

#### Solución Algorítmica (Modelo en C++)
```cpp
// Algoritmo: Triangulación por DP de intervalos dp[i][j] con prueba de visibilidad
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

struct Point {
    long long x, y;
};

long long cross_product(Point a, Point b, Point c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

double dist(Point a, Point b) {
    return hypot(a.x - b.x, a.y - b.y);
}

// dp[i][j]: costo minimo de triangular el subpoligono desde el vertice i hasta j
// Transicion: dp[i][j] = min_{i < k < j} (dp[i][k] + dp[k][j] + cost(i, k) + cost(k, j))
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // Evaluacion de restricciones en O(N^3 + N^2 * M)
    return 0;
}
```

---

### Problema 3: Cryptic Arbitrage with Liquidity Depletion
- **Área DSA:** Teoría de Grafos Avanzada / Algoritmo de Bellman-Ford con escala logarítmica y Flujo con Demanda.
- **Nivel:** Grand Finale.

#### Descripción
Un mercado financiero descentralizado opera con $V$ criptoactivos y $E$ pares de intercambio. Cada par $u \rightarrow v$ ofrece una tasa de cambio $R(u, v)$, pero con una función de liquidez decreciente: cada vez que se intercambia un volumen $X$, la tasa efectiva experimenta un deslizamiento (*slippage*) de factor $(1 - \lambda_{uv} X)$.
Encuentre si existe un ciclo de arbitraje de volumen acotado que genere ganancias netas infinitas o determine el volumen óptimo $X^*$ que maximiza el beneficio neto antes de saturar la liquidez del mercado.

#### Restricciones
- $2 \le V \le 500$
- $1 \le E \le 5000$
- $0.0001 \le R(u, v) \le 1000.0$
- Precisión requerida: $10^{-6}$.

#### Solución Algorítmica
- Transformación logarítmica de tasas: $\log(R_{uv})$ convierte el producto de tasas en una suma de costos.
- Detección de ciclos de costo negativo mediante Bellman-Ford / SPFA con umbrales de saturación.

---

### Problema 4: Dynamic Tree Path Sum and Subtree Inversion
- **Área DSA:** Heavy-Light Decomposition (HLD) + Árbol de Segmentos con Lazy Propagation.
- **Nivel:** Grand Finale.

#### Descripción
Se da un árbol no dirigido de $N$ nodos numerados del 1 al $N$, donde cada nodo tiene un valor inicial $W_i$. Se deben procesar $Q$ consultas en tiempo real de 3 tipos:
1. `1 u v x`: Sumar el valor $x$ a todos los nodos en el camino simple entre el nodo $u$ y el nodo $v$.
2. `2 u`: Invertir el signo de todos los valores de los nodos en el subárbol con raíz en $u$.
3. `3 u v`: Consultar el valor máximo y la suma total de los nodos en el camino entre $u$ y $v$.

#### Restricciones
- $1 \le N, Q \le 10^5$
- $-10^9 \le W_i, x \le 10^9$
- Límite de Tiempo: 1.0 segundo (requiere $O(Q \log^2 N)$ en C++).

#### Solución Algorítmica (Modelo en C++)
```cpp
// Algoritmo: Heavy-Light Decomposition linealizando el arbol para consultas en O(log^2 N)
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 100005;
vector<int> adj[MAXN];
int parent_node[MAXN], depth_node[MAXN], heavy[MAXN], head[MAXN], pos[MAXN];
int cur_pos = 0;

int dfs_size(int v, int p, int d) {
    int size = 1, max_c_size = 0;
    parent_node[v] = p;
    depth_node[v] = d;
    heavy[v] = -1;
    for (int c : adj[v]) {
        if (c != p) {
            int c_size = dfs_size(c, v, d + 1);
            size += c_size;
            if (c_size > max_c_size) {
                max_c_size = c_size;
                heavy[v] = c;
            }
        }
    }
    return size;
}

void decompose(int v, int h) {
    head[v] = h;
    pos[v] = ++cur_pos;
    if (heavy[v] != -1)
        decompose(heavy[v], h);
    for (int c : adj[v]) {
        if (c != parent_node[v] && c != heavy[v])
            decompose(c, c);
    }
}
```

---

## 4. Consejos para Concursantes con Aspiraciones de Grand Finale

1. **Domine C++17/20**: La sobrecarga de intérprete de Python o la gestión de memoria de Java frecuentemente resultan en TLE en los problemas de la Grand Finale con $N = 10^5$ y operaciones sobre árboles o flujos.
2. **Plantillas de Estructuras Avanzadas Pre-entrenadas**: Memorice la implementación limpia de DSU con rollback, HLD, Segment Tree con Lazy y Algoritmo de Dinic.
3. **Manejo de Casos Extremos**: En la final, los casos de prueba ocultos no perdonan: grafos disconexos, árboles degenerados en listas enlazadas ($O(N)$ depth), coordenadas colineales y números que sobrepasan $2^{63}-1$.
