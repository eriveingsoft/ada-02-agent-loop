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

### Qué información tuvo que leer el agente?

La estructura del directorio para identificar qué archivos componían el repositorio.

El código fuente de calculator.py (para analizar las funciones aritméticas).

El código de pruebas de test_calculator.py (para ver qué aserciones y casos de prueba existían).

La salida del comando de terminal pytest para verificar los resultados de las pruebas en tiempo de ejecución.

### ¿Qué herramienta utilizó para conocer el contenido del archivo?

La herramienta Read (ejecutada como Read(~/Documents/ada-02-agent-loop/calculator.py) y Read(~/Documents/ada-02-agent-loop/test_calculator.py)).

### ¿Modificó algún archivo?

No. Cumplió con la restricción explícita de la instrucción ("Do not modify any files"). Solo ejecutó herramientas de lectura e inspección (ListDir, Find, Read) y una herramienta de ejecución de terminal en modo lectura (Bash(pytest)).

### ¿Cómo podría comprobar que su hipótesis sobre el bug es correcta?

Modificando la línea en calculator.py para cambiar el operador return a * b por return a / b (o a // b).

Ejecutando nuevamente pytest mediante la herramienta Bash y verificando que los 4 tests pasen con un estado 100% exitoso (4 passed).

### ¿Qué diferencia observas entre pedir una respuesta a un LLM y permitir que un agente interactúe con un repositorio?

LLM tradicional (solo texto/chat): Depende únicamente de lo que el usuario copie y pegue manualmente en el prompt, no tiene noción del entorno real del sistema y puede alucinar supuestos sobre dependencias o estructura sin forma de comprobarlos.

Agente con acceso al repositorio (Agent Loop): Es autónomo para explorar el árbol de archivos, leer el código en tiempo real, ejecutar comandos (como suites de prueba o linters) en el entorno real para validar sus hipótesis y basar sus conclusiones en evidencia empírica directa del proyecto.