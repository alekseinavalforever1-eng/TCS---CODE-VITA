# Guía Teórica y Análisis: CodeVita 60 Problems Index

**Edición / Categoría:** `No-Season`  
**Nombre del Ejercicio:** `CodeVita-60-Problems-Index`  
**Tópico Principal (DSA):** `Algoritmos Voraces (Greedy) y Programación de Intervalos`  

---

## 1. Concepto y Enfoque del Problema
El ejercicio **CodeVita 60 Problems Index** evalúa la habilidad del competidor para modelar una situación mediante **algoritmos voraces (greedy) y programación de intervalos**.
En el contexto de TCS CodeVita, este tipo de problemas requiere traducir una descripción narrativa en un modelo algorítmico formal, asegurando la selección de la estructura de datos más eficiente para no sobrepasar los límites de tiempo de ejecución (habitualmente 1.0 a 2.0 segundos).

---

## 2. Conocimientos y Prerrequisitos Teóricos
Para abordar este ejercicio de manera efectiva, el aspirante debe dominar los siguientes conceptos fundamentales:

- **Criterio de ordenamiento voraz (ordenar por tiempo de finalización, razón valor/peso, o tiempo de inicio).**
- **Algoritmo de barrido (Sweep-line) y simulación con eventos (llegada / salida).**
- **Colas de prioridad / Montículos (Min-Heap / Max-Heap) para rastrear recursos disponibles.**
- **Demostración de elección voraz**

---

## 3. Complejidad Algorítmica Esperada
- **Complejidad Temporal:** `O(N log N) dominado por el paso de ordenamiento.` — Diseñada para procesar el límite máximo de casos de prueba dentro de la ventana de ejecución.
- **Complejidad Espacial:** `O(N) para almacenar las estructuras de eventos e intervalos.` — Respetando los límites de memoria estándar de la plataforma (256 MB a 512 MB).

---

## 4. Casos Borde y Consideraciones de CodeVita
En la plataforma de evaluación de TCS CodeVita, los casos de prueba ocultos suelen atacar los siguientes escenarios críticos:

- ⚠️ Empates en los criterios de ordenamiento: definir correctamente el desempate secundario.
- ⚠️ Intervalos abiertos vs. cerrados: si el fin de una tarea coincide con el inicio de otra, ¿se solapan o no?
- ⚠️ Casos con listas vacías o de un solo elemento.

---

## 5. Recursos Asociados en esta Carpeta
- **Tipo de Enunciado:** ⭐ **Enunciado Oficial de TCS CodeVita disponible**
- **Archivos de Enunciado / Material:** `enunciado.md`
- **Soluciones disponibles:** `solution.py`
