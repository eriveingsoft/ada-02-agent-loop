### 1. ¿Qué es tool calling?
Es el mecanismo que permite a un modelo de lenguaje (LLM) decidir invocar funciones o herramientas externas estructuradas (como leer archivos, ejecutar comandos o consultar APIs) con argumentos específicos, en lugar de limitarse a generar texto conversacional.

---

### 2. ¿Qué es una observation?
Es la respuesta o salida directa que el entorno devuelve al agente tras la ejecución de una herramienta (por ejemplo, el contenido de un archivo, un mensaje de error o el reporte de pruebas en consola). El agente incorpora esta información en su contexto para decidir su siguiente acción.

---

### 3. ¿Qué es el Agent Loop?
Es el ciclo iterativo y autónomo de razonamiento y acción (**Pensar $\rightarrow$ Actuar $\rightarrow$ Observar $\rightarrow$ Actualizar contexto**) mediante el cual un agente interactúa con el entorno de forma continua hasta cumplir un objetivo o alcanzar una condición de parada.

---

### 4. ¿Qué operaciones corresponden a READ, WRITE, EDIT y BASH?
* **READ:** Leer e inspeccionar el contenido de un archivo existente en el sistema sin alterarlo.
* **WRITE:** Crear un archivo nuevo desde cero o sobrescribir por completo uno existente.
* **EDIT:** Aplicar cambios quirúrgicos (reemplazos de líneas o bloques de texto) en un archivo manteniendo intacto el resto del código.
* **BASH:** Ejecutar comandos en la terminal del sistema operativo (por ejemplo: `pytest`, `git diff`, `python`).

---

### 5. ¿Dónde intervino el agente?
* **Exploración:** Inspeccionó el directorio y los archivos disponibles (`ListDir`, `Find`).
* **Lectura:** Analizó el código fuente y las aserciones de prueba (`calculator.py`, `test_calculator.py`).
* **Reproducción:** Ejecutó la suite de pruebas para confirmar empíricamente el fallo antes de intervenir (`Bash(pytest)`).
* **Modificación:** Corrigió la lógica de la función `divide` aplicando el cambio mínimo necesario (`Edit(calculator.py)`).
* **Verificación:** Ejecutó nuevamente las pruebas y revisó el `git diff` para validar que todo pasara sin efectos colaterales.

---

### 6. ¿Dónde intervino el humano?
* **Preparación del entorno:** Inicializó el repositorio Git y creó los archivos base iniciales.
* **Establecimiento de línea base:** Realizó el commit inicial y ejecutó la primera prueba manual.
* **Dirección y restricciones:** Definió el prompt con las reglas del juego (no alterar tests, hacer el cambio mínimo, validar antes y después).
* **Auditoría y control:** Supervisó el comportamiento del agente y documentó las iteraciones en `agent-run.md`.

---

### 7. ¿Qué capacidad se perdería sin ejecución de comandos?
* **Validación empírica en tiempo real:** El agente no podría ejecutar suites de prueba (`pytest`) ni linters para verificar si su solución realmente funciona en el entorno real.
* **Bucle de retroalimentación (Feedback Loop):** Perdería la capacidad de autocorrección, quedando limitado a "suponer" que el código es correcto sin confirmación del sistema operativo.