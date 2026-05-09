from typing import List
from .states import TextState

class MPSEngine:
    """Execution engine for Machine4MPS."""
    def __init__(self, pipeline: List):
        self.pipeline = pipeline

    def solve(self, problem_text: str):
        current_state = TextState(problem_text)
        history = [current_state]
        
        for transform in self.pipeline:
            current_state = transform(current_state)
            history.append(current_state)
            
        return current_state, history