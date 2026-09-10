# Guía Teórica y Análisis: Three Palindrome

**Edición / Categoría:** `No-Season`  
**Nombre del Ejercicio:** `Three-Palindrome`  
**Tópico Principal (DSA):** `Manipulación de Cadenas (Strings) y Algoritmos de Texto`  

---

## 1. Concepto y Enfoque del Problema
El ejercicio **Three Palindrome** evalúa la habilidad del competidor para modelar una situación mediante **manipulación de cadenas (strings) y algoritmos de texto**.
En el contexto de TCS CodeVita, este tipo de problemas requiere traducir una descripción narrativa en un modelo algorítmico formal, asegurando la selección de la estructura de datos más eficiente para no sobrepasar los límites de tiempo de ejecución (habitualmente 1.0 a 2.0 segundos).

---

## 2. Conocimientos y Prerrequisitos Teóricos
Para abordar este ejercicio de manera efectiva, el aspirante debe dominar los siguientes conceptos fundamentales:

- **Técnicas de Dos Punteros para detección y validación de palíndromos.**
- **Tablas de frecuencia de caracteres (`dict`, `Counter` o arrays de 256 posiciones para ASCII).**
- **Funciones de coincidencia de patrones (KMP, Z-Algorithm o Rolling Hash para subcadenas si es necesario).**
- **Parsing y tokenización con expresiones regulares (`re`) o divisores delimitados.**

---

## 3. Complejidad Algorítmica Esperada
- **Complejidad Temporal:** `O(N) o O(N log N) si involucra ordenamiento alfabético.` — Diseñada para procesar el límite máximo de casos de prueba dentro de la ventana de ejecución.
- **Complejidad Espacial:** `O(N) para la cadena resultante o O(1) con alfabeto fijo de 26/256 caracteres.` — Respetando los límites de memoria estándar de la plataforma (256 MB a 512 MB).

---

## 4. Casos Borde y Consideraciones de CodeVita
En la plataforma de evaluación de TCS CodeVita, los casos de prueba ocultos suelen atacar los siguientes escenarios críticos:

- ⚠️ Sensibilidad a mayúsculas y minúsculas (case sensitivity) no contemplada.
- ⚠️ Concatenación repetida ineficiente de strings inmutables en Python/Java (usar `list.append` y `''.join()` o `StringBuilder`).
- ⚠️ Espacios en blanco intermedios o saltos de línea adicionales al final del buffer de entrada.

---

## 5. Recursos Asociados en esta Carpeta
- **Tipo de Enunciado:** ⭐ **Enunciado Oficial de TCS CodeVita disponible**
- **Archivos de Enunciado / Material:** `enunciado.md, enunciado_alt1.md`
- **Soluciones disponibles:** `solution.java, ThreePalindrome.cpp, ThreePalindrome.java`
