# Guía Teórica y Análisis: Shapes Geometry

**Edición / Categoría:** `No-Season`  
**Nombre del Ejercicio:** `Shapes-Geometry`  
**Tópico Principal (DSA):** `Geometría Computacional y Álgebra Vectorial`  

---

## 1. Concepto y Enfoque del Problema
El ejercicio **Shapes Geometry** evalúa la habilidad del competidor para modelar una situación mediante **geometría computacional y álgebra vectorial**.
En el contexto de TCS CodeVita, este tipo de problemas requiere traducir una descripción narrativa en un modelo algorítmico formal, asegurando la selección de la estructura de datos más eficiente para no sobrepasar los límites de tiempo de ejecución (habitualmente 1.0 a 2.0 segundos).

---

## 2. Conocimientos y Prerrequisitos Teóricos
Para abordar este ejercicio de manera efectiva, el aspirante debe dominar los siguientes conceptos fundamentales:

- **Geometría euclidiana en 2D (distancia entre puntos, producto punto y producto cruz).**
- **Fórmula de Shoelace (área de polígonos por coordenadas).**
- **Ecuación de la recta y pruebas de intersección entre segmentos.**
- **Manejo de precisión con números de punto flotante (`double`, `round`, `epsilon`).**

---

## 3. Complejidad Algorítmica Esperada
- **Complejidad Temporal:** `O(N) a O(N^2) según el número de pares de segmentos o vértices evaluados.` — Diseñada para procesar el límite máximo de casos de prueba dentro de la ventana de ejecución.
- **Complejidad Espacial:** `O(N) para almacenar las coordenadas y vértices del polígono/figura.` — Respetando los límites de memoria estándar de la plataforma (256 MB a 512 MB).

---

## 4. Casos Borde y Consideraciones de CodeVita
En la plataforma de evaluación de TCS CodeVita, los casos de prueba ocultos suelen atacar los siguientes escenarios críticos:

- ⚠️ Errores de precisión por redondeo flotante al calcular tangentes, cosenos o raíces cuadradas.
- ⚠️ Casos colineales o líneas paralelas que pueden provocar divisiones entre cero.
- ⚠️ Formato estricto de salida: verificar si la plataforma exige 2 decimales (`{:.2f}`) o truncamiento entero.

---

## 5. Recursos Asociados en esta Carpeta
- **Tipo de Enunciado:** 📝 **Enunciado Reconstruido y Modelado según Estándar CodeVita**
- **Archivos de Enunciado / Material:** `enunciado.md`
- **Soluciones disponibles:** `solution.java`
