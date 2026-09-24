# 🏆 TCS CodeVita — Repositorio Maestro y Ecosistema de Preparación

El repositorio más completo, estructurado y documentado para la preparación integral en **TCS CodeVita**, la competencia global de programación competitiva más grande del mundo certificada por el **Guinness World Records**.

---

## 🧭 Guías Maestras de Entrenamiento

Para comenzar a estudiar y resolver problemas, utiliza las guías centrales ubicadas en el repositorio:

- 🚀 **[Ruta Oficial de Preparación](TCS-CODEVITA/RUTA_OFICIAL_PREPARACION.md)**  
  *Guía paso a paso por niveles (Nivel 1 a 6), plantillas indispensables de Fast I/O, sintaxis clave y trucos de optimización para **C++**, **Python** y **Java**.*

- ⚙️ **[Guía de Compilador: g++ 9.3.0 vs Entorno Local](TCS-CODEVITA/GUIA_COMPILADOR_GCC_9_3_0.md)**  
  *Análisis técnico de la versión oficial del juez de CodeVita (g++ 9.3.0 en Linux), qué tienes en Windows (GCC 16), por qué no descargar fuentes de ftp.gnu.org y cómo configurar g++ 9.3.0 portable.*

- ✅ **[Checklist Maestro de Ejercicios](TCS-CODEVITA/CHECKLIST_ORDEN_EJERCICIOS.md)**  
  *Checklist interactivo con casillas `[ ]` $\rightarrow$ `[x]` que organiza los ejercicios en orden secuencial óptimo desde **MockVita** hasta la **Grand Finale**.*

- 📖 **[Guía Maestra y Catálogo de 450+ Problemas](TCS-CODEVITA/GUIA_PREPARACION_CODEVITA.md)**  
  *Catálogo completo de problemas clasificados por áreas de DSA (Arrays, Programación Dinámica, Grafos, Geometría, Cadenas, Voraces, Matemáticas y Simulación).*

- 🏆 **[Compendio de la Grand Finale](TCS-CODEVITA/GRAND_FINALE_PROBLEMS.md)**  
  *Análisis exclusivo sobre la **Fase 3 (Final Mundial)**, por qué estos ejercicios no suelen encontrarse en internet y 4 problemas representativos de nivel mundial con soluciones completas.*

- 📑 **[Correlación de 60 Problemas Clásicos](TCS-CODEVITA/CORRELACION_60_PROBLEMAS.md)** / **[60.md](60.md)**  
  *Mapeo y resolución de los 60 problemas clásicos del portal preparatorio indio preparefocus.com.*

---

## 📂 Estructura del Repositorio

El contenido está clasificado por temporadas históricas (**Seasons**) y subdividido internamente por fases oficiales (**Round 1**, **Round 2** y **MockVita**):

```text
TCS---CODE-VITA/
├── README.md                           <-- Portada principal y enlaces rápidos
├── 60.md                               <-- Mapeo de los 60 problemas clásicos
├── TCS-CODEVITA/
│   ├── RUTA_OFICIAL_PREPARACION.md     <-- Ruta de estudio por niveles y sintaxis
│   ├── CHECKLIST_ORDEN_EJERCICIOS.md   <-- Checklist de avance paso a paso
│   ├── GUIA_PREPARACION_CODEVITA.md    <-- Catálogo completo de 450+ ejercicios
│   ├── GRAND_FINALE_PROBLEMS.md        <-- Problemas y análisis de la final mundial
│   ├── CORRELACION_60_PROBLEMAS.md     <-- Mapeo detallado de los 60 problemas
│   │
│   ├── Season-13/                      <-- Edición 2024-2025
│   │   ├── Round-1/                    <-- Pre-Qualifier (45 problemas)
│   │   └── Round-2/                    <-- Qualifier (13 problemas)
│   ├── Season-12/                      <-- Edición 2023-2024
│   │   ├── Round-1/                    <-- Pre-Qualifier (49 problemas)
│   │   └── Round-2/                    <-- Qualifier (13 problemas)
│   ├── Season-11/                      <-- Edición 2023
│   │   └── Round-1/                    <-- Pre-Qualifier y Mock (12 problemas)
│   ├── Season-10/                      <-- Edición 2022
│   │   └── Round-1/                    <-- Pre-Qualifier (7 problemas)
│   ├── Season-9/                       <-- Edición 2020
│   │   ├── Round-1/                    <-- Pre-Qualifier (31 problemas)
│   │   └── MockVita-2/                 <-- Ronda simulada oficial (2 problemas)
│   ├── Season-8/                       <-- Edición 2019
│   │   ├── Round-1/                    <-- Pre-Qualifier Zonal (34 problemas)
│   │   └── MockVita-2/                 <-- Ronda simulada oficial (6 problemas)
│   ├── Season-7/                       <-- Edición 2018
│   │   └── Round-1/                    <-- Pre-Qualifier (10 problemas)
│   ├── Season-6/                       <-- Edición 2017
│   │   ├── Round-1/                    <-- Pre-Qualifier (8 problemas)
│   │   └── Round-2/                    <-- Qualifier (8 problemas)
│   └── No-Season/
│       ├── Practice-Problems/          <-- 191 problemas del banco general de práctica
│       ├── TCS-Digital/                <-- 23 problemas para entrevistas avanzadas Digital
│       ├── TCS-NQT/                    <-- 5 problemas de National Qualifier Test
│       └── Reference-Material/         <-- Manuales de estudio e índices de referencia
```

---

## 🏷️ Estructura de Cada Carpeta de Ejercicio

Cada uno de los ejercicios del repositorio está equipado con:
1. **Solución funcional en código**: Implementaciones comentadas y optimizadas en **Python**, **C++** o **Java**.
2. **`enunciado.md` o PDFs/Imágenes Oficiales**: Descripción detallada, restricciones numéricas de $N$, formato estricto de entrada y salida, y casos de ejemplo explicados.
   - *Los ejercicios marcados con el prefijo `[OFICIAL]-` contienen los enunciados, PDFs o capturas originales de la plataforma.*
3. **`teoria.md`**: Ficha técnica con el tópico principal de DSA, conceptos teóricos requeridos, complejidad temporal y espacial esperada, y casos borde críticos.

---

## 📊 Métricas del Repositorio

- **Total de problemas organizados:** 465+ ejercicios
- **Cobertura de Fichas Teóricas (`teoria.md`):** 100%
- **Cobertura de Enunciados (`enunciado.md` / PDFs / Capturas):** 100%
- **Cobertura de Soluciones de Código:** 99.4%
- **Temporadas cubiertas:** Season 6 hasta Season 13 + TCS Digital + TCS NQT

---

## ⚖️ Simulador y Juez de Pruebas Local (`codevita_judge.py`)

El repositorio incluye un **juez local offline** en Python puro que emula con precisión el evaluador oficial de TCS CodeVita, permitiéndote probar soluciones en **Python**, **C++** y **Java**:

- 🧪 **Detección automática de casos de prueba**: Lee los ejemplos de entrada/salida directamente desde el `enunciado.md`.
- ⚡ **Compilación y ejecución real**: Soporta `clang++`/`g++` con compatibilidad para `<bits/stdc++.h>`, `javac`/`java`, y `python`.
- ⏱️ **Medición de tiempo y TLE**: Reporta el tiempo de ejecución en milisegundos y alerta si excede el límite de tiempo oficial (> 2.0s).
- 🔍 **Comparador exacto de salidas**: Detecta `[ACCEPTED]` o muestra la discrepancia detallada (`[WRONG ANSWER]`).

### Comandos de Ejemplo:

```bash
# 1. Evaluar un problema contra sus casos de prueba de ejemplo
python codevita_judge.py "Season-9/Round-1/[OFICIAL]-Railwaystation"

# 2. Evaluar ingresando una entrada manual por consola
python codevita_judge.py "Season-8/Round-1/[OFICIAL]-Exchange-Digits" -i "459 500"

# 3. Probar en modo interactivo paso a paso
python codevita_judge.py "No-Season/Practice-Problems/[OFICIAL]-Collecting-Candies" --interactive

# 4. Forzar evaluación con un lenguaje específico (ej: java o cpp)
python codevita_judge.py "Collecting-Candies" -l java -i "4 1 2 3 4"
```

---

## 🚀 Cómo Empezar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/alekseinavalforever1-eng/TCS---CODE-VITA.git
   cd TCS---CODE-VITA
   ```
2. Lee la **[Ruta Oficial de Preparación](TCS-CODEVITA/RUTA_OFICIAL_PREPARACION.md)** para configurar tus plantillas de Fast I/O en C++, Python o Java.
3. Abre el **[Checklist Maestro de Ejercicios](TCS-CODEVITA/CHECKLIST_ORDEN_EJERCICIOS.md)** y comienza a resolver los ejercicios desde **MockVita** hacia adelante.
4. Usa el simulador `python codevita_judge.py [problema]` para validar tus soluciones localmente antes de competir.
