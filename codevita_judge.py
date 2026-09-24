#!/usr/bin/env python3
"""
=============================================================================
  🏆 TCS CodeVita Local Judge & Test Simulator
  Simulador de Evaluación Local para Ejercicios de TCS CodeVita
=============================================================================
"""

import os
import re
import sys
import time
import shutil
import tempfile
import argparse
import subprocess
from pathlib import Path

# Ensure UTF-8 output on Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ANSI Colors for Windows / Unix terminals
class Colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"

# Enable VT100 colors in Windows cmd/PowerShell
if sys.platform == "win32":
    os.system("")

BASE_DIR = Path(__file__).resolve().parent
TCS_ROOT = BASE_DIR / "TCS-CODEVITA"

def find_problem_folder(query):
    """Finds problem folder by relative path, full path, or fuzzy problem name."""
    p_direct = Path(query)
    if p_direct.is_dir():
        return p_direct
        
    p_in_tcs = TCS_ROOT / query
    if p_in_tcs.is_dir():
        return p_in_tcs
        
    # Search fuzzy by problem name
    q_clean = "".join(c for c in query.lower() if c.isalnum())
    matches = []
    
    for root, dirs, files in os.walk(TCS_ROOT):
        r_path = Path(root)
        if any(f.suffix.lower() in ['.py', '.cpp', '.java', '.c'] for f in r_path.iterdir()):
            folder_clean = "".join(c for c in r_path.name.lower() if c.isalnum())
            if q_clean == folder_clean:
                return r_path
            elif q_clean in folder_clean or folder_clean in q_clean:
                matches.append(r_path)
                
    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        # Prefer official folder if ambiguous
        for m in matches:
            if "[OFICIAL]-" in m.name:
                return m
        return matches[0]
        
    return None

def parse_test_cases_from_text(text):
    """Parses sample input and output blocks from problem statement."""
    test_cases = []
    clean_txt = text.replace('\r\n', '\n')
    
    # Format 1: Sample input ... Sample output
    p_sample = re.finditer(
        r'Sample\s*input\s*\d*\s*:?\s*(?:-+\s*)?\n([\s\S]*?)\n+Sample\s*output\s*\d*\s*:?\s*(?:-+\s*)?\n([\s\S]*?)(?=\n+(?:Sample\s*input|---|##|$))',
        clean_txt, re.IGNORECASE
    )
    for m in p_sample:
        inp = m.group(1).strip()
        out = m.group(2).strip()
        if inp and out and not out.startswith("["):
            test_cases.append({"input": inp, "expected": out, "name": f"Sample {len(test_cases)+1}"})

    # Format 2: Example X ... Input ... Output
    if not test_cases:
        p_ex = re.finditer(
            r'(?:###?\s*)?Example\s*(\d+)?\s*\n+.*?(?:Input|Input:)\s*\n+(?:```[a-zA-Z]*\s*)?([\s\S]*?)(?:```)?\n+(?:Output|Output:)\s*\n+(?:```[a-zA-Z]*\s*)?([\s\S]*?)(?:```)?(?=\n+(?:Explanation|Example|Constraints|---|$))',
            clean_txt, re.IGNORECASE
        )
        for m in p_ex:
            num = m.group(1) or str(len(test_cases) + 1)
            raw_inp = m.group(2).strip()
            raw_out = m.group(3).strip()
            
            clean_inp_lines = [l.strip() for l in raw_inp.splitlines() if l.strip()]
            clean_out_lines = [l for l in raw_out.splitlines()]
            
            inp = "\n".join(clean_inp_lines)
            out = "\n".join(clean_out_lines).strip()
            
            if inp and out and not out.startswith("[Resultado") and not out.startswith("[Computed"):
                test_cases.append({"input": inp, "expected": out, "name": f"Example {num}"})

    # Format 3: Explicit test text files
    return test_cases

def get_problem_test_cases(folder_path):
    """Retrieves all test cases available in the problem directory."""
    test_cases = []
    
    # 1. Check for external test files like test_*.txt, input*.txt
    inp_files = sorted(list(folder_path.glob("input*.txt")) + list(folder_path.glob("test*.txt")))
    for inf in inp_files:
        # Check corresponding output file
        outf = folder_path / inf.name.replace("input", "output").replace("test", "expected")
        if outf.exists():
            test_cases.append({
                "input": inf.read_text(encoding='utf-8', errors='ignore').strip(),
                "expected": outf.read_text(encoding='utf-8', errors='ignore').strip(),
                "name": inf.stem
            })
            
    # 2. Extract from statement files
    if not test_cases:
        statement_files = [
            f for f in folder_path.iterdir()
            if f.suffix.lower() in ['.md', '.txt'] and f.name != 'teoria.md'
        ]
        for sf in statement_files:
            try:
                txt = sf.read_text(encoding='utf-8', errors='ignore')
                tcs = parse_test_cases_from_text(txt)
                if tcs:
                    test_cases.extend(tcs)
                    break
            except Exception:
                pass
                
    return test_cases

def normalize_output(out_str):
    """Normalizes output by removing trailing carriage returns, whitespace and empty lines."""
    lines = [l.rstrip() for l in out_str.replace('\r\n', '\n').splitlines()]
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines)

def run_solution(code_file, input_text, timeout=2.0):
    """Compiles (if necessary) and executes the code against input_text."""
    ext = code_file.suffix.lower()
    start_time = 0
    duration = 0
    
    # Python
    if ext == '.py':
        cmd = [sys.executable, str(code_file)]
        start_time = time.perf_counter()
        try:
            res = subprocess.run(
                cmd, input=input_text, capture_output=True, text=True,
                timeout=timeout, cwd=str(code_file.parent)
            )
            duration = (time.perf_counter() - start_time) * 1000
            return {
                "verdict": "OK" if res.returncode == 0 else "RTE",
                "stdout": res.stdout,
                "stderr": res.stderr,
                "time_ms": duration,
                "returncode": res.returncode
            }
        except subprocess.TimeoutExpired:
            return {"verdict": "TLE", "stdout": "", "stderr": f"Time Limit Exceeded (> {timeout}s)", "time_ms": timeout * 1000, "returncode": -1}
        except Exception as e:
            return {"verdict": "RTE", "stdout": "", "stderr": str(e), "time_ms": 0, "returncode": -1}

    # C++
    elif ext in ['.cpp', '.c']:
        # Look for g++ first (TCS CodeVita standard), custom paths, then clang++
        cxx_candidates = [
            os.environ.get("CODEVITA_CXX"),
            shutil.which("g++"),
            r"C:\msys64\ucrt64\bin\g++.exe",
            r"C:\msys64\mingw64\bin\g++.exe",
            r"C:\mingw64-9.3.0\bin\g++.exe",
            r"C:\mingw64\bin\g++.exe",
            shutil.which("clang++"),
        ]
        compiler = next((c for c in cxx_candidates if c and (shutil.which(c) or Path(c).is_file())), None)
        if not compiler:
            return {"verdict": "CE", "stdout": "", "stderr": "No C++ compiler found (g++ or clang++ needed in PATH)", "time_ms": 0, "returncode": -1}
            
        with tempfile.TemporaryDirectory() as temp_dir:
            # Provide bits/stdc++.h compatibility for clang++ on Windows
            bits_dir = Path(temp_dir) / "bits"
            bits_dir.mkdir(parents=True, exist_ok=True)
            bits_header = bits_dir / "stdc++.h"
            bits_header.write_text(
                "#ifndef _BITS_STDCPP_H\n"
                "#define _BITS_STDCPP_H\n"
                "#include <iostream>\n#include <cstdio>\n#include <cstdlib>\n#include <cstring>\n"
                "#include <cmath>\n#include <ctime>\n#include <cassert>\n#include <climits>\n#include <cfloat>\n"
                "#include <vector>\n#include <list>\n#include <deque>\n#include <queue>\n#include <stack>\n"
                "#include <set>\n#include <map>\n#include <unordered_set>\n#include <unordered_map>\n#include <bitset>\n"
                "#include <string>\n#include <sstream>\n#include <algorithm>\n#include <numeric>\n#include <utility>\n"
                "#include <functional>\n#include <iterator>\n#include <memory>\n#include <tuple>\n#include <regex>\n"
                "#include <iomanip>\n#endif\n",
                encoding='utf-8'
            )
            exe_path = Path(temp_dir) / "prog.exe"
            compile_cmd = [compiler, "-O3", "-std=c++17", f"-I{temp_dir}", str(code_file), "-o", str(exe_path)]
            c_res = subprocess.run(compile_cmd, capture_output=True, text=True)
            if c_res.returncode != 0:
                return {"verdict": "CE", "stdout": "", "stderr": c_res.stderr, "time_ms": 0, "returncode": c_res.returncode}
                
            start_time = time.perf_counter()
            try:
                res = subprocess.run(
                    [str(exe_path)], input=input_text, capture_output=True, text=True,
                    timeout=timeout, cwd=str(code_file.parent)
                )
                duration = (time.perf_counter() - start_time) * 1000
                return {
                    "verdict": "OK" if res.returncode == 0 else "RTE",
                    "stdout": res.stdout,
                    "stderr": res.stderr,
                    "time_ms": duration,
                    "returncode": res.returncode
                }
            except subprocess.TimeoutExpired:
                return {"verdict": "TLE", "stdout": "", "stderr": f"Time Limit Exceeded (> {timeout}s)", "time_ms": timeout * 1000, "returncode": -1}
            except Exception as e:
                return {"verdict": "RTE", "stdout": "", "stderr": str(e), "time_ms": 0, "returncode": -1}

    # Java
    elif ext == '.java':
        javac = shutil.which("javac")
        java = shutil.which("java")
        if not javac or not java:
            return {"verdict": "CE", "stdout": "", "stderr": "Java compiler/runtime not found (javac/java needed in PATH)", "time_ms": 0, "returncode": -1}
            
        with tempfile.TemporaryDirectory() as temp_dir:
            src_code = code_file.read_text(encoding='utf-8', errors='ignore')
            # Comment out package declaration for judge sandbox compatibility
            cleaned_code = re.sub(r'^\s*package\s+[\w\.]+;', '// package removed for judge', src_code, flags=re.MULTILINE)
            java_src = Path(temp_dir) / code_file.name
            java_src.write_text(cleaned_code, encoding='utf-8')
            
            c_res = subprocess.run([javac, str(java_src)], capture_output=True, text=True, cwd=temp_dir)
            if c_res.returncode != 0:
                return {"verdict": "CE", "stdout": "", "stderr": c_res.stderr, "time_ms": 0, "returncode": c_res.returncode}
                
            class_name = code_file.stem
            start_time = time.perf_counter()
            try:
                res = subprocess.run(
                    [java, "-cp", temp_dir, class_name], input=input_text, capture_output=True, text=True,
                    timeout=timeout, cwd=temp_dir
                )
                duration = (time.perf_counter() - start_time) * 1000
                return {
                    "verdict": "OK" if res.returncode == 0 else "RTE",
                    "stdout": res.stdout,
                    "stderr": res.stderr,
                    "time_ms": duration,
                    "returncode": res.returncode
                }
            except subprocess.TimeoutExpired:
                return {"verdict": "TLE", "stdout": "", "stderr": f"Time Limit Exceeded (> {timeout}s)", "time_ms": timeout * 1000, "returncode": -1}
            except Exception as e:
                return {"verdict": "RTE", "stdout": "", "stderr": str(e), "time_ms": 0, "returncode": -1}

    return {"verdict": "ERR", "stdout": "", "stderr": f"Unsupported file extension {ext}", "time_ms": 0, "returncode": -1}

def judge_problem(folder_path, custom_input=None, lang_pref=None, timeout=2.0):
    """Evaluates a problem against test cases or custom input."""
    rel_path = folder_path.relative_to(TCS_ROOT) if TCS_ROOT in folder_path.parents else folder_path
    print(f"\n{Colors.CYAN}{Colors.BOLD}======================================================================{Colors.RESET}")
    print(f"{Colors.BOLD}🔍 Evaluando Ejercicio:{Colors.RESET} {Colors.YELLOW}{rel_path}{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}======================================================================{Colors.RESET}")

    # Find solution file
    sol_files = sorted(
        [f for f in folder_path.iterdir() if f.suffix.lower() in ['.py', '.cpp', '.java', '.c']],
        key=lambda x: (x.suffix != '.py', x.name)
    )
    
    if lang_pref:
        filtered = [f for f in sol_files if f.suffix.lower() == f".{lang_pref.lower()}"]
        if filtered:
            sol_files = filtered

    if not sol_files:
        print(f"{Colors.RED}❌ No se encontró ningún archivo de código (.py, .cpp, .java) en esta carpeta.{Colors.RESET}")
        return False

    code_file = sol_files[0]
    print(f"📄 {Colors.BOLD}Archivo de Solución:{Colors.RESET} {code_file.name} ({code_file.suffix.upper()})")

    # If custom input provided
    if custom_input is not None:
        print(f"\n{Colors.BLUE}▶ Ejecutando con Entrada Personalizada...{Colors.RESET}")
        res = run_solution(code_file, custom_input, timeout=timeout)
        print(f"⏱️ Tiempo: {res['time_ms']:.2f} ms")
        if res['verdict'] == 'OK':
            print(f"\n{Colors.GREEN}{Colors.BOLD}--- Salida Obtenida (stdout) ---{Colors.RESET}")
            print(res['stdout'].rstrip())
        else:
            print(f"{Colors.RED}{Colors.BOLD}[{res['verdict']}]{Colors.RESET}: {res['stderr']}")
        return res['verdict'] == 'OK'

    # Extract test cases
    test_cases = get_problem_test_cases(folder_path)
    if not test_cases:
        print(f"{Colors.YELLOW}⚠️ No se detectaron casos de prueba automáticos en el enunciado.{Colors.RESET}")
        print("💡 Puedes ejecutar el evaluador con `--input` o `--interactive` para probar tu propia entrada:")
        print(f"   python codevita_judge.py \"{rel_path}\" --interactive\n")
        return True

    print(f"🧪 Casos de Prueba Encontrados: {len(test_cases)}")
    all_passed = True

    for i, tc in enumerate(test_cases, 1):
        name = tc.get('name', f"Caso #{i}")
        inp = tc['input']
        exp = tc['expected']
        
        print(f"\n{Colors.BOLD}--- [{i}/{len(test_cases)}] {name} ---{Colors.RESET}")
        res = run_solution(code_file, inp, timeout=timeout)
        time_str = f"({res['time_ms']:.1f} ms)"
        
        if res['verdict'] == 'CE':
            print(f"  {Colors.RED}{Colors.BOLD}⚙️ [COMPILATION ERROR]{Colors.RESET} {res['stderr']}")
            all_passed = False
            break
        elif res['verdict'] == 'TLE':
            print(f"  {Colors.YELLOW}{Colors.BOLD}⏱️ [TIME LIMIT EXCEEDED]{Colors.RESET} {time_str}")
            all_passed = False
        elif res['verdict'] == 'RTE':
            print(f"  {Colors.RED}{Colors.BOLD}💥 [RUNTIME ERROR]{Colors.RESET} {time_str}")
            if res['stderr']:
                print(f"     {Colors.RED}{res['stderr'].strip()}{Colors.RESET}")
            all_passed = False
        elif res['verdict'] == 'OK':
            got = normalize_output(res['stdout'])
            exp_clean = normalize_output(exp)
            
            if got == exp_clean:
                print(f"  {Colors.GREEN}{Colors.BOLD}✅ [ACCEPTED]{Colors.RESET} {time_str}")
            else:
                print(f"  {Colors.RED}{Colors.BOLD}❌ [WRONG ANSWER]{Colors.RESET} {time_str}")
                print(f"     {Colors.BOLD}Esperado:{Colors.RESET}\n{Colors.CYAN}{exp_clean}{Colors.RESET}")
                print(f"     {Colors.BOLD}Obtenido:{Colors.RESET}\n{Colors.YELLOW}{got}{Colors.RESET}")
                all_passed = False

    print(f"\n{Colors.CYAN}----------------------------------------------------------------------{Colors.RESET}")
    if all_passed:
        print(f"{Colors.GREEN}{Colors.BOLD}🎉 RESULTADO FINAL: TODOS LOS CASOS SUPERADOS CON ÉXITO (AC){Colors.RESET}")
    else:
        print(f"{Colors.RED}{Colors.BOLD}⚠️ RESULTADO FINAL: HUBO FALLOS EN AL MENOS UN CASO DE PRUEBA{Colors.RESET}")
    print(f"{Colors.CYAN}----------------------------------------------------------------------{Colors.RESET}\n")

    return all_passed

def main():
    parser = argparse.ArgumentParser(description="TCS CodeVita Local Judge & Test Simulator")
    parser.add_argument("problem", nargs="?", help="Nombre o ruta del problema a evaluar (ej: Railwaystation o Season-9/Round-1/[OFICIAL]-Railwaystation)")
    parser.add_argument("-i", "--input", help="Entrada de texto directa para evaluar")
    parser.add_argument("-f", "--input-file", help="Ruta a archivo con entrada personalizada")
    parser.add_argument("--interactive", action="store_true", help="Modo interactivo para ingresar datos por consola")
    parser.add_argument("-l", "--lang", choices=["py", "cpp", "java", "c"], help="Forzar lenguaje específico")
    parser.add_argument("-t", "--timeout", type=float, default=2.0, help="Límite de tiempo en segundos (default: 2.0s)")
    parser.add_argument("--season", help="Evaluar todos los problemas de una Season específica (ej: Season-9)")
    
    args = parser.parse_args()

    print(f"{Colors.CYAN}{Colors.BOLD}")
    print("  ============================================================")
    print("     🏆 TCS CodeVita Local Judge & Test Simulator v1.0")
    print("  ============================================================")
    print(f"{Colors.RESET}")

    # Season batch mode
    if args.season:
        season_dir = TCS_ROOT / args.season
        if not season_dir.exists():
            print(f"{Colors.RED}No existe la Season '{args.season}'.{Colors.RESET}")
            sys.exit(1)
        prob_dirs = []
        for root, dirs, files in os.walk(season_dir):
            r = Path(root)
            if any(f.suffix.lower() in ['.py', '.cpp', '.java'] for f in r.iterdir()):
                prob_dirs.append(r)
        print(f"🚀 Evaluando {len(prob_dirs)} problemas en {args.season}...\n")
        passed = 0
        for pd in prob_dirs:
            if judge_problem(pd, timeout=args.timeout, lang_pref=args.lang):
                passed += 1
        print(f"\n{Colors.BOLD}Resumen Season {args.season}:{Colors.RESET} {passed}/{len(prob_dirs)} superados.")
        return

    if not args.problem:
        print("💡 Uso rápido:")
        print("   python codevita_judge.py <nombre-o-carpeta>")
        print("   python codevita_judge.py Railwaystation")
        print("   python codevita_judge.py \"Season-13/Round-2/[OFICIAL]-Ascii-Homes\"")
        print("   python codevita_judge.py Primetimeagain --interactive")
        sys.exit(0)

    folder = find_problem_folder(args.problem)
    if not folder:
        print(f"{Colors.RED}❌ No se encontró ningún ejercicio que coincida con '{args.problem}'.{Colors.RESET}")
        sys.exit(1)

    custom_inp = None
    if args.input:
        custom_inp = args.input
    elif args.input_file:
        custom_inp = Path(args.input_file).read_text(encoding='utf-8', errors='ignore')
    elif args.interactive:
        print(f"{Colors.YELLOW}Escribe o pega la entrada estándar (finaliza con Ctrl+Z en Windows o Ctrl+D en Unix):{Colors.RESET}\n")
        custom_inp = sys.stdin.read()

    judge_problem(folder, custom_input=custom_inp, lang_pref=args.lang, timeout=args.timeout)

if __name__ == "__main__":
    main()
