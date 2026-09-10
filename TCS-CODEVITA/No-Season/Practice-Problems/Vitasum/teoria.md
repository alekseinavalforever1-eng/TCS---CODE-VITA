# Guía Teórica y Análisis: Vitasum

**Edición / Categoría:** `No-Season`  
**Nombre del Ejercicio:** `Vitasum`  
**Tópico Principal (DSA):** `Matemáticas Discretas, Aritmética Modular y Teoría de Números`  

---

## 1. Concepto y Enfoque del Problema
El ejercicio **Vitasum** evalúa la habilidad del competidor para modelar una situación mediante **matemáticas discretas, aritmética modular y teoría de números**.
En el contexto de TCS CodeVita, este tipo de problemas requiere traducir una descripción narrativa en un modelo algorítmico formal, asegurando la selección de la estructura de datos más eficiente para no sobrepasar los límites de tiempo de ejecución (habitualmente 1.0 a 2.0 segundos).

---

## 2. Conocimientos y Prerrequisitos Teóricos
Para abordar este ejercicio de manera efectiva, el aspirante debe dominar los siguientes conceptos fundamentales:

- **Criba de Eratóstenes para generación rápida de primos hasta 10^7.**
- **Algoritmo de Euclides para Máximo Común Divisor (GCD) y Mínimo Común Múltiplo (LCM).**
- **Combinatoria**
- **Aritmética modular e Inverso Modular (Pequeño Teorema de Fermat).**

---

## 3. Complejidad Algorítmica Esperada
- **Complejidad Temporal:** `O(sqrt(N)) para verificación de primos o divisores; O(N log log N) para cribas.` — Diseñada para procesar el límite máximo de casos de prueba dentro de la ventana de ejecución.
- **Complejidad Espacial:** `O(1) auxiliar o O(N) para tablas de primos prefijadas.` — Respetando los límites de memoria estándar de la plataforma (256 MB a 512 MB).

---

## 4. Casos Borde y Consideraciones de CodeVita
En la plataforma de evaluación de TCS CodeVita, los casos de prueba ocultos suelen atacar los siguientes escenarios críticos:

- ⚠️ Límite de tiempo (TLE) al usar divisiones ingenuas hasta N en lugar de detenerse en $\sqrt{N}$.
- ⚠️ Desbordamiento de enteros de 32 bits en C++/Java: usar `long long` en C++ y `long` o `BigInteger` en Java.
- ⚠️ Consideración del 0 y el 1 (que no son primos ni compuestos).

---

## 5. Recursos Asociados en esta Carpeta
- **Tipo de Enunciado:** 📝 **Enunciado Reconstruido y Modelado según Estándar CodeVita**
- **Archivos de Enunciado / Material:** `enunciado.md`
- **Soluciones disponibles:** `solution.py`
