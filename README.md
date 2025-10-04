## Soft Computing

---
# 🧠 Soft Computing Learning Journey

<div align="center">

![Soft Computing Banner](media/images/banner.png)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.6%2B-orange?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](contributing/CONTRIBUTING.md)

**📚 Complete documentation of Soft Computing course for S1 Informatics**

[📖 Syllabus](SYLLABUS.md) • [🚀 Quick Start](#-quick-start) • [📊 Progress](#-learning-progress) • [💡 Projects](#-featured-projects) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 About This Repository

This repository documents my comprehensive learning journey in **Soft Computing** course at the Informatics undergraduate program. It contains all theoretical materials, practical implementations, assignments, projects, and personal experiments conducted throughout the semester.

### 🌟 What's Inside?

- 📘 **16 Weeks of Theory** - Detailed notes and summaries
- ⚙️ **11+ Lab Practices** - Hands-on implementations
- 💡 **4 Major Projects** - Real-world applications
- 🧪 **Research Experiments** - Parameter tuning and comparisons
- 📑 **Extensive References** - Books, papers, and resources
- 🛠️ **Reusable Tools** - Utilities and templates

---

## 📚 Course Content

### 📘 Part 1: Fuzzy Logic Systems (Week 1-5)
Learn about fuzzy sets, membership functions, fuzzy operations, and inference systems.

**Topics Covered:**
- Introduction to Soft Computing
- Fuzzy Sets Theory
- Membership Functions (Triangular, Trapezoidal, Gaussian)
- Fuzzy Operations (Union, Intersection, Complement)
- Fuzzy Inference Systems (Mamdani & Sugeno)
- Real-world Applications

**[📂 View Theory →](📘_theory/) | [⚙️ View Labs →](⚙️_practices/lab02_fuzzy_logic/)**

---

### 🧠 Part 2: Artificial Neural Networks (Week 6-9)
Deep dive into neural networks, from perceptrons to deep learning basics.

**Topics Covered:**
- Perceptron & Multi-layer Perceptron
- Activation Functions
- Backpropagation Algorithm
- Training & Optimization
- Overfitting & Regularization
- Introduction to CNN & RNN

**[📂 View Theory →](📘_theory/) | [⚙️ View Labs →](⚙️_practices/lab04_perceptron/)**

---

### 🧬 Part 3: Genetic Algorithms (Week 11-13)
Explore evolutionary computation and optimization techniques.

**Topics Covered:**
- Evolutionary Computation Basics
- GA Components (Population, Chromosome, Genes)
- Selection Methods
- Crossover & Mutation Operators
- Fitness Functions
- Real-world Optimization Problems

**[📂 View Theory →](📘_theory/) | [⚙️ View Labs →](⚙️_practices/lab08_genetic_algorithm/)**

---

### 🔄 Part 4: Hybrid & Advanced Systems (Week 14-16)
Combine multiple techniques for powerful hybrid systems.

**Topics Covered:**
- Neuro-Fuzzy Systems (ANFIS)
- Particle Swarm Optimization (PSO)
- Ant Colony Optimization (ACO)
- Hybrid Approaches
- Final Project Integration

**[📂 View Theory →](📘_theory/) | [⚙️ View Labs →](⚙️_practices/lab10_anfis/)**

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- Basic understanding of Python programming
- Jupyter Notebook (optional but recommended)

### Installation

1. **Clone this repository**
```bash
git clone https://github.com/hafizhhasyhari/SOFT-COMPUTING-COLLEGE-S1-2025-PUBLIC-KOMPUTASI-LUNAK.git
cd SOFT-COMPUTING-COLLEGE-S1-2025-PUBLIC-KOMPUTASI-LUNAK.git
'''

---

''' bash
│
├── README.md                              # Landing page utama
├── SYLLABUS.md                            # Silabus lengkap
├── LICENSE                                # MIT License
├── .gitignore                             # Python gitignore
├── requirements.txt                       # Dependencies
├── environment.yml                        # Conda environment
│
├── 📘_theory/                             # Materi Teori (per minggu)
│   ├── week01_introduction_soft_computing.md
│   ├── week02_soft_vs_hard_computing.md
│   ├── week03_fuzzy_sets_operations.md
│   ├── week04_membership_functions.md
│   ├── week05_fuzzy_inference_systems.md
│   ├── week06_perceptron_and_mlp.md
│   ├── week07_backpropagation.md
│   ├── week08_activation_functions.md
│   ├── week09_deep_learning_intro.md
│   ├── week10_midterm_review.md
│   ├── week11_genetic_algorithms_basics.md
│   ├── week12_selection_crossover_mutation.md
│   ├── week13_ga_applications.md
│   ├── week14_neuro_fuzzy_anfis.md
│   ├── week15_pso_aco_advanced.md
│   ├── week16_final_project_guide.md
│   ├── summary_fuzzy_logic.md
│   ├── summary_neural_networks.md
│   ├── summary_genetic_algorithms.md
│   └── exam_preparation_notes.md
│
├── ⚙️_practices/                          # Praktikum & Lab Work
│   ├── lab01_python_setup/
│   │   ├── installation_guide.md
│   │   ├── test_environment.py
│   │   └── screenshots/
│   ├── lab02_fuzzy_logic/
│   │   ├── fuzzy_sets_implementation.py
│   │   ├── membership_functions.py
│   │   ├── fuzzy_operations.py
│   │   ├── temperature_controller.py
│   │   └── lab_report_02.md
│   ├── lab03_fuzzy_inference/
│   │   ├── mamdani_system.py
│   │   ├── sugeno_system.py
│   │   ├── tipping_problem.py
│   │   └── lab_report_03.md
│   ├── lab04_perceptron/
│   │   ├── perceptron_from_scratch.py
│   │   ├── perceptron_visualization.ipynb
│   │   └── lab_report_04.md
│   ├── lab05_mlp_sklearn/
│   │   ├── mlp_classification.py
│   │   ├── mlp_regression.py
│   │   └── lab_report_05.md
│   ├── lab06_keras_basics/
│   │   ├── keras_sequential.py
│   │   ├── mnist_classifier.py
│   │   ├── model_training.ipynb
│   │   └── lab_report_06.md
│   ├── lab07_cnn_basics/
│   │   ├── cnn_architecture.py
│   │   ├── image_classification.py
│   │   └── lab_report_07.md
│   ├── lab08_genetic_algorithm/
│   │   ├── simple_ga.py
│   │   ├── ga_visualization.py
│   │   └── lab_report_08.md
│   ├── lab09_tsp_solver/
│   │   ├── tsp_genetic_algorithm.py
│   │   ├── tsp_visualization.ipynb
│   │   └── lab_report_09.md
│   ├── lab10_anfis/
│   │   ├── anfis_implementation.py
│   │   ├── neuro_fuzzy_demo.ipynb
│   │   └── lab_report_10.md
│   ├── lab11_pso/
│   │   ├── particle_swarm_optimization.py
│   │   ├── pso_visualization.py
│   │   └── lab_report_11.md
│   └── lab_datasets/                       # Dataset untuk praktikum
│       ├── iris.csv
│       ├── diabetes.csv
│       ├── mnist_sample/
│       └── README.md
│
├── 💡_projects/                           # Project & Assignments
│   ├── assignment01_fuzzy_logic_system/
│   │   ├── README.md
│   │   ├── requirements.md
│   │   ├── source_code/
│   │   │   ├── main.py
│   │   │   ├── fuzzy_controller.py
│   │   │   └── visualization.py
│   │   ├── documentation/
│   │   │   ├── project_report.pdf
│   │   │   ├── user_guide.md
│   │   │   └── testing_results.md
│   │   ├── diagrams/
│   │   │   ├── system_architecture.png
│   │   │   └── membership_functions.png
│   │   └── demo_video_link.md
│   │
│   ├── assignment02_neural_network_classifier/
│   │   ├── README.md
│   │   ├── requirements.md
│   │   ├── source_code/
│   │   │   ├── train_model.py
│   │   │   ├── evaluate_model.py
│   │   │   └── predict.py
│   │   ├── models/
│   │   │   ├── best_model.h5
│   │   │   └── model_architecture.json
│   │   ├── notebooks/
│   │   │   ├── data_exploration.ipynb
│   │   │   └── model_training.ipynb
│   │   ├── results/
│   │   │   ├── accuracy_plot.png
│   │   │   ├── confusion_matrix.png
│   │   │   └── performance_metrics.txt
│   │   ├── documentation/
│   │   │   └── project_report.pdf
│   │   └── presentation.pdf
│   │
│   ├── assignment03_ga_optimization/
│   │   ├── README.md
│   │   ├── requirements.md
│   │   ├── source_code/
│   │   │   ├── genetic_algorithm.py
│   │   │   ├── fitness_functions.py
│   │   │   └── visualization.py
│   │   ├── results/
│   │   │   ├── convergence_plot.png
│   │   │   ├── best_solution.txt
│   │   │   └── performance_analysis.md
│   │   ├── documentation/
│   │   │   └── project_report.pdf
│   │   └── demo_screenshots/
│   │
│   └── final_project_hybrid_system/
│       ├── README.md
│       ├── proposal.md
│       ├── source_code/
│       │   ├── main.py
│       │   ├── fuzzy_module.py
│       │   ├── neural_module.py
│       │   ├── ga_module.py
│       │   └── hybrid_system.py
│       ├── datasets/
│       ├── models/
│       ├── results/
│       ├── documentation/
│       │   ├── final_report.pdf
│       │   ├── technical_documentation.md
│       │   └── user_manual.md
│       ├── presentation/
│       │   ├── slides.pdf
│       │   └── demo_video.mp4
│       └── testing/
│           ├── test_cases.md
│           └── test_results.md
│
├── 🧪_experiments/                        # Eksperimen & Research
│   ├── experiment01_fuzzy_membership_comparison/
│   │   ├── README.md
│   │   ├── triangular_vs_gaussian.py
│   │   ├── results.ipynb
│   │   └── conclusion.md
│   ├── experiment02_activation_functions/
│   │   ├── README.md
│   │   ├── compare_activations.py
│   │   ├── performance_analysis.ipynb
│   │   └── findings.md
│   ├── experiment03_ga_parameters_tuning/
│   │   ├── README.md
│   │   ├── parameter_experiments.py
│   │   ├── results_visualization.ipynb
│   │   └── optimal_params.md
│   └── experiment04_hybrid_approaches/
│       ├── README.md
│       ├── fuzzy_nn.py
│       ├── ga_nn.py
│       ├── comparison.ipynb
│       └── conclusions.md
│
├── 📑_references/                         # Referensi & Resources
│   ├── README.md
│   ├── textbooks_and_papers.md
│   ├── online_courses_tutorials.md
│   ├── useful_websites.md
│   ├── youtube_channels.md
│   ├── cheatsheets/
│   │   ├── fuzzy_logic_cheatsheet.md
│   │   ├── neural_networks_cheatsheet.md
│   │   ├── genetic_algorithms_cheatsheet.md
│   │   ├── python_numpy_cheatsheet.md
│   │   └── scikit_learn_cheatsheet.md
│   ├── code_snippets/
│   │   ├── fuzzy_templates.py
│   │   ├── nn_templates.py
│   │   └── ga_templates.py
│   └── datasets_sources/
│       ├── public_datasets.md
│       └── dataset_preprocessing_tips.md
│
├── 🛠️_tools/                              # Utilities & Helpers
│   ├── README.md
│   ├── setup_guide.md
│   ├── data_preprocessing/
│   │   ├── data_loader.py
│   │   ├── data_cleaner.py
│   │   └── feature_engineering.py
│   ├── visualization/
│   │   ├── plot_fuzzy.py
│   │   ├── plot_neural_network.py
│   │   ├── plot_ga_convergence.py
│   │   └── plot_templates.py
│   ├── evaluation/
│   │   ├── metrics.py
│   │   ├── performance_evaluator.py
│   │   └── model_comparison.py
│   ├── templates/
│   │   ├── project_template/
│   │   ├── lab_report_template.md
│   │   └── notebook_template.ipynb
│   └── scripts/
│       ├── setup_environment.sh
│       ├── run_all_tests.py
│       └── generate_report.py
│
├── 📝_notes/                              # Catatan Kuliah & Exam Prep
│   ├── lecture_notes/
│   │   ├── week01_notes.md
│   │   ├── week02_notes.md
│   │   ├── week03_notes.md
│   │   └── ...
│   ├── exam_preparation/
│   │   ├── midterm_review.md
│   │   ├── midterm_practice_questions.md
│   │   ├── finals_review.md
│   │   └── finals_practice_questions.md
│   ├── key_concepts/
│   │   ├── important_formulas.md
│   │   ├── key_algorithms.md
│   │   └── common_mistakes.md
│   └── personal_insights/
│       ├── learning_reflections.md
│       └── tips_and_tricks.md
│
├── 🎤_presentations/                      # Presentasi & Slides
│   ├── week_presentations/
│   │   ├── week03_fuzzy_logic.pdf
│   │   ├── week07_neural_networks.pdf
│   │   └── week12_genetic_algorithms.pdf
│   ├── assignment_presentations/
│   │   ├── assignment01_presentation.pdf
│   │   ├── assignment02_presentation.pdf
│   │   └── assignment03_presentation.pdf
│   ├── final_presentation/
│   │   ├── final_project_slides.pdf
│   │   ├── demo_video.mp4
│   │   └── poster.png
│   └── templates/
│       └── presentation_template.pptx
│
├── 📸_media/                              # Assets & Media Files
│   ├── images/
│
├── 📊_progress/                           # Progress Tracking
│   ├── weekly_progress.md
│   ├── assignment_checklist.md
│   ├── lab_completion_status.md
│   └── learning_goals.md
│
└── 🤝_contributing/                       # Contribution Guidelines
    ├── CONTRIBUTING.md
    ├── CODE_OF_CONDUCT.md
    └── PULL_REQUEST_TEMPLATE.md
'''
