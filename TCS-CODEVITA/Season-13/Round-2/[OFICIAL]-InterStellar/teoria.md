# Guía Teórica y Análisis: InterStellar

**Edición / Categoría:** `Season-13`  
**Nombre del Ejercicio:** `InterStellar`  
**Tópico Principal (DSA):** `Simulación Ad-hoc, Juegos y Modelado de Estados`  

---

## 1. Concepto y Enfoque del Problema
El ejercicio **InterStellar** evalúa la habilidad del competidor para modelar una situación mediante **simulación ad-hoc, juegos y modelado de estados**.
En el contexto de TCS CodeVita, este tipo de problemas requiere traducir una descripción narrativa en un modelo algorítmico formal, asegurando la selección de la estructura de datos más eficiente para no sobrepasar los límites de tiempo de ejecución (habitualmente 1.0 a 2.0 segundos).

---

## 2. Conocimientos y Prerrequisitos Teóricos
Para abordar este ejercicio de manera efectiva, el aspirante debe dominar los siguientes conceptos fundamentales:

- **Modelado de máquinas de estado finito o tableros matriciales.**
- **Simulación paso a paso de reglas de negocio, turnos de jugadores o señales lógicas.**
- **Representación por máscaras de bits (Bitmasks) para estados compactos (ej. visualizadores de 7 segmentos).**
- **Teoría de juegos elemental**

---

## 3. Complejidad Algorítmica Esperada
- **Complejidad Temporal:** `O(K) donde K es el número de turnos o pasos del autómata, o O(R * C) para tableros.` — Diseñada para procesar el límite máximo de casos de prueba dentro de la ventana de ejecución.
- **Complejidad Espacial:** `O(1) si es simulación en línea o O(R * C) para el estado del tablero.` — Respetando los límites de memoria estándar de la plataforma (256 MB a 512 MB).

---

## 4. Casos Borde y Consideraciones de CodeVita
En la plataforma de evaluación de TCS CodeVita, los casos de prueba ocultos suelen atacar los siguientes escenarios críticos:

- ⚠️ Ciclos infinitos si el juego o la simulación entra en un estado recurrente no detectado.
- ⚠️ Reglas especiales o excepciones no contempladas en las especificaciones del problema.
- ⚠️ Manejo de coordenadas relativas o transformaciones cíclicas (módulo).

---

## 5. Recursos Asociados en esta Carpeta
- **Tipo de Enunciado:** ⭐ **Enunciado Oficial de TCS CodeVita disponible**
- **Archivos de Enunciado / Material:** `enunciado.md`
- **Soluciones disponibles:** `solution.py, solution_abhigandesri13.py`
