import json
from core.states import TextState, EquationState, AnswerState

class LMV24KConverter:
    """
    Utility to convert LMV24K raw data into Machine4MPS compatible states.
    LMV24K provides ground-truth for intermediate reasoning steps.
    """
    
    @staticmethod
    def json_to_states(raw_json_str: str):
        """
        Parses a single problem entry from LMV24K.
        Example entry might contain: 'question', 'equations', 'ans'.
        """
        data = json.loads(raw_json_str)
        
        # S0: Input text
        s0_text = TextState(data.get("question", ""))
        
        # S7: Equation System (Ground Truth)
        # Note: In LMV24K, these are often provided as a list of strings
        s7_equations = EquationState(data.get("equations", []))
        
        # S_ans: Final Numerical Answer (Ground Truth)
        s_ans = AnswerState(float(data.get("ans", 0.0)))
        
        # Return a dictionary of GT states indexed by their type/stage
        return {
            "S0": s0_text,
            "S7": s7_equations,
            "S_ans": s_ans
        }

    @staticmethod
    def batch_convert(file_path: str):
        """Processes a full dataset file."""
        print(f"[Storage] Loading dataset from {file_path}...")
        # Simulation of batch loading
        processed_data = []
        # Logic to iterate through lines would go here
        return processed_data

if __name__ == "__main__":
    # Test sample
    sample_raw = '{"question": "Add 5 to 10", "equations": ["x = 5 + 10"], "ans": 15}'
    states = LMV24KConverter.json_to_states(sample_raw)
    print(f"Converted Question: {states['S0'].content}")
    print(f"Ground Truth Answer: {states['S_ans'].content}")