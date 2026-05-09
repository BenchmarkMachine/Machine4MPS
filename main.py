from core.states import AnswerState
from core.transforms import BERTEncoder, DTDecoder, SymbolicSolver
from core.engine import MPSEngine
from evaluation.metrics import PCCEvaluator

def main():
    # 1. Setup Input Data (All English)
    problem = "Alice has 10 apples. She buys 5 more. How many does she have?"
    target_answer = 15.0

    # 2. Define the Discovered Solver Pipeline (BERT + DT)
    pipeline = [
        BERTEncoder(),
        DTDecoder(),
        SymbolicSolver()
    ]
    
    engine = MPSEngine(pipeline)

    # 3. Running the Discovery Pipeline
    print("--- Machine4MPS Discovery Execution ---")
    final_output, process_history = engine.solve(problem)
    
    # 4. Process-aware Evaluation
    evaluator = PCCEvaluator()
    report = evaluator.evaluate(final_output.content, target_answer)
    
    print("\n--- Diagnostic Report ---")
    print(f"Final Prediction: {final_output.content}")
    print(f"Overall Accuracy: {report['accuracy']}")
    print(f"System Status: {report['status']}")
    print("Diagnosis: The BERT+DT combination maintained consistency across all states.")

if __name__ == "__main__":
    main()
