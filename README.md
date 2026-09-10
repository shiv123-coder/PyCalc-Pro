<div align="center">

# 🧮 PyCalc Pro

### *Real-Time Smart Math Dashboard*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/NumPy-1.26-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Matplotlib-3.8-11557C?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib" />
</p>

**Type anything → Get instant results. No buttons needed.**

</div>

---

## 📖 Overview

**PyCalc Pro** is an advanced, real-time mathematical toolkit built with Python and Streamlit. It acts as a **smart math extension** – open the webpage and it automatically solves calculations as you type. No "Calculate" buttons, no page reloads – just instant, live results.

This project demonstrates core Python concepts learned during the **Rubicon Skill Development Python Training 2026**.

## ⚡ Features

### 🧮 Smart Expression Bar
- Type any math expression and get instant results
- Supports: `5!`, `sqrt(25)`, `gcd(12,8)`, `lcm(4,6)`, `sin(45)`, `fib(10)`, and more
- Step-by-step breakdown of complex expressions

### 🔢 Number Theory
- **Factorial** (recursion), **Fibonacci** sequence, **GCD/HCF** & **LCM**
- **Sum of Squares**, Sum of Cubes, Sum of N
- Prime checker, Armstrong number, Palindrome, Perfect number
- **nCr** (Combinations) & **nPr** (Permutations)
- Prime number generator (Sieve of Eratosthenes)

### 📐 Matrix Operations
- Addition, Subtraction, Multiplication (up to 5×5)
- Determinant, Inverse, Transpose, Trace, Rank
- Eigenvalue calculation
- All results update **live** as you change values

### 🧩 Sudoku Solver (9×9)
- Interactive 9×9 grid input
- **Recursive backtracking** algorithm
- Pre-loaded Easy, Medium, Hard puzzles
- Visual solution with highlighted solved cells

### ⭐ Pattern Generator
- Star patterns: Pyramid, Diamond, Butterfly, Hollow Square
- Number patterns: Floyd's Triangle, Pascal's Triangle
- Multiplication table generator
- All from **loops and functions** (training concepts)

### 🔄 Unit Converter
- 7 categories: Length, Weight, Temperature, Speed, Data, Area, Time
- **Instant conversion** as you change values

### 📊 Graph Plotter
- Plot any math function: `x**2`, `sin(x)`, `exp(-x**2/2)`
- Adjustable X range, dark-themed plots
- Multiple function overlay support
- 10 pre-built example functions

## 🛠 Python Concepts Used

| Concept | Where Used |
|---------|-----------|
| **Functions (def)** | Every module – calculator, converter, analyzer |
| **Recursion** | Factorial, Fibonacci, GCD, Sudoku solver, digit_sum |
| **Lambda** | Expression evaluator, filter/map operations |
| **Loops (for/while)** | Pattern generator, matrix operations, prime sieve |
| **Conditionals** | Prime checker, Armstrong, input validation |
| **Libraries** | NumPy, Matplotlib, math, functools |

## 🚀 Setup & Run

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/PyCalc-Pro.git
cd PyCalc-Pro

# Create virtual environment (optional)
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📂 Project Structure

```
PyCalc-Pro/
├── app.py                    # Main single-page dashboard
├── utils/
│   ├── __init__.py
│   ├── smart_parser.py       # Expression parser (auto-detect & solve)
│   ├── math_functions.py     # Core math (recursion, lambda, functions)
│   ├── matrix_ops.py         # Matrix operations (NumPy)
│   ├── sudoku_solver.py      # 9×9 Sudoku solver (backtracking)
│   ├── pattern_gen.py        # Star & number patterns (loops)
│   ├── converter.py          # Unit conversions
│   └── grapher.py            # Function plotting (Matplotlib)
├── .streamlit/
│   └── config.toml           # Dark theme configuration
├── requirements.txt
├── .gitignore
└── README.md
```

## ☁️ Deployment

Deployed on **Streamlit Cloud**: [Live URL will be added after deployment]

## 👤 Author

- **Shivshankar Mali**
- Email: shivashankrmali7@gmail.com
- Phone: 9370717823

## 📜 License

This project is built as part of the **Rubicon Skill Development** Python Training Program 2026.

<div align="center">
  <p><em>Built with ❤️ using Python</em></p>
</div>
