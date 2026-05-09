from typing import List, Dict, Any
from core.states import State

class ErrorAnalyzer:
    """
    Implements Process-aware Confusion Comparison (PCC).
    Analyzes where and why a solver fails during the multi-step reasoning process
    by identifying the 'Confusion Point' in the State-Transform sequence.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.first_error_stage = -1
        self.is_consistent = True

    def analyze_propagation(self, prediction_history: List[State], gt_history: List[State]) -> Dict[str, Any]:
        """
        Compares the predicted state sequence against the ground truth sequence.
        
        Args:
            prediction_history: List of states produced by the solver pipeline.
            gt_history: List of gold-standard states for the same problem.
            
        Returns:
            A diagnostic dictionary containing the error location and propagation map.
        """
        self.reset()
        results = []
        
        # We start comparison from stage 1 (first transformation) as stage 0 is the input text
        max_stages = min(len(prediction_history), len(gt_history))
        
        for i in range(1, max_stages):
            pred_state = prediction_history[i]
            gt_state = gt_history[i]
            
            is_match = self._compare_states(pred_state, gt_state)
            
            status = "PASS" if is_match else "FAIL"
            
            # Detect the first point of failure (The Confusion Point)
            if not is_match and self.is_consistent:
                self.is_consistent = False
                self.first_error_stage = i
            
            results.append({
                "stage": i,
                "type": pred_state.state_type,
                "status": status
            })

        return {
            "is_correct": self.is_consistent,
            "confusion_point_index": self.first_error_stage,
            "confusion_stage_type": prediction_history[self.first_error_stage].state_type if not self.is_consistent else None,
            "details": results
        }

    def _compare_states(self, pred: State, gt: State) -> bool:
        """
        Performs stage-specific content comparison.
        In a production environment, this could involve symbolic equivalence 
        checking or graph isomorphism for LogicStates.
        """
        if pred.state_type != gt.state_type:
            return False
            
        # Basic content equivalence check
        return pred.content == gt.content

    def generate_diagnostic_report(self, analysis: Dict[str, Any]) -> str:
        """
        Converts the analysis dictionary into a human-readable diagnostic summary.
        """
        if analysis["is_correct"]:
            return "DIAGNOSIS: SUCCESS. The solver followed the correct reasoning path."
        
        err_idx = analysis["confusion_point_index"]
        err_type = analysis["confusion_stage_type"]
        
        report = f"DIAGNOSIS: FAILURE. Reasoning chain corrupted at Stage {err_idx} ({err_type}).\n"
        report += "Execution Trace:\n"
        for step in analysis["details"]:
            report += f"  [Step {step['stage']}] {step['type']:<12}: {step['status']}\n"
            
        report += f"Actionable Insight: Focus on optimizing the Transform leading to {err_type}."
        return report

# Example of standalone usage for testing
if __name__ == "__main__":
    from core.states import TextState, AnswerState
    
    # Mock data
    pred_hist = [TextState("Query"), AnswerState(10.0)]
    gt_hist = [TextState("Query"), AnswerState(15.0)]
    
    analyzer = ErrorAnalyzer()
    res = analyzer.analyze_propagation(pred_hist, gt_hist)
    print(analyzer.generate_diagnostic_report(res))