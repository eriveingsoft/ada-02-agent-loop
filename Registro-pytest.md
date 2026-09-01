# Reporte de Pruebas: Resultados de Pytest Antes y Después

A continuación se detalla el registro empírico de las ejecuciones de la suite de pruebas unitarias (`pytest`) a lo largo de las distintas etapas de la práctica.

---

## 1. Línea Base (Paso 8: Antes de Iniciar el Agente)

Ejecución manual inicial en terminal PowerShell previa al uso del agente para confirmar el estado fallido del repositorio:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\erive\Documents\ada-02-agent-loop
collected 4 items

test_calculator.py ...F                                                  [100%]

================================== FAILURES ===================================
_________________________________ test_divide _________________________________

    def test_divide():
>       assert divide(10, 2) == 5
E       assert 20 == 5
E        +  where 20 = divide(10, 2)

test_calculator.py:17: AssertionError
=========================== short test summary info ===========================
FAILED test_calculator.py::test_divide - assert 20 == 5
========================= 1 failed, 3 passed in 0.19s =========================
```

## 2. Inspección y Validación Previa al Cambio (Agent Loop: Bug Fix)
```text

FAILED test_calculator.py::test_divide - assert 20 == 5
========================= 1 failed, 3 passed in 0.09s =========================
```
## 3. Verificación Posterior a la Corrección (Agent Loop: Bug Fix)
```text
============================== 4 passed in 0.03s ==============================
```

## 4. Verificación de Nueva Característica (Agent Loop: Feature Modulo)
  ```text
============================= test session starts =============================
platform win32 -- Python 3.14.3, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\erive\Documents\ada-02-agent-loop
collected 5 items

test_calculator.py .....                                                 [100%]

============================== 5 passed in 0.03s ==============================
```