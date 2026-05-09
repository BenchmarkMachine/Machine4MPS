from .states import TextState, LogicState, EquationState, AnswerState

class Transform:
    """Base class for state transitions (Si -> Sj)."""
    def __call__(self, input_state: State) -> State:
        raise NotImplementedError

class BERTEncoder(Transform):
    """Encoder module: Text -> Logic."""
    def __call__(self, state: TextState) -> LogicState:
        print(f"[Transform] Using BERT to encode: {state.content[:30]}...")
        # Simulated logic extraction
        return LogicState(nodes=["apples_initial", "apples_bought"], relations=["add"])

class DTDecoder(Transform):
    """Tree-based decoder: Logic -> Equation."""
    def __call__(self, state: LogicState) -> EquationState:
        print("[Transform] Using Deep-Tree to generate equations...")
        return EquationState(["x = 10 + 5"])

class SymbolicSolver(Transform):
    """Numerical solver: Equation -> Answer."""
    def __call__(self, state: EquationState) -> AnswerState:
        print("[Transform] Solving equations symbolically...")
        # Simple parser simulation
        return AnswerState(15.0)