from .core import run_code


class Runtime:
    def __init__(self):
        self.scope = {}

    def run(self, source: str) -> str:
        return run_code(source, self.scope)
