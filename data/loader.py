import json
import os
from typing import List, Dict
from core.states import TextState, EquationState, AnswerState

class LMV24KLoader:
    """
    DataLoader for the LMV24K dataset.
    Handles reading raw JSON data and converting them into State objects 
    for process-aware evaluation.
    """
    
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.raw_data = self._load_file()

    def _load_file(self) -> List[Dict]:
        if not os.path.exists(self.data_path):
            print(f"[Error] Data file not found: {self.data_path}")
            return []
        
        with open(self.data_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_problem(self, index: int) -> Dict:
        """
        Retrieves a single problem and its ground truth states.
        """
        item = self.raw_data[index]
        
        # S0: The input question
        question = TextState(item["question"])
        
        # Ground Truths for PCC (Process-aware Confusion Comparison)
        gt_states = {
            "S0": question,
            "S7": EquationState(item["equations"]),
            "S_ans": AnswerState(float(item["answer"]))
        }
        
        return {
            "id": item.get("id"),
            "type": item.get("type"), # Type 1, 2, or 3 as per paper
            "input": question,
            "gt": gt_states
        }

    def __len__(self):
        return len(self.raw_data)