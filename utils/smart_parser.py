# Smart Expression Parser
# Parses natural math expressions like "5! + sqrt(144) + gcd(12,8)"
# and evaluates them with step-by-step breakdown

import re
import math
from utils.math_functions import (
    factorial, fibonacci_nth, gcd, lcm, power,
    is_prime, sum_of_squares, sum_of_cubes, nCr, nPr,
    sin_deg, cos_deg, tan_deg, log_base, ln
)


def parse_and_evaluate(expression):
    """
    Parse a mathematical expression and return result + steps.
    Returns: (result, steps_list, error_message)
    """
    if not expression or not expression.strip():
        return None, [], None
    
    original = expression.strip()
    steps = []
    expr = original
    
    try:
        # Step 1: Replace factorial notation (e.g., 5!)
        factorial_pattern = r'(\d+)!'
        for match in re.finditer(factorial_pattern, expr):
            n = int(match.group(1))
            val = factorial(n)
            steps.append(f"{n}! = {val}")
        expr = re.sub(factorial_pattern, lambda m: str(factorial(int(m.group(1)))), expr)
        
        # Step 2: Replace function calls
        function_map = {
            'sqrt': (lambda args: math.sqrt(args[0]), 1),
            'cbrt': (lambda args: args[0] ** (1/3), 1),
            'abs': (lambda args: abs(args[0]), 1),
            'ceil': (lambda args: math.ceil(args[0]), 1),
            'floor': (lambda args: math.floor(args[0]), 1),
            'round': (lambda args: round(args[0], int(args[1]) if len(args) > 1 else 0), 1),
            'sin': (lambda args: sin_deg(args[0]), 1),
            'cos': (lambda args: cos_deg(args[0]), 1),
            'tan': (lambda args: tan_deg(args[0]), 1),
            'log': (lambda args: log_base(args[0], args[1] if len(args) > 1 else 10), 1),
            'ln': (lambda args: ln(args[0]), 1),
            'exp': (lambda args: math.exp(args[0]), 1),
            'gcd': (lambda args: gcd(int(args[0]), int(args[1])), 2),
            'hcf': (lambda args: gcd(int(args[0]), int(args[1])), 2),
            'lcm': (lambda args: lcm(int(args[0]), int(args[1])), 2),
            'fib': (lambda args: fibonacci_nth(int(args[0])), 1),
            'factorial': (lambda args: factorial(int(args[0])), 1),
            'pow': (lambda args: power(args[0], args[1]), 2),
            'ncr': (lambda args: nCr(int(args[0]), int(args[1])), 2),
            'npr': (lambda args: nPr(int(args[0]), int(args[1])), 2),
            'sumsq': (lambda args: sum_of_squares(int(args[0])), 1),
            'sumcube': (lambda args: sum_of_cubes(int(args[0])), 1),
            'prime': (lambda args: is_prime(int(args[0])), 1),
        }
        
        # Process each function
        func_pattern = r'(\w+)\(([^)]*)\)'
        
        def replace_func(match):
            fname = match.group(1).lower()
            args_str = match.group(2)
            
            if fname not in function_map:
                return match.group(0)
            
            func, _ = function_map[fname]
            args = [float(a.strip()) for a in args_str.split(',') if a.strip()]
            result = func(args)
            
            # Create step description
            args_display = ', '.join(str(int(a) if a == int(a) else a) for a in args)
            steps.append(f"{fname}({args_display}) = {result}")
            
            return str(result)
        
        # Keep replacing until no more functions found
        prev_expr = ""
        while prev_expr != expr:
            prev_expr = expr
            expr = re.sub(func_pattern, replace_func, expr, flags=re.IGNORECASE)
        
        # Step 3: Replace constants
        expr = expr.replace('pi', str(math.pi))
        expr = expr.replace('π', str(math.pi))
        expr = expr.replace('e', str(math.e)) if not re.search(r'[a-df-zA-DF-Z]', expr.replace(str(math.e), '')) else expr
        
        # Step 4: Replace power notation
        expr = expr.replace('^', '**')
        
        # Step 5: Evaluate the final expression safely
        # Only allow safe characters
        safe_chars = set('0123456789.+-*/() %')
        clean_expr = expr
        for ch in clean_expr:
            if ch not in safe_chars and ch != '*':
                # Try to evaluate with eval in restricted scope
                break
        
        result = eval(expr, {"__builtins__": {}}, {"math": math})
        
        if isinstance(result, float) and result == int(result) and abs(result) < 1e15:
            result = int(result)
        
        if steps:
            steps.append(f"Final: {original} = {result}")
        
        return result, steps, None
        
    except ZeroDivisionError:
        return None, steps, "⚠️ Division by zero!"
    except ValueError as e:
        return None, steps, f"⚠️ Math error: {str(e)}"
    except Exception as e:
        return None, steps, f"⚠️ Could not parse: {str(e)}"


def get_supported_functions():
    """Return a list of supported functions for help display."""
    return {
        "Arithmetic": ["+ − × ÷ %", "^ (power)", "( ) grouping"],
        "Factorial": ["5! or factorial(5)"],
        "Square Root": ["sqrt(25)"],
        "Trigonometry": ["sin(45), cos(60), tan(30) — degrees"],
        "Logarithm": ["log(100), ln(e), log(8,2)"],
        "GCD / HCF": ["gcd(12, 8) or hcf(12, 8)"],
        "LCM": ["lcm(4, 6)"],
        "Fibonacci": ["fib(10) — 10th Fibonacci number"],
        "Sum of Squares": ["sumsq(5) — 1²+2²+...+5²"],
        "Sum of Cubes": ["sumcube(5) — 1³+2³+...+5³"],
        "Combinations": ["ncr(5, 2)"],
        "Permutations": ["npr(5, 2)"],
        "Constants": ["pi (π), e (Euler's number)"],
    }
