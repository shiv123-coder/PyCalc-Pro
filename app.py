# ============================================================
# PyCalc Pro – Real-Time Smart Math Dashboard
# Built with Python + Streamlit
# Demonstrates: Functions, Recursion, Lambda, Loops (Rubicon Training)
# ============================================================

import streamlit as st
import numpy as np
import copy
import math

from PIL import Image
icon_img = Image.open("chrome_extension/icon.png")

# Page config must be the very first Streamlit command
st.set_page_config(
    page_title="Rubicon MathSolver Pro | Intelligent Calculator",
    page_icon=icon_img,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Import utility modules
from utils.smart_parser import parse_and_evaluate, get_supported_functions
from utils.math_functions import (
    factorial, fibonacci, gcd, lcm, is_prime, prime_factors,
    all_factors, sum_of_squares, sum_of_cubes, sum_of_n,
    is_armstrong, is_palindrome, is_perfect, digit_sum,
    reverse_number, number_to_words, generate_primes, nCr, nPr,
    sin_deg, cos_deg, tan_deg, log_base, ln,
    get_even_numbers, get_odd_numbers, square_all, cube_all
)
from utils.matrix_ops import (
    matrix_add, matrix_subtract, matrix_multiply,
    matrix_transpose, matrix_determinant, matrix_inverse,
    matrix_trace, matrix_rank, matrix_eigenvalues, matrix_power,
    matrix_scalar_multiply
)
from utils.sudoku_solver import (
    solve_sudoku, is_valid_board, get_sample_puzzles, board_to_string
)
from utils.pattern_gen import PATTERNS
from utils.converter import CATEGORIES, get_units_for_category, convert
from utils.grapher import plot_function, plot_multiple, EXAMPLE_FUNCTIONS


# ============================================================
# CUSTOM CSS – Premium Dark Theme
# ============================================================

st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap');

    /* Global styles */
    .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* Hero header */
    .hero-header {
        background: linear-gradient(135deg, #0F0C29 0%, #302B63 50%, #24243E 100%);
        border-radius: 20px;
        padding: 2rem 2.5rem;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    }
    .hero-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(0, 212, 255, 0.05) 0%, transparent 60%);
        animation: pulse 8s ease-in-out infinite;
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.5; }
        50% { transform: scale(1.1); opacity: 1; }
    }
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(120deg, #00D4FF, #7B61FF, #FF6B9D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        position: relative;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        color: rgba(255, 255, 255, 0.6);
        font-size: 1rem;
        margin-top: 0.3rem;
        position: relative;
        font-weight: 400;
    }

    /* Result display */
    .result-box {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.12) 0%, rgba(123, 97, 255, 0.12) 100%);
        border: 1px solid rgba(0, 212, 255, 0.25);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    .result-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 2.2rem;
        font-weight: 700;
        color: #00D4FF;
        margin: 0;
    }
    .result-label {
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 0.3rem;
    }

    /* Step breakdown */
    .step-box {
        background: rgba(255, 255, 255, 0.03);
        border-left: 3px solid #7B61FF;
        padding: 0.8rem 1.2rem;
        margin: 0.4rem 0;
        border-radius: 0 8px 8px 0;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.8);
    }

    /* Section headers */
    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #FAFAFA;
        padding: 0.8rem 0;
        margin-top: 0.5rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Info cards */
    .info-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    .info-card:hover {
        border-color: rgba(0, 212, 255, 0.3);
        background: rgba(0, 212, 255, 0.05);
    }
    .info-card-value {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.5rem;
        font-weight: 700;
        color: #00D4FF;
    }
    .info-card-label {
        color: rgba(255, 255, 255, 0.5);
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.3rem;
    }

    /* Sudoku grid */
    .sudoku-cell {
        width: 45px;
        height: 45px;
        text-align: center;
        font-family: 'JetBrains Mono', monospace;
        font-size: 1.1rem;
        font-weight: 600;
    }

    /* Pattern display */
    .pattern-box {
        background: #0A0A0F;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 1.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 1rem;
        color: #FFD93D;
        line-height: 1.6;
        white-space: pre;
        overflow-x: auto;
    }

    /* Badge */
    .badge {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 20px;
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .badge-green {
        background: rgba(81, 207, 102, 0.15);
        color: #51CF66;
        border: 1px solid rgba(81, 207, 102, 0.3);
    }
    .badge-red {
        background: rgba(255, 107, 107, 0.15);
        color: #FF6B6B;
        border: 1px solid rgba(255, 107, 107, 0.3);
    }
    .badge-blue {
        background: rgba(0, 212, 255, 0.15);
        color: #00D4FF;
        border: 1px solid rgba(0, 212, 255, 0.3);
    }

    /* Hide Streamlit defaults for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Expander styling */
    .streamlit-expanderHeader {
        font-size: 1.1rem;
        font-weight: 600;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 20px;
    }

    /* Fix number input width */
    .stNumberInput > div {
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO HEADER
# ============================================================

st.markdown("""
<div class="hero-header">
    <p class="hero-title">🧮 PyCalc Pro</p>
    <p class="hero-subtitle">Real-Time Smart Math Dashboard • Type anything → Get instant results</p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# 1. SMART EXPRESSION BAR (Top of Page – Always Visible)
# ============================================================

st.markdown('<div class="section-header">⚡ Smart Expression Bar</div>', unsafe_allow_html=True)

col_input, col_help = st.columns([4, 1])

if "smart_expr" not in st.session_state:
    st.session_state.smart_expr = ""

def append_to_expr(val):
    st.session_state.smart_expr += str(val)

def clear_expr():
    st.session_state.smart_expr = ""

def backspace_expr():
    st.session_state.smart_expr = st.session_state.smart_expr[:-1]

with col_input:
    expression = st.text_input(
        "Type any math expression",
        placeholder="e.g.  5! + sqrt(144) + gcd(12, 8)    or    sin(45) * 2 + log(100)",
        label_visibility="collapsed",
        key="smart_expr"
    )

with col_help:
    show_help = st.toggle("📖 Help", key="show_help")

with st.expander("⌨️ On-Screen Keypad (Symbols, Numbers, Constants)", expanded=False):
    # Keypad rows
    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)
    with k1: st.button("7", on_click=append_to_expr, args=("7",), use_container_width=True)
    with k2: st.button("8", on_click=append_to_expr, args=("8",), use_container_width=True)
    with k3: st.button("9", on_click=append_to_expr, args=("9",), use_container_width=True)
    with k4: st.button("÷", on_click=append_to_expr, args=("/",), use_container_width=True)
    with k5: st.button("(", on_click=append_to_expr, args=("(",), use_container_width=True)
    with k6: st.button(")", on_click=append_to_expr, args=(")",), use_container_width=True)
    with k7: st.button("⌫", on_click=backspace_expr, use_container_width=True)
    
    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)
    with k1: st.button("4", on_click=append_to_expr, args=("4",), use_container_width=True)
    with k2: st.button("5", on_click=append_to_expr, args=("5",), use_container_width=True)
    with k3: st.button("6", on_click=append_to_expr, args=("6",), use_container_width=True)
    with k4: st.button("×", on_click=append_to_expr, args=("*",), use_container_width=True)
    with k5: st.button("sin", on_click=append_to_expr, args=("sin(",), use_container_width=True)
    with k6: st.button("cos", on_click=append_to_expr, args=("cos(",), use_container_width=True)
    with k7: st.button("tan", on_click=append_to_expr, args=("tan(",), use_container_width=True)
    
    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)
    with k1: st.button("1", on_click=append_to_expr, args=("1",), use_container_width=True)
    with k2: st.button("2", on_click=append_to_expr, args=("2",), use_container_width=True)
    with k3: st.button("3", on_click=append_to_expr, args=("3",), use_container_width=True)
    with k4: st.button("−", on_click=append_to_expr, args=("-",), use_container_width=True)
    with k5: st.button("sqrt", on_click=append_to_expr, args=("sqrt(",), use_container_width=True)
    with k6: st.button("log", on_click=append_to_expr, args=("log(",), use_container_width=True)
    with k7: st.button("^", on_click=append_to_expr, args=("^",), use_container_width=True)
    
    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)
    with k1: st.button("0", on_click=append_to_expr, args=("0",), use_container_width=True)
    with k2: st.button(".", on_click=append_to_expr, args=(".",), use_container_width=True)
    with k3: st.button("!", on_click=append_to_expr, args=("!",), use_container_width=True)
    with k4: st.button("+", on_click=append_to_expr, args=("+",), use_container_width=True)
    with k5: st.button("π", on_click=append_to_expr, args=("pi",), use_container_width=True)
    with k6: st.button("e", on_click=append_to_expr, args=("e",), use_container_width=True)
    with k7: st.button("C", on_click=clear_expr, type="primary", use_container_width=True)

# Show result automatically as user types
if expression:
    result, steps, error = parse_and_evaluate(expression)
    if error:
        st.markdown(f"""
        <div class="result-box" style="border-color: rgba(255, 107, 107, 0.3);">
            <p class="result-label">Error</p>
            <p class="result-value" style="color: #FF6B6B; font-size: 1.2rem;">{error}</p>
        </div>
        """, unsafe_allow_html=True)
    elif result is not None:
        st.markdown(f"""
        <div class="result-box">
            <p class="result-label">Result</p>
            <p class="result-value">= {result}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if steps:
            with st.expander("📝 Step-by-Step Breakdown", expanded=True):
                for step in steps:
                    st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)

if show_help:
    funcs = get_supported_functions()
    cols = st.columns(3)
    for i, (category, examples) in enumerate(funcs.items()):
        with cols[i % 3]:
            st.markdown(f"**{category}**")
            for ex in examples:
                st.code(ex, language=None)


# ============================================================
# TOOL SECTIONS (Expandable – All Auto-Solving)
# ============================================================

st.markdown("---")

# ============================================================
# 2. NUMBER THEORY
# ============================================================

with st.expander("🔢 Number Theory – Factorial, Fibonacci, GCD, LCM, Primes & More", expanded=False):
    
    tab_nt1, tab_nt2, tab_nt3 = st.tabs(["🔍 Number Analyzer", "🔗 GCD / LCM", "📊 Sequences"])
    
    with tab_nt1:
        st.markdown("##### Instant Number Analysis")
        num = st.number_input("Enter a number", value=120, step=1, key="nt_num", min_value=0, max_value=999999)
        
        if num is not None:
            n = int(num)
            
            # Row 1: Key properties
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                fact_val = factorial(n) if n <= 20 else "Too large"
                st.markdown(f"""<div class="info-card">
                    <div class="info-card-value">{fact_val}</div>
                    <div class="info-card-label">Factorial ({n}!)</div>
                </div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""<div class="info-card">
                    <div class="info-card-value">{sum_of_squares(n)}</div>
                    <div class="info-card-label">Sum of Squares</div>
                </div>""", unsafe_allow_html=True)
            with c3:
                st.markdown(f"""<div class="info-card">
                    <div class="info-card-value">{sum_of_cubes(n)}</div>
                    <div class="info-card-label">Sum of Cubes</div>
                </div>""", unsafe_allow_html=True)
            with c4:
                st.markdown(f"""<div class="info-card">
                    <div class="info-card-value">{sum_of_n(n)}</div>
                    <div class="info-card-label">Sum (1 to {n})</div>
                </div>""", unsafe_allow_html=True)
            
            # Row 2: Checks
            c5, c6, c7, c8 = st.columns(4)
            with c5:
                badge = "badge-green" if is_prime(n) else "badge-red"
                label = "Yes" if is_prime(n) else "No"
                st.markdown(f"""<div class="info-card">
                    <div><span class="badge {badge}">{label}</span></div>
                    <div class="info-card-label" style="margin-top:0.5rem">Prime?</div>
                </div>""", unsafe_allow_html=True)
            with c6:
                badge = "badge-green" if is_armstrong(n) else "badge-red"
                label = "Yes" if is_armstrong(n) else "No"
                st.markdown(f"""<div class="info-card">
                    <div><span class="badge {badge}">{label}</span></div>
                    <div class="info-card-label" style="margin-top:0.5rem">Armstrong?</div>
                </div>""", unsafe_allow_html=True)
            with c7:
                badge = "badge-green" if is_palindrome(n) else "badge-red"
                label = "Yes" if is_palindrome(n) else "No"
                st.markdown(f"""<div class="info-card">
                    <div><span class="badge {badge}">{label}</span></div>
                    <div class="info-card-label" style="margin-top:0.5rem">Palindrome?</div>
                </div>""", unsafe_allow_html=True)
            with c8:
                badge = "badge-green" if is_perfect(n) else "badge-red"
                label = "Yes" if is_perfect(n) else "No"
                st.markdown(f"""<div class="info-card">
                    <div><span class="badge {badge}">{label}</span></div>
                    <div class="info-card-label" style="margin-top:0.5rem">Perfect?</div>
                </div>""", unsafe_allow_html=True)
            
            # Row 3: Details
            st.markdown("")
            c9, c10 = st.columns(2)
            with c9:
                factors = all_factors(n)
                st.markdown(f"**All Factors ({len(factors)}):** `{factors}`")
                pf = prime_factors(n)
                st.markdown(f"**Prime Factors:** `{pf}`")
            with c10:
                st.markdown(f"**Digit Sum:** `{digit_sum(n)}`")
                st.markdown(f"**Reversed:** `{reverse_number(n)}`")
                st.markdown(f"**In Words:** *{number_to_words(n)}*")
    
    with tab_nt2:
        st.markdown("##### GCD (HCF) & LCM Calculator")
        c1, c2 = st.columns(2)
        with c1:
            a_val = st.number_input("Number A", value=12, step=1, key="gcd_a", min_value=1)
        with c2:
            b_val = st.number_input("Number B", value=8, step=1, key="gcd_b", min_value=1)
        
        gc, lc = st.columns(2)
        with gc:
            g = gcd(int(a_val), int(b_val))
            st.markdown(f"""<div class="info-card">
                <div class="info-card-value">{g}</div>
                <div class="info-card-label">GCD / HCF ({int(a_val)}, {int(b_val)})</div>
            </div>""", unsafe_allow_html=True)
        with lc:
            l = lcm(int(a_val), int(b_val))
            st.markdown(f"""<div class="info-card">
                <div class="info-card-value">{l}</div>
                <div class="info-card-label">LCM ({int(a_val)}, {int(b_val)})</div>
            </div>""", unsafe_allow_html=True)
        
        st.markdown("")
        st.markdown("##### Combinations & Permutations")
        cn1, cn2 = st.columns(2)
        with cn1:
            n_val = st.number_input("n", value=5, step=1, key="comb_n", min_value=0, max_value=20)
        with cn2:
            r_val = st.number_input("r", value=2, step=1, key="comb_r", min_value=0, max_value=20)
        
        cc1, cc2 = st.columns(2)
        with cc1:
            st.markdown(f"""<div class="info-card">
                <div class="info-card-value">{nCr(int(n_val), int(r_val))}</div>
                <div class="info-card-label">nCr ({int(n_val)}C{int(r_val)})</div>
            </div>""", unsafe_allow_html=True)
        with cc2:
            st.markdown(f"""<div class="info-card">
                <div class="info-card-value">{nPr(int(n_val), int(r_val))}</div>
                <div class="info-card-label">nPr ({int(n_val)}P{int(r_val)})</div>
            </div>""", unsafe_allow_html=True)
    
    with tab_nt3:
        st.markdown("##### Fibonacci Sequence")
        fib_n = st.slider("Number of terms", 1, 30, 10, key="fib_slider")
        fib_seq = fibonacci(fib_n)
        st.code(" → ".join(str(x) for x in fib_seq), language=None)
        
        st.markdown("##### Prime Numbers")
        prime_limit = st.slider("Generate primes up to", 10, 500, 100, key="prime_slider")
        primes = generate_primes(prime_limit)
        st.markdown(f"**Found {len(primes)} primes:**")
        st.code(", ".join(str(p) for p in primes), language=None)


# ============================================================
# 3. MATRIX OPERATIONS
# ============================================================

with st.expander("📐 Matrix Operations – Add, Multiply, Determinant, Inverse & More", expanded=False):
    
    tab_m1, tab_m2 = st.tabs(["🔢 Two Matrix Operations", "📊 Single Matrix Analysis"])
    
    with tab_m1:
        mc1, mc2, mc3 = st.columns([1, 1, 1])
        with mc1:
            m_rows = st.selectbox("Rows", [2, 3, 4, 5], index=0, key="m_rows")
        with mc2:
            m_cols = st.selectbox("Columns", [2, 3, 4, 5], index=0, key="m_cols")
        with mc3:
            m_op = st.selectbox("Operation", ["Add (A + B)", "Subtract (A - B)", "Multiply (A × B)"], key="m_op")
        
        st.markdown("**Matrix A:**")
        matrix_a = []
        for i in range(m_rows):
            cols = st.columns(m_cols)
            row = []
            for j in range(m_cols):
                with cols[j]:
                    val = st.number_input(f"A[{i+1}][{j+1}]", value=0.0, key=f"ma_{i}_{j}",
                                         label_visibility="collapsed", step=1.0)
                    row.append(val)
            matrix_a.append(row)
        
        # For multiply, B might have different dimensions
        if "Multiply" in m_op:
            b_rows = m_cols  # A's cols must equal B's rows
            b_cols_sel = st.selectbox("Matrix B columns", [2, 3, 4, 5], index=0, key="mb_cols")
        else:
            b_rows = m_rows
            b_cols_sel = m_cols
        
        st.markdown("**Matrix B:**")
        matrix_b = []
        for i in range(b_rows):
            cols = st.columns(b_cols_sel)
            row = []
            for j in range(b_cols_sel):
                with cols[j]:
                    val = st.number_input(f"B[{i+1}][{j+1}]", value=0.0, key=f"mb_{i}_{j}",
                                         label_visibility="collapsed", step=1.0)
                    row.append(val)
            matrix_b.append(row)
        
        # Auto-calculate result
        if "Add" in m_op:
            result, err = matrix_add(matrix_a, matrix_b)
        elif "Subtract" in m_op:
            result, err = matrix_subtract(matrix_a, matrix_b)
        else:
            result, err = matrix_multiply(matrix_a, matrix_b)
        
        st.markdown("**Result:**")
        if err:
            st.error(err)
        elif result:
            result_arr = np.array(result)
            st.dataframe(result_arr, use_container_width=True)
    
    with tab_m2:
        st.markdown("##### Analyze a Single Matrix")
        s_size = st.selectbox("Matrix size", ["2×2", "3×3", "4×4", "5×5"], index=1, key="s_size")
        s_n = int(s_size[0])
        
        st.markdown("**Enter Matrix:**")
        single_matrix = []
        for i in range(s_n):
            cols = st.columns(s_n)
            row = []
            for j in range(s_n):
                with cols[j]:
                    val = st.number_input(f"M[{i+1}][{j+1}]", value=float(1 if i == j else 0),
                                         key=f"sm_{i}_{j}", label_visibility="collapsed", step=1.0)
                    row.append(val)
            single_matrix.append(row)
        
        # Auto-compute all properties
        det, _ = matrix_determinant(single_matrix)
        tr, _ = matrix_trace(single_matrix)
        rk, _ = matrix_rank(single_matrix)
        trans, _ = matrix_transpose(single_matrix)
        inv, inv_err = matrix_inverse(single_matrix)
        eigen, eigen_err = matrix_eigenvalues(single_matrix)
        
        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown(f"""<div class="info-card">
                <div class="info-card-value">{det}</div>
                <div class="info-card-label">Determinant</div>
            </div>""", unsafe_allow_html=True)
        with r2:
            st.markdown(f"""<div class="info-card">
                <div class="info-card-value">{tr}</div>
                <div class="info-card-label">Trace</div>
            </div>""", unsafe_allow_html=True)
        with r3:
            st.markdown(f"""<div class="info-card">
                <div class="info-card-value">{rk}</div>
                <div class="info-card-label">Rank</div>
            </div>""", unsafe_allow_html=True)
        
        tc1, tc2 = st.columns(2)
        with tc1:
            st.markdown("**Transpose:**")
            if trans:
                st.dataframe(np.array(trans), use_container_width=True)
        with tc2:
            st.markdown("**Inverse:**")
            if inv:
                st.dataframe(np.round(np.array(inv), 4), use_container_width=True)
            elif inv_err:
                st.warning(inv_err)
        
        if eigen is not None:
            st.markdown(f"**Eigenvalues:** `{eigen}`")


# ============================================================
# 4. SUDOKU SOLVER
# ============================================================

with st.expander("🧩 Sudoku Solver – 9×9 Backtracking Algorithm (Recursion)", expanded=False):
    
    st.markdown("Enter the puzzle below (leave 0 for empty cells). The solver uses **recursive backtracking**.")
    
    # Sample puzzle selector
    sample_choice = st.selectbox("Load sample puzzle:", ["Custom (enter your own)", "Easy", "Medium", "Hard"], key="sudoku_sample")
    
    samples = get_sample_puzzles()
    
    # Initialize board in session state
    if 'sudoku_board' not in st.session_state:
        st.session_state.sudoku_board = [[0]*9 for _ in range(9)]
    
    if sample_choice != "Custom (enter your own)" and st.button("📥 Load Puzzle", key="load_puzzle"):
        st.session_state.sudoku_board = [row[:] for row in samples[sample_choice]]
        st.rerun()
    
    # Display 9x9 grid
    st.markdown("##### Puzzle Input")
    board = []
    for i in range(9):
        cols = st.columns(9)
        row = []
        for j in range(9):
            with cols[j]:
                default = st.session_state.sudoku_board[i][j] if st.session_state.sudoku_board[i][j] != 0 else 0
                val = st.number_input(
                    f"Cell ({i+1},{j+1})",
                    min_value=0, max_value=9, value=int(default), step=1,
                    key=f"sud_{i}_{j}",
                    label_visibility="collapsed"
                )
                row.append(int(val))
        board.append(row)
    
    if st.button("🚀 Solve Sudoku", key="solve_sudoku", type="primary", use_container_width=True):
        # Validate board
        valid, conflict = is_valid_board(board)
        if not valid:
            st.error(f"❌ Invalid puzzle! Conflict at row {conflict[0]+1}, column {conflict[1]+1}")
        else:
            solution = copy.deepcopy(board)
            if solve_sudoku(solution):
                st.success("✅ Puzzle Solved!")
                st.markdown("##### Solution")
                
                # Display solved grid
                for i in range(9):
                    cols = st.columns(9)
                    for j in range(9):
                        with cols[j]:
                            original = board[i][j]
                            solved = solution[i][j]
                            if original == 0:
                                st.markdown(f"<div style='text-align:center;background:rgba(0,212,255,0.15);border-radius:6px;padding:8px;font-family:JetBrains Mono;font-weight:700;color:#00D4FF;font-size:1.1rem;'>{solved}</div>", unsafe_allow_html=True)
                            else:
                                st.markdown(f"<div style='text-align:center;background:rgba(255,255,255,0.05);border-radius:6px;padding:8px;font-family:JetBrains Mono;font-weight:500;color:#FAFAFA;font-size:1.1rem;'>{solved}</div>", unsafe_allow_html=True)
            else:
                st.error("❌ No solution exists for this puzzle.")


# ============================================================
# 5. PATTERN GENERATOR
# ============================================================

with st.expander("⭐ Pattern Generator – Star & Number Patterns (Loops)", expanded=False):
    
    pc1, pc2 = st.columns([2, 1])
    with pc1:
        pattern_choice = st.selectbox("Select Pattern", list(PATTERNS.keys()), key="pattern_select")
    with pc2:
        pattern_size = st.slider("Size", 3, 15, 5, key="pattern_size")
    
    # Auto-generate pattern
    pattern = PATTERNS[pattern_choice](pattern_size)
    st.markdown(f'<div class="pattern-box">{pattern}</div>', unsafe_allow_html=True)


# ============================================================
# 6. UNIT CONVERTER
# ============================================================

with st.expander("🔄 Unit Converter – Length, Weight, Temperature, Speed & More", expanded=False):
    
    uc1, uc2 = st.columns([1, 3])
    with uc1:
        category = st.selectbox("Category", list(CATEGORIES.keys()), key="conv_cat")
    
    units = get_units_for_category(category)
    
    with uc2:
        cc1, cc2, cc3 = st.columns([2, 1, 2])
        with cc1:
            from_unit = st.selectbox("From", units, key="conv_from")
            value = st.number_input("Value", value=1.0, key="conv_val", format="%.6f")
        with cc2:
            st.markdown("<div style='text-align:center;padding:2rem 0;font-size:2rem;'>→</div>", unsafe_allow_html=True)
        with cc3:
            to_unit = st.selectbox("To", units, index=min(1, len(units)-1), key="conv_to")
            result, err = convert(value, from_unit, to_unit, category)
            if err:
                st.error(err)
            elif result is not None:
                st.markdown(f"""<div class="result-box">
                    <p class="result-value" style="font-size:1.6rem;">{result:,.6g}</p>
                    <p class="result-label">{to_unit}</p>
                </div>""", unsafe_allow_html=True)


# ============================================================
# 7. GRAPH PLOTTER
# ============================================================

with st.expander("📊 Graph Plotter – Plot Any Math Function", expanded=False):
    
    gc1, gc2 = st.columns([3, 1])
    with gc1:
        func_expr = st.text_input(
            "Function (use 'x' as variable)",
            value="x**2",
            placeholder="e.g. sin(x), x**3 - 3*x, exp(-x**2)",
            key="graph_func"
        )
    with gc2:
        example = st.selectbox("Examples", ["Custom"] + list(EXAMPLE_FUNCTIONS.keys()), key="graph_example")
        if example != "Custom":
            func_expr = EXAMPLE_FUNCTIONS[example]
    
    gr1, gr2 = st.columns(2)
    with gr1:
        x_min = st.number_input("X min", value=-10.0, key="graph_xmin")
    with gr2:
        x_max = st.number_input("X max", value=10.0, key="graph_xmax")
    
    if func_expr:
        fig, err = plot_function(func_expr, x_min, x_max)
        if fig:
            st.pyplot(fig)
        if err:
            st.error(err)
    
    # Multiple function plotting
    with st.popover("📈 Plot Multiple Functions"):
        st.markdown("Enter one function per line:")
        multi_funcs = st.text_area(
            "Functions",
            value="sin(x)\ncos(x)\nx/5",
            key="multi_funcs",
            label_visibility="collapsed"
        )
        if multi_funcs:
            func_list = [f.strip() for f in multi_funcs.strip().split("\n") if f.strip()]
            if func_list:
                fig, errors = plot_multiple(func_list, x_min, x_max)
                if fig:
                    st.pyplot(fig)
                if errors:
                    for e in errors:
                        st.warning(e)


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.3); font-size: 0.85rem; padding: 1rem 0;">
    <p><strong>PyCalc Pro</strong> • Built with Python & Streamlit</p>
    <p>Concepts: Functions • Recursion • Lambda • Loops • Libraries</p>
    <p style="font-size:0.75rem;">Rubicon Skill Development – Python Training Project 2026</p>
</div>
""", unsafe_allow_html=True)
