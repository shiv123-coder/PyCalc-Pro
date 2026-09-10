# Matrix Operations Module
# Uses NumPy for matrix math – demonstrates function usage from training

import numpy as np


def create_matrix(rows, cols, values=None):
    """Create a matrix from a flat list of values or zeros."""
    if values:
        return np.array(values).reshape(rows, cols)
    return np.zeros((rows, cols))


def matrix_add(a, b):
    """Add two matrices."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    if a.shape != b.shape:
        return None, "Matrices must have the same dimensions for addition."
    return (a + b).tolist(), None


def matrix_subtract(a, b):
    """Subtract matrix B from matrix A."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    if a.shape != b.shape:
        return None, "Matrices must have the same dimensions for subtraction."
    return (a - b).tolist(), None


def matrix_multiply(a, b):
    """Multiply two matrices."""
    a, b = np.array(a, dtype=float), np.array(b, dtype=float)
    if a.shape[1] != b.shape[0]:
        return None, f"Cannot multiply: A columns ({a.shape[1]}) ≠ B rows ({b.shape[0]})."
    return np.matmul(a, b).tolist(), None


def matrix_scalar_multiply(a, scalar):
    """Multiply a matrix by a scalar."""
    a = np.array(a, dtype=float)
    return (a * scalar).tolist(), None


def matrix_transpose(a):
    """Transpose a matrix."""
    a = np.array(a, dtype=float)
    return a.T.tolist(), None


def matrix_determinant(a):
    """Calculate the determinant of a square matrix."""
    a = np.array(a, dtype=float)
    if a.shape[0] != a.shape[1]:
        return None, "Determinant is only defined for square matrices."
    det = np.linalg.det(a)
    return round(det, 6), None


def matrix_inverse(a):
    """Calculate the inverse of a square matrix."""
    a = np.array(a, dtype=float)
    if a.shape[0] != a.shape[1]:
        return None, "Inverse is only defined for square matrices."
    det = np.linalg.det(a)
    if abs(det) < 1e-10:
        return None, "Matrix is singular (determinant ≈ 0). No inverse exists."
    inv = np.linalg.inv(a)
    return np.round(inv, 6).tolist(), None


def matrix_trace(a):
    """Calculate the trace (sum of diagonal elements)."""
    a = np.array(a, dtype=float)
    if a.shape[0] != a.shape[1]:
        return None, "Trace is only defined for square matrices."
    return float(np.trace(a)), None


def matrix_rank(a):
    """Calculate the rank of a matrix."""
    a = np.array(a, dtype=float)
    return int(np.linalg.matrix_rank(a)), None


def matrix_eigenvalues(a):
    """Calculate eigenvalues of a square matrix."""
    a = np.array(a, dtype=float)
    if a.shape[0] != a.shape[1]:
        return None, "Eigenvalues are only defined for square matrices."
    eigenvalues = np.linalg.eigvals(a)
    return np.round(eigenvalues, 6).tolist(), None


def matrix_power(a, n):
    """Raise a square matrix to the power n."""
    a = np.array(a, dtype=float)
    if a.shape[0] != a.shape[1]:
        return None, "Matrix power is only defined for square matrices."
    result = np.linalg.matrix_power(a, int(n))
    return result.tolist(), None


def format_matrix(matrix):
    """Format a matrix for display."""
    if matrix is None:
        return "N/A"
    arr = np.array(matrix)
    rows = []
    for row in arr:
        formatted = [f"{val:g}" for val in row]
        rows.append("  ".join(f"{v:>8}" for v in formatted))
    return "\n".join(rows)
