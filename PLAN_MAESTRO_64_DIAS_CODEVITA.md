# ⚔️ Plan de Choque Espartano: 64 Días para la Ronda 1 de TCS CodeVita

> **Objetivo:** Dominio absoluto de **C++17 (g++ 9.3.0)**, los **150 problemas del NeetCode Roadmap**, los **3 libros canónicos de Programación Competitiva** y el banco integral de problemas de **`TCS-CODEVITA/`**, asegurando la clasificación a la Ronda 2 y la máxima oferta laboral (**TCS Digital / Innovator**).

---

## 🧭 Los 4 Pilares del Plan Integrado

Intentar estudiar estas 4 áreas por separado en 64 días causaría agotamiento. El secreto del plan radica en la **Sinergia Temática Diaria**: lo que lees por la mañana en el libro de CP lo aplicas a mediodía en los patrones de NeetCode y lo llevas al combate por la noche en los problemas reales de CodeVita.

```
       ┌────────────────────────────────────────────────────────┐
       │                 RUTINA DIARIA DE 7-8 HORAS             │
       ├────────────────────────────────────────────────────────┤
       │ 1. MAÑANA   (2.0 hrs) ──▶ Lectura de CP Books + C++17  │
       │ 2. MEDIODÍA (2.5 hrs) ──▶ NeetCode 150 Roadmap en C++  │
       │ 3. NOCHE    (3.0 hrs) ──▶ Banco TCS CodeVita + Judge   │
       └────────────────────────────────────────────────────────┘
```

---

## 📚 Bibliografía Canónica Seleccionada

1. **Libro 1:** 📘 ***Competitive Programmer's Handbook*** (Antti Laaksonen, CSES / Univ. of Helsinki).  
   *La referencia #1 en C++17 para CP: ultra directa, sin relleno, código conciso y algoritmos optimizados.*
2. **Libro 2:** 📕 ***Competitive Programming 4 — Book 1 & Book 2*** (Steven Halim, Felix Halim & Suhendry).  
   *La biblia del entrenamiento ICPC/IOI: patrones de problemas, clasificación sistemática y estructuras no triviales.*
3. **Libro 3:** 📗 ***Principles of Algorithmic Problem Solving*** (Johan Sannemo, KTH) o ***Guide to Competitive Programming*** (Laaksonen, Springer).  
   *Profundización en matemáticas discretas, invariantes, sweep-line y diseño algorítmico riguroso.*

---

## ⚡ Inventario de C++17 (g++ 9.3.0) que Debes Dominar

* **I/O y Parsing:** `ios_base::sync_with_stdio(false); cin.tie(NULL);`, lectura con `getline`, despiece con `stringstream`, lectura hasta EOF con `while (cin >> x)`.
* **Contenedores de la STL:**
  * Secuenciales: `vector`, `deque`, `array`, `list`.
  * Adaptadores: `stack`, `queue`, `priority_queue` (con comparadores lambda y `greater<T>`).
  * Asociativos (Árboles Rojo-Negro): `set`, `multiset`, `map`, `multimap` ($O(\log N)$).
  * No ordenados (Hash Tables): `unordered_set`, `unordered_map` ($O(1)$ amortizado).
  * Bitwise: `std::bitset<N>`, funciones intrínsecas GCC (`__builtin_popcountll`, `__builtin_clzll`).
* **Algoritmos STL (`<algorithm>` y `<numeric>`):**
  * Búsquedas: `lower_bound`, `upper_bound`, `binary_search`.
  * Ordenamiento y permutaciones: `sort`, `stable_sort`, `next_permutation`, `prev_permutation`.
  * Manipulación: `reverse`, `rotate`, `unique`, `min_element`, `max_element`, `nth_element`.
  * Reducción: `accumulate`, `iota`, `std::gcd`, `std::lcm`.
* **Manejo Numérico y Desbordamiento:**
  * Enteros de 64 bits: `long long` (hasta $9 \times 10^{18}$).
  * Enteros de 128 bits de GCC: `__int128_t` (útil en CodeVita para multiplicaciones modulares gigantescas).
  * Constantes seguras: `const long long INF = 1e18;`, `const int MOD = 1e9 + 7;`.

---

## 📅 Calendario Detallado de 64 Días

### 🟢 FASE 1: Días 1 a 14 — C++17 STL, Arrays, Two Pointers, Sliding Window y MockVita

#### Semana 1: Fundamentos de C++17, Arrays, Two Pointers y Primeros MockVita
- [ ] **Día 1: Inmersión en C++17 y Fast I/O**
  - *Libro:* Laaksonen Caps. 1 y 2 (Entorno, Complejidad temporal, optimizaciones).
  - *C++:* Plantilla universal, Fast I/O, `vector`, `pair`, `tuple`, rangos básicos.
  - *NeetCode:* Contains Duplicate, Valid Anagram, Two Sum.
  - *CodeVita:* [`[OFICIAL]-Swayamvar`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/MockVita-2/[OFICIAL]-Swayamvar/) y [`[OFICIAL]-Hop-Game`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/MockVita-2/[OFICIAL]-Hop-Game/).
- [ ] **Día 2: Hashing y Conteo de Frecuencias**
  - *Libro:* Laaksonen Cap. 4 (Data Structures - set, map, unordered_map) + Halim CP4 Cap. 2.1-2.2.
  - *C++:* `unordered_map`, `unordered_set`, prevención de colisiones en GCC.
  - *NeetCode:* Group Anagrams, Top K Frequent Elements, Encode and Decode Strings.
  - *CodeVita:* [`[OFICIAL]-Bottle-Necks`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Bottle-Necks/) y [`[OFICIAL]-Lexi-String`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Lexi-String/).
- [ ] **Día 3: Patrones de Arrays Avanzados y Prefijos**
  - *Libro:* Sannemo Cap. 2 (Data structures) + Laaksonen Cap. 9 (Range queries intro).
  - *C++:* Prefix Sum 1D y 2D, `std::accumulate`, `std::partial_sum`.
  - *NeetCode:* Product of Array Except Self, Valid Sudoku, Longest Consecutive Sequence.
  - *CodeVita:* [`[OFICIAL]-Chakravyuha`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-7/Round-1/[OFICIAL]-Chakravyuha/) y [`Accicoequipairs`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Accicoequipairs/).
- [ ] **Día 4: Two Pointers (Dos Punteros)**
  - *Libro:* Halim CP4 Cap. 3.2 (Complete Search & Two Pointers).
  - *C++:* Punteros opuestos, punteros en misma dirección, ordenamiento in-place con `sort`.
  - *NeetCode:* Valid Palindrome, Two Sum II, 3Sum.
  - *CodeVita:* [`Pairwithdifferencek`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Pairwithdifferencek/) y [`Sheldoncooperparadigmbeverages`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Sheldoncooperparadigmbeverages/).
- [ ] **Día 5: Two Pointers con Áreas e Intervalos**
  - *Libro:* Laaksonen Cap. 3 (Sorting: two pointers method).
  - *C++:* `std::max`, `std::min`, iteradores de contenedores reversos `rbegin()`, `rend()`.
  - *NeetCode:* Container With Most Water, Trapping Rain Water.
  - *CodeVita:* [`[OFICIAL]-Overlapping-Boxes`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/MockVita-2/[OFICIAL]-Overlapping-Boxes/) e [`Intersectionof2sortedarrays`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Intersectionof2sortedarrays/).
- [ ] **Día 6: Sliding Window (Ventana Deslizante) I**
  - *Libro:* Sannemo Cap. 3 (Two Pointers and Sliding Window).
  - *C++:* Ventana de tamaño fijo vs tamaño dinámico, mapas de frecuencias de ventana.
  - *NeetCode:* Best Time to Buy and Sell Stock, Longest Substring Without Repeating Characters.
  - *CodeVita:* [`[OFICIAL]-Counting-Rock-Sample`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-6/Round-1/[OFICIAL]-Counting-Rock-Sample/) y [`Longestprogressiveseq`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Longestprogressiveseq/).
- [ ] **Día 7: Sliding Window II y Repaso Semanal**
  - *NeetCode:* Longest Repeating Character Replacement, Permutation in String, Minimum Window Substring.
  - *CodeVita:* [`[OFICIAL]-Minimumgifts`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-Minimumgifts/) y [`[OFICIAL]-Railwaystation`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-Railwaystation/).
  - *Simulador:* Ejecutar `codevita_judge.py` sobre todos los problemas completados en la semana.

#### Semana 2: Pilas, Colas, Búsqueda Binaria y Pre-Qualifier Histórico (Seasons 6 y 7)
- [ ] **Día 8: Pilas y Evaluación de Expresiones**
  - *Libro:* Halim CP4 Cap. 2.2 (Linear Data Structures with Built-in Libraries).
  - *C++:* `std::stack`, parsing de paréntesis y expresiones postfijas.
  - *NeetCode:* Valid Parentheses, Min Stack, Evaluate Reverse Polish Notation.
  - *CodeVita:* [`[OFICIAL]-Holes-And-Balls`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Holes-And-Balls/) y [`[OFICIAL]-Base-6`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-6/Round-1/[OFICIAL]-Base-6/).
- [ ] **Día 9: Monotonic Stack (Pila Monótona)**
  - *Libro:* Laaksonen Cap. 8 (Amortized Analysis - Nearest smaller elements).
  - *C++:* Siguiente elemento mayor/menor en $O(N)$, optimización con arreglos planos.
  - *NeetCode:* Generate Parentheses, Daily Temperatures, Car Fleet, Largest Rectangle in Histogram.
  - *CodeVita:* [`[OFICIAL]-Date-Time`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/MockVita-2/[OFICIAL]-Date-Time/) y [`[OFICIAL]-Digital-Time`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-6/Round-1/[OFICIAL]-Digital-Time/).
- [ ] **Día 10: Búsqueda Binaria Clásica y STL**
  - *Libro:* Laaksonen Cap. 3 (Binary Search) + Halim CP4 Cap. 3.3.
  - *C++:* `lower_bound`, `upper_bound`, evitar desbordamiento con `mid = low + (high - low) / 2`.
  - *NeetCode:* Binary Search, Search a 2D Matrix, Koko Eating Bananas.
  - *CodeVita:* [`[OFICIAL]-Kth-Largest-Factor`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-6/Round-1/[OFICIAL]-Kth-Largest-Factor/) y [`[OFICIAL]-Bank-Compare`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-7/Round-1/[OFICIAL]-Bank-Compare/).
- [ ] **Día 11: Binary Search on Answer (Búsqueda sobre la Respuesta)**
  - *Libro:* Sannemo Cap. 5 (Binary Search on Monotonic Functions).
  - *C++:* Funciones predicado booleanas `bool check(long long val)`.
  - *NeetCode:* Find Minimum in Rotated Sorted Array, Search in Rotated Sorted Array, Time Based Key-Value Store, Median of Two Sorted Arrays.
  - *CodeVita:* [`[OFICIAL]-Bride-Hunting`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-7/Round-1/[OFICIAL]-Bride-Hunting/) y [`Televisionsets`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Televisionsets/).
- [ ] **Día 12: Listas Enlazadas y Punteros Rápidos/Lentos**
  - *Libro:* Halim CP4 Cap. 2.2.
  - *C++:* Estructuras con punteros, `struct Node`, gestión de memoria, referencias `Node*&`.
  - *NeetCode:* Reverse Linked List, Merge Two Sorted Lists, Reorder List, Remove Nth Node From End of List.
  - *CodeVita:* [`[OFICIAL]-String-Rotation`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-7/Round-1/[OFICIAL]-String-Rotation/) y [`[OFICIAL]-The-Great-Chase`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-6/Round-1/[OFICIAL]-The-Great-Chase/).
- [ ] **Día 13: Listas Enlazadas Complejas y Operaciones LRU**
  - *NeetCode:* Copy List with Random Pointer, Add Two Numbers, Linked List Cycle, Find the Duplicate Number, LRU Cache, Merge k Sorted Lists, Reverse Nodes in k-Group.
  - *CodeVita:* [`[OFICIAL]-Jumping-Beetle`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-6/Round-1/[OFICIAL]-Jumping-Beetle/) y [`[OFICIAL]-Bad-Permutation`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/MockVita-2/[OFICIAL]-Bad-Permutation/).
- [ ] **Día 14: Simulación de Mitad de Fase y Evaluación con Juez**
  - *Meta:* Revisar los 20 primeros problemas de [CHECKLIST_ORDEN_EJERCICIOS.md](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/CHECKLIST_ORDEN_EJERCICIOS.md).
  - *Práctica:* Correr `python codevita_judge.py` en lote para verificar que todas tus soluciones compilan con `-std=c++17`.

---

### 🟡 FASE 2: Días 15 a 30 — Árboles, Heaps, Backtracking y Season 8/9

#### Semana 3: Árboles Binarios, BST, Heaps y Colas de Prioridad
- [ ] **Día 15: Fundamentos de Árboles y Recorridos DFS**
  - *Libro:* Laaksonen Cap. 14 (Tree Algorithms - Tree traversal) + Halim CP4 Cap. 2.3.
  - *C++:* Recursión de árbol, pasaje por referencia de estados, cálculo de alturas y diámetros.
  - *NeetCode:* Invert Binary Tree, Maximum Depth of Binary Tree, Diameter of Binary Tree, Balanced Binary Tree.
  - *CodeVita:* [`[OFICIAL]-Coins-Required`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Coins-Required/) y [`[OFICIAL]-Clock-Angle`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Clock-Angle/).
- [ ] **Día 16: Comparación de Subárboles y Ancestros Comunes (LCA)**
  - *Libro:* Laaksonen Cap. 14 (Lowest Common Ancestor).
  - *NeetCode:* Same Tree, Subtree of Another Tree, Lowest Common Ancestor of a BST.
  - *CodeVita:* [`[OFICIAL]-All-Party-Meet`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-All-Party-Meet/) y [`[OFICIAL]-Dole-Out-Cadbury`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Dole-Out-Cadbury/).
- [ ] **Día 17: Recorridos BFS por Niveles y Vistas de Árbol**
  - *C++:* `std::queue<TreeNode*>`, procesamiento nivel por nivel con `int sz = q.size()`.
  - *NeetCode:* Binary Tree Level Order Traversal, Binary Tree Right Side View, Count Good Nodes in Binary Tree.
  - *CodeVita:* [`[OFICIAL]-Path-Through-Graph`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-Path-Through-Graph/) y [`[OFICIAL]-Digit-Pairs`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-Digit-Pairs/).
- [ ] **Día 18: Validación de BST y Serialización**
  - *NeetCode:* Validate Binary Search Tree, Kth Smallest Element in a BST, Construct Binary Tree from Preorder and Inorder Traversal, Binary Tree Maximum Path Sum, Serialize and Deserialize Binary Tree.
  - *CodeVita:* [`Grooving-Monkeys`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/Grooving-Monkeys/) y [`[OFICIAL]-Constellation`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-Constellation/).
- [ ] **Día 19: Heaps / Priority Queues y Estructura Heapq**
  - *Libro:* Laaksonen Cap. 4 (Priority Queue) + Halim CP4 Cap. 2.4.
  - *C++:* `priority_queue<int>`, `priority_queue<int, vector<int>, greater<int>>`, custom struct con `operator<`.
  - *NeetCode:* Kth Largest Element in a Stream, Last Stone Weight, K Closest Points to Origin.
  - *CodeVita:* [`[OFICIAL]-Minimizethesum`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-Minimizethesum/) y [`Collectingcandiesheapq`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Collectingcandiesheapq/).
- [ ] **Día 20: Heaps Avanzados y Mediana Continua**
  - *NeetCode:* Kth Largest Element in an Array, Task Scheduler, Design Twitter, Find Median from Data Stream.
  - *CodeVita:* [`[OFICIAL]-Collecting-Candies`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Collecting-Candies/) y [`[OFICIAL]-New-ATM-Design`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-New-ATM-Design/).
- [ ] **Día 21: Tries (Prefix Trees)**
  - *Libro:* Laaksonen Cap. 26 (Trie structures).
  - *C++:* Arreglos de punteros `Node* child[26]` o `int child[MAXN][26]`.
  - *NeetCode:* Implement Trie (Prefix Tree), Design Add and Search Words Data Structure, Word Search II.
  - *CodeVita:* [`Wordsearch`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Wordsearch/) y [`[OFICIAL]-Cross-Word`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-7/Round-1/[OFICIAL]-Cross-Word/).

#### Semana 4: Backtracking, Búsqueda Exhaustiva y Poda
- [ ] **Día 22: Subconjuntos y Permutaciones Básicas**
  - *Libro:* Laaksonen Cap. 5 (Complete Search - Generating subsets and permutations).
  - *C++:* Recursión con estado, `std::next_permutation`, poda con `return`.
  - *NeetCode:* Subsets, Subsets II, Permutations.
  - *CodeVita:* [`[OFICIAL]-Exchange-Digits`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Exchange-Digits/) y [`Crosswords`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Crosswords/).
- [ ] **Día 23: Sumas de Combinaciones y Poda Aritmética**
  - *NeetCode:* Combination Sum, Combination Sum II, Letter Combinations of a Phone Number.
  - *CodeVita:* [`[OFICIAL]-Petrol-Pump`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Petrol-Pump/) y [`Petrolpumpnotdone`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Petrolpumpnotdone/).
- [ ] **Día 24: Particiones y Problemas N-Queens**
  - *Libro:* Laaksonen Cap. 5 (Backtracking - Pruning the search).
  - *C++:* Bitmasking para marcar diagonales y columnas en $O(1)$.
  - *NeetCode:* Word Search, Palindrome Partitioning, N-Queens.
  - *CodeVita:* [`Nqueensproblem`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Nqueensproblem/) y [`Wanderpaths`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Wanderpaths/).
- [ ] **Día 25: Grafos I — Representación, BFS y DFS en Matrices**
  - *Libro:* Laaksonen Cap. 11 (Basics of graphs - Representations & Traversal) + Halim CP4 Cap. 4.1-4.2.
  - *C++:* Arreglos de adyacencia `vector<vector<int>> adj`, `int dx[] = {-1, 0, 1, 0}`, `int dy[] = {0, 1, 0, -1}`.
  - *NeetCode:* Number of Islands, Max Area of Island, Clone Graph.
  - *CodeVita:* [`[OFICIAL]-Island`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Island/) e [`Islands`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Islands/).
- [ ] **Día 26: Multi-source BFS y Propagación de Estados**
  - *Libro:* Halim CP4 Cap. 4.2 (Flood Fill & BFS on Grid).
  - *NeetCode:* Walls and Gates, Rotting Oranges, Pacific Atlantic Water Flow.
  - *CodeVita:* [`[OFICIAL]-Jurrassic-Park`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-7/Round-1/[OFICIAL]-Jurrassic-Park/) y [`[OFICIAL]-Friendcircle`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Friendcircle/).
- [ ] **Día 27: DSU (Disjoint Set Union / Union-Find)**
  - *Libro:* Laaksonen Cap. 15 (Spanning trees - Kruskal & Union-find structure).
  - *C++:* Implementación estándar de DSU con unión por rango y compresión de caminos.
  - *NeetCode:* Redundant Connection, Number of Connected Components in an Undirected Graph, Graph Valid Tree.
  - *CodeVita:* [`Castlearbitrage`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Castlearbitrage/) y [`[OFICIAL]-Death-Battle`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/MockVita-2/[OFICIAL]-Death-Battle/).
- [ ] **Día 28: Ordenamiento Topológico (Topological Sort en DAG)**
  - *Libro:* Laaksonen Cap. 16 (Directed graphs - Topological sorting).
  - *C++:* Algoritmo de Kahn con colas de grado de entrada `in_degree`.
  - *NeetCode:* Course Schedule, Course Schedule II.
  - *CodeVita:* [`Longesttaskpath`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-10/Round-1/Longesttaskpath/) y [`[OFICIAL]-Primetimeagain`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-9/Round-1/[OFICIAL]-Primetimeagain/).
- [ ] **Día 29: Detección de Ciclos y Transformación de Estados**
  - *NeetCode:* Surrounded Regions, Word Ladder.
  - *CodeVita:* [`[OFICIAL]-Paper-Generation`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/MockVita-2/[OFICIAL]-Paper-Generation/) y [`[OFICIAL]-Colliding-Cannon`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-7/Round-1/[OFICIAL]-Colliding-Cannon/).
- [ ] **Día 30: Examen de Bloque (Simulación con Límites de Tiempo)**
  - Resolver 3 problemas de Seasons 8 y 9 cronometrando 45 min por ejercicio usando [codevita_judge.py](file:///c:/Users/Aleks/Carrera/TCS/Repos/codevita_judge.py).

---

### 🟠 FASE 3: Días 31 a 48 — Caminos Mínimos, Programación Dinámica y Seasons 10 a 12

#### Semana 5: Algoritmos de Grafos Avanzados y DP 1D
- [ ] **Día 31: Caminos Mínimos (Dijkstra)**
  - *Libro:* Laaksonen Cap. 13 (Shortest paths - Dijkstra's algorithm) + Halim CP4 Cap. 4.4.
  - *C++:* `priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;`
  - *NeetCode:* Network Delay Time, Reconstruct Itinerary.
  - *CodeVita:* [`Minproductarray`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Minproductarray/) y [`Distributebooks`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Distributebooks/).
- [ ] **Día 32: Bellman-Ford y Floyd-Warshall**
  - *Libro:* Laaksonen Cap. 13 (Bellman-Ford, SPFA, Floyd-Warshall).
  - *C++:* Detección de ciclos negativos, matriz de distancias `dist[i][j]`.
  - *NeetCode:* Min Cost to Connect All Points, Cheapest Flights Within K Stops.
  - *CodeVita:* [`[OFICIAL]-Bank-Statement`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/MockVita-2/[OFICIAL]-Bank-Statement/) y [`Distribute-Books`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/Distribute-Books/).
- [ ] **Día 33: Fundamentos de DP 1D (Mochila y Subestructuras Óptimas)**
  - *Libro:* Laaksonen Cap. 7 (Dynamic Programming - Coin problem, Longest increasing subsequence) + Halim CP4 Cap. 3.5.
  - *C++:* Memoización top-down vs tabulación bottom-up, optimización de espacio a $O(1)$ variables.
  - *NeetCode:* Climbing Stairs, Min Cost Climbing Stairs, House Robber, House Robber II.
  - *CodeVita:* [`[OFICIAL]-Uncertain-Step`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-8/Round-1/[OFICIAL]-Uncertain-Step/) y [`Uncertainsteps`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Uncertainsteps/).
- [ ] **Día 34: DP en Subcadenas y Palíndromos**
  - *NeetCode:* Longest Palindromic Substring, Palindromic Substrings, Decode Ways.
  - *CodeVita:* [`[OFICIAL]-Three-Palindrome`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Three-Palindrome/) y [`Pascalpyramid`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Pascalpyramid/).
- [ ] **Día 35: Familia Knapsack (Mochila 0/1 y No Acotada)**
  - *Libro:* Laaksonen Cap. 7 (Knapsack problems).
  - *C++:* Arreglos 1D iterando de atrás hacia adelante para evitar reutilización.
  - *NeetCode:* Coin Change, Maximum Product Subarray, Word Break.
  - *CodeVita:* [`Digitpairs`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Digitpairs/) y [`Decryptthecrypt`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Decryptthecrypt/).
- [ ] **Día 36: LIS (Longest Increasing Subsequence) en $O(N \log N)$**
  - *Libro:* Laaksonen Cap. 7 (Longest increasing subsequence with binary search).
  - *C++:* `vector<int> tails; auto it = lower_bound(tails.begin(), tails.end(), x);`
  - *NeetCode:* Longest Increasing Subsequence, Partition Equal Subset Sum.
  - *CodeVita:* [`[OFICIAL]-Consecutive-Prime-Sum`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Consecutive-Prime-Sum/) y [`[OFICIAL]-Civilwar`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Civilwar/).
- [ ] **Día 37: Repaso de DP 1D y Casos Borde de CodeVita**
  - Resolver problemas de Season 10 Round 1: [`Classarrangement`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-10/Round-1/Classarrangement/) y [`Dicegame`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-10/Round-1/Dicegame/).

#### Semana 6: Programación Dinámica 2D, Grillas y Season 11/12
- [ ] **Día 38: DP en Grillas 2D (Caminos y Costos Mínimos)**
  - *Libro:* Laaksonen Cap. 7 (Paths in a grid).
  - *C++:* `vector<vector<int>> dp(R, vector<int>(C, 0));`
  - *NeetCode:* Unique Paths, Longest Common Subsequence.
  - *CodeVita:* [`[OFICIAL]-Housesproblem`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Housesproblem/) y [`[OFICIAL]-Maneuveringcave`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Maneuveringcave/).
- [ ] **Día 39: DP de Alineamiento y Distancia de Edición (Edit Distance)**
  - *Libro:* Halim CP4 Cap. 3.5 (String DP).
  - *NeetCode:* Best Time to Buy and Sell Stock with Cooldown, Coin Change II, Target Sum.
  - *CodeVita:* [`[OFICIAL]-Curtains-Aqua-Black`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Curtains-Aqua-Black/) y [`[OFICIAL]-Cyclic-Array-Rotation`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Cyclic-Array-Rotation/).
- [ ] **Día 40: DP de Intervalos y Subcadenas Intercaladas**
  - *NeetCode:* Interleaving String, Edit Distance.
  - *CodeVita:* [`[OFICIAL]-Jugs-And-Cups`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-11/Round-1/[OFICIAL]-Jugs-And-Cups/) y [`[OFICIAL]-Countingrocks`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Countingrocks/).
- [ ] **Día 41: DP Avanzado con Matrices de Transición y Cadenas**
  - *NeetCode:* Longest Increasing Path in a Matrix, Distinct Subsequences.
  - *CodeVita:* [`Matrixrotations`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/Matrixrotations/) y [`[OFICIAL]-Philalandcoins`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Philalandcoins/).
- [ ] **Día 42: DP de Expresiones y Comodines (Burst Balloons / Wildcards)**
  - *NeetCode:* Burst Balloons, Regular Expression Matching.
  - *CodeVita:* [`[OFICIAL]-Max`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-12/Round-1/[OFICIAL]-Max/) y [`[OFICIAL]-Buzz-Day-Sale`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-12/Round-1/[OFICIAL]-Buzz-Day-Sale/).
- [ ] **Día 43: Teoría de Números y Criba de Eratóstenes en C++**
  - *Libro:* Laaksonen Cap. 21 (Number theory - Primes, Sieve of Eratosthenes, Euclid's algorithm).
  - *C++:* Criba rápida en $O(N \log \log N)$, factorización en $O(\sqrt{N})$, exponenciación modular rápida en $O(\log B)$.
  - *CodeVita:* [`[OFICIAL]-Divinedivisors`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Divinedivisors/) y [`[OFICIAL]-Primeconstruction`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Primeconstruction/).
- [ ] **Día 44: Aritmética Modular, Inversos y Combinatoria**
  - *Libro:* Laaksonen Cap. 22 (Combinatorics - Binomial coefficients, Pascal's triangle).
  - *C++:* Pequeño Teorema de Fermat para inverso modular: $A^{-1} \equiv A^{MOD-2} \pmod{MOD}$.
  - *CodeVita:* [`[OFICIAL]-Round-Table-Conference`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Round-Table-Conference/) y [`[OFICIAL]-Supermarket-Pricing`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Supermarket-Pricing/).
- [ ] **Día 45: Simulación Semanal Season 12 Round 1**
  - Resolver problemas de Season 12: [`[OFICIAL]-Shannon-Circuits`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-12/Round-1/[OFICIAL]-Shannon-Circuits/) y [`[OFICIAL]-Bubble-Trouble`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-12/Round-2/[OFICIAL]-Bubble-Trouble/).
- [ ] **Día 46 al 48: Limpieza de Cola de Ejercicios y Casos Borde**
  - Testear con `codevita_judge.py` todos los problemas de Season 11 y Season 12.

---

### 🔴 FASE 4: Días 49 a 60 — Season 13 (La Edición Más Reciente), Greedy, Geometría y Sweep-Line

#### Semana 7: Greedy, Intervalos, Geometría y Season 13 Round 1 (Parte 1)
- [ ] **Día 49: Algoritmos Voraces (Greedy) y Heurísticas**
  - *Libro:* Laaksonen Cap. 6 (Greedy algorithms - Scheduling, Tasks and deadlines).
  - *NeetCode:* Maximum Subarray, Jump Game, Jump Game II, Gas Station.
  - *CodeVita:* [`[OFICIAL]-F1-Logistics`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-F1-Logistics/) y [`[OFICIAL]-Order-It`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-Order-It/).
- [ ] **Día 50: Greedy con Ordenamiento y Subcadenas**
  - *NeetCode:* Hand of Straights, Merge Triplets to Form Target Triplet, Partition Labels, Valid Parenthesis String.
  - *CodeVita:* [`[OFICIAL]-Enthusiastic-Vijay`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-Enthusiastic-Vijay/) y [`[OFICIAL]-Max-Match-Box`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-Max-Match-Box/).
- [ ] **Día 51: Manejo de Intervalos y Sweep-Line**
  - *Libro:* Laaksonen Cap. 28 (Sweep-line algorithms).
  - *C++:* Eventos de entrada y salida con pares `(x, tipo)`, ordenamiento de eventos.
  - *NeetCode:* Insert Interval, Merge Intervals, Non-overlapping Intervals, Meeting Rooms, Meeting Rooms II, Minimum Interval to Include Each Query.
  - *CodeVita:* [`[OFICIAL]-Minimum-Distance`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-Minimum-Distance/) y [`[OFICIAL]-Path-Finder`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-Path-Finder/).
- [ ] **Día 52: Geometría Computacional 2D (Puntos, Vectores y Producto Cruz)**
  - *Libro:* Laaksonen Cap. 29 (Geometry - Points and lines, Polygon area) + Halim CP4 Cap. 7.
  - *C++:* `struct Point { long long x, y; };`, producto cruz para orientación izquierda/derecha.
  - *NeetCode:* Rotate Image, Spiral Matrix, Set Matrix Zeroes.
  - *CodeVita:* [`[OFICIAL]-Maxareapolygon`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-Maxareapolygon/) y [`[OFICIAL]-On-A-Cube`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/No-Season/Practice-Problems/[OFICIAL]-On-A-Cube/).
- [ ] **Día 53: Geometría Avanzada (Área de Polígonos con Fórmula de Shoelace y Cubos 3D)**
  - *NeetCode:* Happy Number, Plus One, Pow(x, n), Multiply Strings, Detect Squares.
  - *CodeVita:* [`[OFICIAL]-Cubemid`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-2/[OFICIAL]-Cubemid/) y [`[OFICIAL]-Wall-Shooter`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-2/[OFICIAL]-Wall-Shooter/).
- [ ] **Día 54: Manipulación de Bits y Trucos de C++**
  - *Libro:* Laaksonen Cap. 10 (Bit manipulation - Bit operations, Representing sets).
  - *C++:* `x & (-x)` (LSB), `x | (1 << k)`, `x & ~(1 << k)`, `__builtin_popcount`.
  - *NeetCode:* Single Number, Number of 1 Bits, Counting Bits, Reverse Bits, Missing Number, Sum of Two Integers, Reverse Integer.
  - *CodeVita:* [`[OFICIAL]-Sai-Mini-Project`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-Sai-Mini-Project/) y [`[OFICIAL]-Uno-Game`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-1/[OFICIAL]-Uno-Game/).
- [ ] **Día 55: Season 13 Round 2 — El Nivel Máximo de Clasificación**
  - Resolver:
    - [`[OFICIAL]-Ascii-Homes`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-2/[OFICIAL]-Ascii-Homes/)
    - [`[OFICIAL]-Bubble-Shooter`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-2/[OFICIAL]-Bubble-Shooter/)
    - [`[OFICIAL]-Isha-And-Nisha`](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/Season-13/Round-2/[OFICIAL]-Isha-And-Nisha/)

#### Semana 8: Grand Finale, Casos Extremos y Verificación Final del Catálogo
- [ ] **Día 56: Compendio de la Grand Finale I (Flujos y Matching Máximo)**
  - *Lectura:* [TCS-CODEVITA/GRAND_FINALE_PROBLEMS.md](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/GRAND_FINALE_PROBLEMS.md).
  - *Algoritmos:* Dinic's Algorithm para flujo máximo, Hopcroft-Karp para emparejamiento bipartito.
  - *Práctica:* Implementación de plantilla de flujo en C++17.
- [ ] **Día 57: Compendio de la Grand Finale II (Heavy-Light Decomposition & Hashing 2D)**
  - *Algoritmos:* Consultas sobre caminos en árboles con HLD, Rolling Hash 2D para submatrices.
  - *Práctica:* Problemas 3 y 4 de la Grand Finale.
- [ ] **Día 58: Verificación y Cierre de los 60 Clásicos**
  - Revisar [CORRELACION_60_PROBLEMAS.md](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/CORRELACION_60_PROBLEMAS.md).
  - Garantizar que los 60 problemas clásicos tienen su `[x]` marcado y compilado en C++.
- [ ] **Día 59: Auditoría Masiva con `codevita_judge.py`**
  - Ejecutar el script contra todas las carpetas marcadas con `[OFICIAL]-` en el repositorio.
- [ ] **Día 60: Consolidación de Bitácora de Errores**
  - Revisar los 15 errores más comunes cometidos durante las semanas 1 a 8 (desbordamiento de enteros, formatos de salto de línea, empates en ordenamiento).

---

### 🏁 SEMANA DE SIMULACROS REALES (Días 61 a 64)

- [ ] **Día 61: Simulacro Oficial #1 (6 Horas continuas - Temporada 11)**
  - Seleccionar 6 problemas al azar de Season 11.
  - Cronómetro de 360 minutos sin mirar soluciones.
  - Objetivo: Mínimo 3 problemas resueltos en AC.
- [ ] **Día 62: Simulacro Oficial #2 (6 Horas continuas - Temporada 12)**
  - Seleccionar 6 problemas de Season 12 Round 1.
  - Evaluar estrategia de descarte rápido: identificar en los primeros 20 min cuáles son los 2 problemas más accesibles.
- [ ] **Día 63: Simulacro Oficial #3 (6 Horas continuas - Temporada 13)**
  - Simular la Ronda 1 de la Season 13 completa.
  - Calibrar tiempos y verificar que no haya fugas de memoria ni TLEs.
- [ ] **Día 64: Tapering, Preparación Mental y Checklist Pre-Competencia**
  - Repaso de la plantilla de Fast I/O de C++17.
  - Revisión del documento [TCS-CODEVITA/GUIA_COMPILADOR_GCC_9_3_0.md](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/GUIA_COMPILADOR_GCC_9_3_0.md).
  - Descanso adecuado previo al inicio oficial de la Ronda 1.

---

## 🎯 Protocolo Diario de Estudio y Reglas Espartanas

1. **Regla de los 30 Minutos de Bloqueo:**  
   Si llevas 30 minutos sin escribir una línea de código ni entender cómo atacar el problema, abre la ficha técnica [teoria.md](file:///c:/Users/Aleks/Carrera/TCS/Repos/TCS-CODEVITA/) del problema en el repositorio para leer la pista de complejidad y el algoritmo requerido. Vuelve a intentar codearlo tú mismo. Solo si tras otros 15 minutos sigues bloqueado, analiza la solución y transcríbela entendiendo cada línea.
2. **Cero Copiar y Pegar:**  
   Todo código debe ser tipeado a mano en C++ para generar memoria muscular de sintaxis.
3. **Validación Inmediata con el Juez:**  
   Cada ejercicio resuelto debe pasar por [codevita_judge.py](file:///c:/Users/Aleks/Carrera/TCS/Repos/codevita_judge.py) para validar que no haya advertencias de compilación en `-std=c++17` y que el tiempo de ejecución esté por debajo de 200 ms.
4. **Métricas de Éxito:**  
   * Días 1-20: 3 a 4 problemas/día (fundamentos).
   * Días 21-45: 4 a 6 problemas/día (ritmo de crucero).
   * Días 46-60: 5 a 7 problemas/día (patrones ya interiorizados).
