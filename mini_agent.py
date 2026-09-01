import subprocess
from pathlib import Path


def read_tool(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write_tool(path: str, content: str) -> str:
    Path(path).write_text(content, encoding="utf-8")
    return f"Wrote {len(content)} characters to {path}"


def edit_tool(path: str, old_str: str, new_str: str) -> str:
    content = Path(path).read_text(encoding="utf-8")
    if old_str not in content:
        return f"Error: '{old_str}' not found in {path}"
    new_content = content.replace(old_str, new_str, 1)
    Path(path).write_text(new_content, encoding="utf-8")
    return f"Replaced '{old_str}' with '{new_str}' in {path}"


def bash_tool(command: str) -> str:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else result.stderr


def execute_tool(action: dict) -> str:
    tool = action.get("tool")
    args = action.get("args", {})

    if tool == "READ":
        return read_tool(args["path"])
    elif tool == "WRITE":
        return write_tool(args["path"], args["content"])
    elif tool == "EDIT":
        return edit_tool(args["path"], args["old_str"], args["new_str"])
    elif tool == "BASH":
        return bash_tool(args["command"])
    elif tool == "FINISH":
        return "Task completed."
    return f"Unknown tool: {tool}"


def mini_agent_loop():
    # Plan simulado de iteraciones que seguiría el agente
    simulated_plan = [
        {"tool": "READ", "args": {"path": "calculator.py"}},
        {"tool": "BASH", "args": {"command": "pytest"}},
        {"tool": "EDIT", "args": {"path": "calculator.py", "old_str": "return a * b", "new_str": "return a / b"}},
        {"tool": "BASH", "args": {"command": "pytest"}},
        {"tool": "FINISH", "args": {}}
    ]

    context = []
    finished = False
    step = 0

    print("=== STARTING MINI-AGENT LOOP ===\n")

    while not finished and step < len(simulated_plan):
        # 1. Decidir acción (obtenida del plan simulado)
        action = simulated_plan[step]
        print(f"[Iteration {step + 1}] Executing: {action['tool']} -> {action['args']}")

        # 2. Ejecutar herramienta
        result = execute_tool(action)
        print(f"[Observation]:\n{result.strip()}\n{'-' * 40}")

        # 3. Actualizar contexto
        context.append({"action": action, "observation": result})

        # 4. Evaluar condición de parada
        if action["tool"] == "FINISH" or "4 passed" in result:
            finished = True

        step += 1

    print("=== LOOP FINISHED SUCCESSFULLY ===")


if __name__ == "__main__":
    mini_agent_loop()