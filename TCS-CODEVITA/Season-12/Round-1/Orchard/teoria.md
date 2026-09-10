# Guía Teórica y Análisis: Orchard

**Edición / Categoría:** `Season-12`  
**Nombre del Ejercicio:** `Orchard`  
**Tópico Principal (DSA):** `Teoría de Grafos, Árboles y Algoritmos de Búsqueda`  

---

## 1. Concepto y Enfoque del Problema
El ejercicio **Orchard** evalúa la habilidad del competidor para modelar una situación mediante **teoría de grafos, árboles y algoritmos de búsqueda**.
En el contexto de TCS CodeVita, este tipo de problemas requiere traducir una descripción narrativa en un modelo algorítmico formal, asegurando la selección de la estructura de datos más eficiente para no sobrepasar los límites de tiempo de ejecución (habitualmente 1.0 a 2.0 segundos).

---

## 2. Conocimientos y Prerrequisitos Teóricos
Para abordar este ejercicio de manera efectiva, el aspirante debe dominar los siguientes conceptos fundamentales:

- **Representación de grafos (Lista de adyacencia vs. Matriz de adyacencia).**
- **Algoritmos de recorrido**
- **Algoritmo de Dijkstra con cola de prioridad (`heapq` / `priority_queue`) para aristas con pesos positivos.**
- **Estructura Disjoint Set Union (DSU / Union-Find) para verificar conectividad y ciclos.**

---

## 3. Complejidad Algorítmica Esperada
- **Complejidad Temporal:** `O(V + E) para BFS/DFS clásico; O(E log V) si se utiliza Dijkstra.` — Diseñada para procesar el límite máximo de casos de prueba dentro de la ventana de ejecución.
- **Complejidad Espacial:** `O(V + E) para la estructura del grafo y el vector de visitados.` — Respetando los límites de memoria estándar de la plataforma (256 MB a 512 MB).

---

## 4. Casos Borde y Consideraciones de CodeVita
En la plataforma de evaluación de TCS CodeVita, los casos de prueba ocultos suelen atacar los siguientes escenarios críticos:

- ⚠️ Grafos no conexos: iterar sobre todos los nodos para no omitir componentes aisladas.
- ⚠️ Límite de recursión en Python (`sys.setrecursionlimit`) en árboles profundos cuando se usa DFS recursivo.
- ⚠️ Nodos indexados en 1 vs. 0: ajustar desfases de índices según los ejemplos del problema.

---

## 5. Recursos Asociados en esta Carpeta
- **Tipo de Enunciado:** 📝 **Enunciado Reconstruido y Modelado según Estándar CodeVita**
- **Archivos de Enunciado / Material:** `enunciado.md`
- **Soluciones disponibles:** `Orchard.java, solution.py`
