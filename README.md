# Machine4MPS: An Automated Benchmark Machine for Process-aware Evaluation and AI-Driven Discovery of MWP Solvers

This repository contains the official implementation of **Machine4MPS**, a framework designed for the systematic evaluation and automated discovery of Math Word Problem (MWP) solvers. Unlike traditional outcome-centric benchmarks, Machine4MPS leverages **State-Transform Theory** to decompose solvers into modular components, enabling fine-grained process-aware diagnosis and the automated search for optimized solver configurations.



## 🌟 Key Features

- **State-Transform Framework:** A unified representation space that treats MWP solving as a sequence of transitions between 8 core states (Text, Logic, Equation, etc.).
- **Process-aware Confusion Comparison (PCC):** A novel evaluation protocol that tracks error propagation across different reasoning stages rather than just checking the final answer.
- **AI-Driven Discovery:** A closed-loop pipeline that automatically explores, recombines, and discovers superior solver compositions (e.g., discovering that `BERT+DT` outperforms many LLMs).
- **LMV24K Dataset Support:** Full integration with the LMV24K dataset, providing rich intermediate annotations for multi-step reasoning.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- PyTorch 2.0+
- CUDA 11.7+ (for neural model evaluation)

### Installation
```bash
# Clone the repository
git clone https://github.com/anonymous/Machine4MPS.git
cd Machine4MPS

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

---

## 📊 Usage

### 1. Process-aware Evaluation (PCC)
To evaluate a specific solver configuration and generate a process-aware diagnostic report:

```bash
python evaluate.py \
    --model_config configs/solvers/bert_dt.yaml \
    --dataset data/LMV24K \
    --protocol pcc \
    --output_dir ./results/eval_results
```

### 2. Automated Solver Discovery
To start the automated discovery process to find the optimal combination of modules:

```bash
python discovery.py \
    --search_space configs/search_space/modular_transforms.yaml \
    --iterations 50 \
    --metric accuracy_and_process_consistency
```

---

## 📂 Project Structure

```text
Machine4MPS/
├── configs/            # Configuration files for models, datasets, and search spaces
├── core/
│   ├── states.py       # Definition of the 8 core states in State-Transform Theory
│   ├── transforms.py   # Modular implementation of solver components (LLM, Rule-based, etc.)
│   └── engine.py       # The execution engine for the benchmark machine
├── data/               # Dataset loading and preprocessing scripts (LMV24K)
├── evaluation/
│   ├── metrics.py      # Standard metrics and PCC implementation
│   └── analyzer.py     # Error propagation and stage-wise analysis tools
├── scripts/            # Utility scripts for data conversion and visualization
├── main.py             # Entry point for running experiments
└── requirements.txt
```

---

## 📝 Theory Overview: State-Transform

Machine4MPS models the solving process as:
$$S_0 \xrightarrow{T_1} S_1 \xrightarrow{T_2} \dots \xrightarrow{T_n} S_{ans}$$
where each $S$ represents a structured state (e.g., a Quantitative Relation Graph) and each $T$ is a transform (e.g., a neural encoder or a symbolic solver). This allows us to swap a "Black-box LLM" transform with a "Modular Neural-Symbolic" transform to compare efficiency and interpretability.

---

## 📈 LMV24K Dataset
The framework is optimized for the **LMV24K** dataset, which includes:
- **24,000+** problems with fine-grained annotations.
- **Type 1/2/3** categorization based on reasoning complexity.
- **Intermediate Ground-truth** for Equations, Logic Graphs, and Numerical Relations.

---

## 🎓 Citation

If you find this work useful in your research, please cite our paper:

```bibtex
@inproceedings{machine4mps2024,
  title={Machine4MPS: An Automated Benchmark Machine for Process-aware Evaluation and AI-Driven Discovery of Math Word Problem Solvers},
  author={Anonymous Authors},
  booktitle={Submitted to NeurIPS 2024},
  year={2024}
}
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




