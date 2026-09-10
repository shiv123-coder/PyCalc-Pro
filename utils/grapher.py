# Graph Plotter Module
# Uses matplotlib and numpy for plotting mathematical functions

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for Streamlit


def plot_function(expression, x_min=-10, x_max=10, num_points=500, title=None):
    """
    Plot a mathematical function.
    expression: string like 'x**2', 'np.sin(x)', 'x**3 - 3*x'
    Returns: matplotlib figure
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Set dark theme
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#1A1D23')
    ax.tick_params(colors='#FAFAFA')
    ax.xaxis.label.set_color('#FAFAFA')
    ax.yaxis.label.set_color('#FAFAFA')
    ax.title.set_color('#FAFAFA')
    for spine in ax.spines.values():
        spine.set_color('#333333')
    
    x = np.linspace(x_min, x_max, num_points)
    
    # Prepare safe namespace for eval
    safe_ns = {
        'x': x, 'np': np,
        'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
        'sqrt': np.sqrt, 'abs': np.abs,
        'log': np.log10, 'ln': np.log, 'exp': np.exp,
        'pi': np.pi, 'e': np.e,
        'arcsin': np.arcsin, 'arccos': np.arccos, 'arctan': np.arctan,
    }
    
    try:
        # Preprocess expression
        expr = expression.replace('^', '**')
        y = eval(expr, {"__builtins__": {}}, safe_ns)
        
        if isinstance(y, (int, float)):
            y = np.full_like(x, y)
        
        # Handle infinities and NaN for cleaner plot
        y = np.where(np.isfinite(y), y, np.nan)
        
        # Plot with gradient effect
        ax.plot(x, y, color='#00D4FF', linewidth=2.5, label=f'y = {expression}')
        ax.fill_between(x, y, alpha=0.1, color='#00D4FF')
        
        # Add grid and axes
        ax.axhline(y=0, color='#555555', linewidth=0.8)
        ax.axvline(x=0, color='#555555', linewidth=0.8)
        ax.grid(True, alpha=0.15, color='#FAFAFA')
        
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.set_title(title or f'y = {expression}', fontsize=14, fontweight='bold')
        ax.legend(facecolor='#1A1D23', edgecolor='#333333', labelcolor='#FAFAFA')
        
        plt.tight_layout()
        return fig, None
        
    except Exception as e:
        plt.close(fig)
        return None, f"Error plotting: {str(e)}"


def plot_multiple(expressions, x_min=-10, x_max=10, num_points=500):
    """Plot multiple functions on the same axes."""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#1A1D23')
    ax.tick_params(colors='#FAFAFA')
    ax.xaxis.label.set_color('#FAFAFA')
    ax.yaxis.label.set_color('#FAFAFA')
    ax.title.set_color('#FAFAFA')
    for spine in ax.spines.values():
        spine.set_color('#333333')
    
    x = np.linspace(x_min, x_max, num_points)
    colors = ['#00D4FF', '#FF6B6B', '#51CF66', '#FFD93D', '#CC5DE8', '#FF922B']
    
    safe_ns = {
        'x': x, 'np': np,
        'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
        'sqrt': np.sqrt, 'abs': np.abs,
        'log': np.log10, 'ln': np.log, 'exp': np.exp,
        'pi': np.pi, 'e': np.e,
        'arcsin': np.arcsin, 'arccos': np.arccos, 'arctan': np.arctan,
    }
    
    plotted = False
    errors = []
    
    for i, expr_str in enumerate(expressions):
        expr_str = expr_str.strip()
        if not expr_str:
            continue
        try:
            expr = expr_str.replace('^', '**')
            y = eval(expr, {"__builtins__": {}}, safe_ns)
            if isinstance(y, (int, float)):
                y = np.full_like(x, y)
            y = np.where(np.isfinite(y), y, np.nan)
            color = colors[i % len(colors)]
            ax.plot(x, y, color=color, linewidth=2.5, label=f'y = {expr_str}')
            plotted = True
        except Exception as e:
            errors.append(f"'{expr_str}': {str(e)}")
    
    if plotted:
        ax.axhline(y=0, color='#555555', linewidth=0.8)
        ax.axvline(x=0, color='#555555', linewidth=0.8)
        ax.grid(True, alpha=0.15, color='#FAFAFA')
        ax.set_xlabel('x', fontsize=12)
        ax.set_ylabel('y', fontsize=12)
        ax.set_title('Function Plot', fontsize=14, fontweight='bold')
        ax.legend(facecolor='#1A1D23', edgecolor='#333333', labelcolor='#FAFAFA')
        plt.tight_layout()
        return fig, errors if errors else None
    
    plt.close(fig)
    return None, errors or ["No valid expressions to plot."]


# Pre-built example functions
EXAMPLE_FUNCTIONS = {
    "Parabola": "x**2",
    "Cubic": "x**3 - 3*x",
    "Sine Wave": "sin(x)",
    "Cosine Wave": "cos(x)",
    "Exponential": "exp(x/5)",
    "Logarithm": "ln(abs(x) + 0.01)",
    "Square Root": "sqrt(abs(x))",
    "Absolute Value": "abs(x)",
    "Damped Sine": "exp(-abs(x)/5) * sin(x*3)",
    "Gaussian": "exp(-x**2 / 2)",
}
