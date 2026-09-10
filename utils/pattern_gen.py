# Pattern Generator Module
# Generates star and number patterns using loops (from Rubicon Training)


def star_right_triangle(n):
    """Right-aligned star triangle (from training codes.ipynb)."""
    lines = []
    for i in range(1, n + 1):
        lines.append("* " * i)
    return "\n".join(lines)


def star_pyramid(n):
    """Centered star pyramid (from training codes.ipynb)."""
    lines = []
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        lines.append(spaces + stars)
    return "\n".join(lines)


def star_inverted_pyramid(n):
    """Inverted centered star pyramid."""
    lines = []
    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        stars = "* " * i
        lines.append(spaces + stars)
    return "\n".join(lines)


def star_diamond(n):
    """Diamond pattern."""
    lines = []
    # Upper half
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        lines.append(spaces + stars)
    # Lower half
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "* " * i
        lines.append(spaces + stars)
    return "\n".join(lines)


def star_hollow_square(n):
    """Hollow square pattern."""
    lines = []
    for i in range(n):
        if i == 0 or i == n - 1:
            lines.append("* " * n)
        else:
            lines.append("* " + "  " * (n - 2) + "* ")
    return "\n".join(lines)


def star_right_triangle_inverted(n):
    """Inverted right triangle."""
    lines = []
    for i in range(n, 0, -1):
        lines.append("* " * i)
    return "\n".join(lines)


def star_left_triangle(n):
    """Left-aligned triangle."""
    lines = []
    for i in range(1, n + 1):
        spaces = "  " * (n - i)
        stars = "* " * i
        lines.append(spaces + stars)
    return "\n".join(lines)


def number_right_triangle(n):
    """Number right triangle."""
    lines = []
    for i in range(1, n + 1):
        row = " ".join(str(j) for j in range(1, i + 1))
        lines.append(row)
    return "\n".join(lines)


def number_pyramid(n):
    """Number pyramid pattern."""
    lines = []
    for i in range(1, n + 1):
        spaces = "  " * (n - i)
        nums = " ".join(str(j) for j in range(1, i + 1))
        lines.append(spaces + nums)
    return "\n".join(lines)


def floyds_triangle(n):
    """Floyd's triangle: consecutive numbers in triangle form."""
    lines = []
    num = 1
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        lines.append(" ".join(f"{x:>3}" for x in row))
    return "\n".join(lines)


def pascals_triangle(n):
    """Pascal's triangle using combinations."""
    from utils.math_functions import nCr
    lines = []
    for i in range(n):
        spaces = "   " * (n - i - 1)
        row = "   ".join(f"{nCr(i, j):>3}" for j in range(i + 1))
        lines.append(spaces + row)
    return "\n".join(lines)


def multiplication_table(n):
    """Generate multiplication table up to n."""
    lines = []
    header = "    " + "  ".join(f"{j:>4}" for j in range(1, n + 1))
    lines.append(header)
    lines.append("─" * len(header))
    for i in range(1, n + 1):
        row = f"{i:>3}│" + "  ".join(f"{i*j:>4}" for j in range(1, n + 1))
        lines.append(row)
    return "\n".join(lines)


def alphabet_triangle(n):
    """Alphabet triangle pattern."""
    lines = []
    for i in range(1, min(n + 1, 27)):
        row = " ".join(chr(64 + j) for j in range(1, i + 1))
        lines.append(row)
    return "\n".join(lines)


def butterfly_pattern(n):
    """Butterfly star pattern."""
    lines = []
    # Upper half
    for i in range(1, n + 1):
        left = "* " * i
        mid = "  " * (2 * (n - i))
        right = "* " * i
        lines.append(left + mid + right)
    # Lower half
    for i in range(n, 0, -1):
        left = "* " * i
        mid = "  " * (2 * (n - i))
        right = "* " * i
        lines.append(left + mid + right)
    return "\n".join(lines)


# Dictionary of all patterns for easy access
PATTERNS = {
    "⭐ Star Right Triangle": star_right_triangle,
    "⭐ Star Pyramid": star_pyramid,
    "⭐ Inverted Pyramid": star_inverted_pyramid,
    "⭐ Diamond": star_diamond,
    "⭐ Hollow Square": star_hollow_square,
    "⭐ Inverted Right Triangle": star_right_triangle_inverted,
    "⭐ Left Triangle": star_left_triangle,
    "⭐ Butterfly": butterfly_pattern,
    "🔢 Number Right Triangle": number_right_triangle,
    "🔢 Number Pyramid": number_pyramid,
    "🔢 Floyd's Triangle": floyds_triangle,
    "🔢 Pascal's Triangle": pascals_triangle,
    "🔢 Multiplication Table": multiplication_table,
    "🔤 Alphabet Triangle": alphabet_triangle,
}
