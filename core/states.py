from dataclasses import dataclass
from typing import Any, List

@dataclass
class State:
    """Base class for all solver states."""
    content: Any
    state_type: str

class TextState(State):
    """S0: Initial problem description in natural language."""
    def __init__(self, content: str):
        super().__init__(content, "Text")

class LogicState(State):
    """S1-S6: Intermediate logic representation (e.g., Knowledge Graph)."""
    def __init__(self, nodes: List, relations: List):
        super().__init__({"nodes": nodes, "relations": relations}, "Logic")

class EquationState(State):
    """S7: Mathematical equation system."""
    def __init__(self, equations: List[str]):
        super().__init__(equations, "Equation")

class AnswerState(State):
    """S_ans: Final numerical result."""
    def __init__(self, value: float):
        super().__init__(value, "Answer")