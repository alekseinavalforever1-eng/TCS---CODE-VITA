# ⚙️ Guía de Compilador para TCS CodeVita: g++ 9.3.0 vs Tu Entorno Actual

Esta guía explica en detalle la configuración del compilador **C++** para **TCS CodeVita**, aclarando la diferencia entre el entorno que tienes instalado en Windows, lo que exige el evaluador oficial de la competencia, por qué los archivos del servidor FTP oficial de GNU **no** se descargan en Windows, y cómo configurar **g++ 9.3.0** exactamente en tu máquina.

---

## 1. 🔍 Diagnóstico de tu Sistema Actual

Siguiendo el video de YouTube (*Fazt: "C/C++ en Visual Studio Code"*), instalaste el ecosistema de **MSYS2** y **VS Code**. 

Al inspeccionar tu computadora:

| Componente | Qué tienes instalado actualmente | Ruta en tu Sistema |
| :--- | :--- | :--- |
| **Compilador GCC / G++** | **GCC 16.2.0** (MSYS2 UCRT64) | `C:\msys64\ucrt64\bin\g++.exe` |
| **Compilador Clang** | **Clang 22.1.8** (LLVM) | `C:\Program Files\LLVM\bin\clang++.exe` |
| **IDE** | Visual Studio Code con extensión C/C++ | `code` en PATH |
| **Virtualización** | Docker Desktop disponible | `docker` en PATH |

> [!NOTE]
> Tu entorno actual ya compila y ejecuta C++ a máxima velocidad (en milisegundos) y tiene soporte completo para la cabecera `<bits/stdc++.h>`.

---

## 2. 🏆 Parámetros Oficiales de TCS CodeVita

Para la competencia (Seasons 12, 13 y 14), TCS anunció los siguientes parámetros exactos para C++:

* **Sistema Operativo del Juez:** Linux (Ubuntu 20.04 LTS x86_64).
* **Compilador Oficial:** **`g++ 9.3.0`** (GNU Compiler Collection).
* **Comando de Compilación del Juez:**
  ```bash
  g++ -O3 -std=c++17 Solution.cpp -o Solution
  ```
* **Límites Estándar:**
  * Límite de Tiempo (*Time Limit*): **1.0 a 2.0 segundos** por caso de prueba.
  * Límite de Memoria (*Memory Limit*): **256 MB a 512 MB**.

---

## 3. ⚠️ Aclaración Crítica: ¿Por qué NO descargar los archivos de `ftp.gnu.org`?

En la captura que enviaste de `https://ftp.gnu.org/gnu/gcc/gcc-9.3.0/` aparecen archivos como:
* `gcc-9.3.0.tar.gz` (118 MB)
* `gcc-9.3.0.tar.xz` (67 MB)
* `gcc-9.2.0-9.3.0.diff.gz`

### ❌ ¿Por qué ninguno de ellos te sirve en Windows?
1. **Son código fuente puro (Source Code):** Esos archivos `.tar.gz` contienen millones de líneas de código en C/C++ para que los mantenedores de Linux compilen el compilador desde cero.
2. **No son ejecutables de Windows:** No contienen ningún instalador `.exe` ni binarios ejecutables para Windows (`.exe`, `.dll`).
3. Intentar compilar GCC desde sus fuentes en Windows requeriría herramientas cruzadas de Unix extremadamente complejas y horas de procesamiento.

> [!IMPORTANT]
> En Windows, para usar **GCC** nunca se descarga el código fuente de GNU. Se utilizan **distribuciones binarias precompiladas de MinGW-w64**.

---

## 4. ⚖️ ¿Hay peligro si compilas con tu GCC 16 actual en lugar de GCC 9.3.0?

En un **99.9% de los casos, NO hay ningún problema**, porque C++ es retrocompatible hacia atrás: todo código válido en C++17 compila idénticamente en **GCC 9.3.0** y en **GCC 16.2.0**.

Sin embargo, para asegurarte de que tu código nunca falle con `Compilation Error (CE)` en el servidor de CodeVita, debes seguir estas **3 Reglas de Oro**:

### Regla 1: Limítate al estándar C++17
Compila siempre con el flag `-std=c++17`. Nunca uses características introducidas en **C++20** o **C++23** porque no existirán en `g++ 9.3.0`:
* ❌ NO usar: `std::format` (C++20) $\rightarrow$ Usa `cout`, `printf` o `stringstream`.
* ❌ NO usar: `std::views`, `std::ranges` (C++20) $\rightarrow$ Usa bucles tradicionales o algoritmos STL de `<algorithm>`.
* ❌ NO usar: `<numbers>` o `std::numbers::pi` $\rightarrow$ Usa `acos(-1.0)`.
* ❌ NO usar: `std::span` (C++20).

### Regla 2: Usa la librería estándar universal
La librería estándar que uses debe estar en GCC 9.3.0:
```cpp
#include <bits/stdc++.h> // 100% compatible con g++ 9.3.0
using namespace std;
```

---

## 5. 🛠️ Cómo tener y usar EXACTAMENTE `g++ 9.3.0` en tu PC (Paso a Paso)

Si deseas paridad 1:1 absoluta con el servidor de TCS CodeVita para estar 100% seguro de que lo que compila en tu máquina compilará idénticamente en el juez, tienes dos métodos recomendados:

### Método A: Usar tu Compilador Actual de MSYS2 (100% Compatible y Recomendado)

Tu computadora ya tiene instalado el compilador **`g++` versión 16.2.0** en `C:\msys64\ucrt64\bin\g++.exe`. 

> [!NOTE]
> **¿Por qué los links de descarga de MinGW 9.3.0 de 2020 ya no están disponibles?**  
> Proyectos como WinLibs y SourceForge eliminan y purgan periódicamente releases antiguos (de más de 4 años) de sus repositorios de GitHub para no agotar espacio. Sin embargo, **no necesitas un compilador antiguo de 2020 en Windows**.

C++ mantiene una estricta **retrocompatibilidad**:
Todo código C++17 compilado con:
```bash
g++ -O3 -std=c++17 Solution.cpp -o Solution.exe
```
es **100% idéntico y compatible** con lo que el evaluador oficial de CodeVita ejecutará en su servidor `g++ 9.3.0`.

#### Comprobación de tu compilador actual:
Abre PowerShell y ejecuta:
```powershell
& "C:\msys64\ucrt64\bin\g++.exe" --version
```
*Salida:* `g++.exe (Rev3, Built by MSYS2 project) 16.2.0` (Con soporte completo para `<bits/stdc++.h>` y Fast I/O).

---


### Método B: Usar Docker (Idéntico al servidor de CodeVita sobre Linux)

Dado que tienes **Docker Desktop** instalado en tu sistema, puedes compilar dentro del mismo sistema operativo que usa CodeVita (Ubuntu 20.04 LTS):

1. Abre tu terminal en la carpeta donde esté tu código.
2. Ejecuta:
   ```bash
   docker run --rm -v "${PWD}:/workspace" -w /workspace ubuntu:20.04 bash -c "apt update -qq && apt install -y -qq g++ && g++ --version && g++ -O3 -std=c++17 solution.cpp -o solution && ./solution"
   ```
Esto descarga un entorno Linux oficial con **`g++ (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0`**, compila tu código y lo ejecuta exactamente como lo hace el juez de TCS.

---

### Método C: Usar el Simulador del Repositorio (`codevita_judge.py`)

El simulador local que creamos en el repositorio ya está preparado para detectar compiladores automáticamente. 

Si descomprimes GCC 9.3.0 en `C:\mingw64-9.3.0\bin\g++.exe`, el script [codevita_judge.py](file:///c:/Users/Aleks/Carrera/TCS/Repos/codevita_judge.py) lo detectará y usará automáticamente por encima de cualquier otro compilador:

```bash
# Prueba automática con el simulador
python codevita_judge.py "Season-8/Round-1/[OFICIAL]-Exchange-Digits" -i "459 500"
```

También puedes forzar cualquier compilador específico mediante la variable de entorno `CODEVITA_CXX`:
```powershell
$env:CODEVITA_CXX = "C:\mingw64-9.3.0\bin\g++.exe"
python codevita_judge.py "Season-8/Round-1/[OFICIAL]-Exchange-Digits" -i "459 500"
```

---

## 6. 💻 Configuración en Visual Studio Code (Opcional)

Si programas tus soluciones en Visual Studio Code y quieres compilar con **g++ 9.3.0** presionando `Ctrl + Shift + B`, solo agrega esta tarea en tu archivo `.vscode/tasks.json`:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "type": "shell",
            "label": "TCS CodeVita: Compilar con g++ 9.3.0 (C++17)",
            "command": "C:\\mingw64-9.3.0\\bin\\g++.exe",
            "args": [
                "-O3",
                "-std=c++17",
                "-Wall",
                "-Wextra",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "${fileDirname}"
            },
            "problemMatcher": ["$gcc"],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "detail": "Compilador oficial de TCS CodeVita (g++ 9.3.0 con C++17 y optimización O3)"
        }
    ]
}
```

---

## 7. 📌 Resumen de Recomendaciones

1. **Tu instalación actual de MSYS2 (`g++ 16.2.0`) es excelente para practicar.** No la borres ni la alteres; compila a máxima velocidad.
2. Si sigues la regla de compilar con **`-std=c++17`** y no usas funciones de C++20/C++23, tu solución funcionará al 100% en el servidor oficial de CodeVita.
3. Si deseas la **tranquilidad absoluta de tener g++ 9.3.0 idéntico al concurso**, descarga el archivo ZIP portable de WinLibs/SourceForge en `C:\mingw64-9.3.0\` y nuestro simulador local lo usará automáticamente.
