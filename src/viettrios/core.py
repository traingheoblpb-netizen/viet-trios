import re


def _safe_eval(expr: str, scope: dict) -> object:
    expr = expr.strip()
    if expr.startswith('"') and expr.endswith('"'):
        return expr[1:-1]
    if expr.startswith("'") and expr.endswith("'"):
        return expr[1:-1]
    if expr in scope:
        return scope[expr]
    if re.fullmatch(r"-?\d+", expr):
        return int(expr)
    if re.fullmatch(r"-?\d+\.\d+", expr):
        return float(expr)
    safe_globals = {"__builtins__": {}}
    return eval(expr, safe_globals, scope)


def run_code(source: str, scope: dict | None = None) -> str:
    scope = {} if scope is None else scope
    output = []
    lines = [line.strip() for line in source.splitlines() if line.strip()]

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("in ra "):
            value = line[5:].strip()
            output.append(str(_safe_eval(value, scope)))
            i += 1
            continue

        if "=" in line and not line.startswith("neu ") and not line.startswith("ham "):
            name, value = [part.strip() for part in line.split("=", 1)]
            scope[name] = _safe_eval(value, scope)
            i += 1
            continue

        if line.startswith("neu "):
            cond_and_body = line[4:]
            if ":" not in cond_and_body:
                raise ValueError(f"Lenh dieu kien khong hop le: {line}")
            condition, body = [part.strip() for part in cond_and_body.split(":", 1)]
            if _safe_eval(condition, scope):
                result = run_code(body, scope)
                if result:
                    output.append(result)
            i += 1
            continue

        raise ValueError(f"Lenh khong duoc ho tro: {line}")

    return "\n".join(output)
