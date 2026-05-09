class PCCEvaluator:
    """Fine-grained diagnostic evaluation."""
    def evaluate(self, prediction: float, ground_truth: float):
        is_correct = (prediction == ground_truth)
        result = {
            "accuracy": 1.0 if is_correct else 0.0,
            "status": "SUCCESS" if is_correct else "FAILURE"
        }
        return result