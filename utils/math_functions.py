# Core math functions using recursion, lambda, and standard algorithms
# These demonstrate Python concepts from Rubicon Training

import math
from functools import reduce

# ============================================================
# RECURSIVE FUNCTIONS (from Rubicon Training - Session codes.ipynb)
# ============================================================

def factorial(n):
    """Calculate factorial using recursion (from training)."""
    if n < 0:
        return "Undefined (negative number)"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Generate Fibonacci sequence up to n terms using recursion."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seq = fibonacci(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq


def fibonacci_nth(n):
    """Get the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)


def gcd(a, b):
    """Calculate GCD (HCF) using Euclidean algorithm (recursion)."""
    a, b = abs(int(a)), abs(int(b))
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    """Calculate LCM using GCD."""
    a, b = abs(int(a)), abs(int(b))
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def power(base, exp):
    """Calculate power using recursion."""
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)


# ============================================================
# LAMBDA FUNCTIONS (from Rubicon Training - lambda, filter, map)
# ============================================================

# Quick arithmetic operations using lambda
add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Undefined (division by zero)"
modulo = lambda a, b: a % b if b != 0 else "Undefined"

# Filter operations using lambda (from training)
get_even_numbers = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
get_odd_numbers = lambda lst: list(filter(lambda x: x % 2 != 0, lst))
get_primes_from_list = lambda lst: list(filter(lambda x: is_prime(x), lst))

# Map operations using lambda (from training)
square_all = lambda lst: list(map(lambda x: x ** 2, lst))
cube_all = lambda lst: list(map(lambda x: x ** 3, lst))
double_all = lambda lst: list(map(lambda x: x * 2, lst))


# ============================================================
# NUMBER THEORY FUNCTIONS
# ============================================================

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    """Find all prime factors of a number."""
    n = abs(int(n))
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def all_factors(n):
    """Find all factors/divisors of a number."""
    n = abs(int(n))
    if n == 0:
        return []
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)


def sum_of_squares(n):
    """Calculate 1² + 2² + 3² + ... + n²."""
    n = abs(int(n))
    return sum(map(lambda x: x ** 2, range(1, n + 1)))


def sum_of_cubes(n):
    """Calculate 1³ + 2³ + 3³ + ... + n³."""
    n = abs(int(n))
    return sum(map(lambda x: x ** 3, range(1, n + 1)))


def sum_of_n(n):
    """Calculate 1 + 2 + 3 + ... + n."""
    n = abs(int(n))
    return n * (n + 1) // 2


def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    n = abs(int(n))
    digits = str(n)
    num_digits = len(digits)
    total = sum(int(d) ** num_digits for d in digits)
    return total == n


def is_palindrome(n):
    """Check if a number is a palindrome."""
    s = str(abs(int(n)))
    return s == s[::-1]


def is_perfect(n):
    """Check if a number is a perfect number."""
    n = abs(int(n))
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


def digit_sum(n):
    """Calculate the sum of digits recursively."""
    n = abs(int(n))
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)


def reverse_number(n):
    """Reverse a number."""
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(int(n)))[::-1])


def number_to_words(n):
    """Convert a number to words (for small numbers)."""
    if n < 0:
        return "Negative " + number_to_words(-n)
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    if n == 0:
        return "Zero"
    if n < 20:
        return ones[n]
    if n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")
    if n < 1000:
        return ones[n // 100] + " Hundred" + (" and " + number_to_words(n % 100) if n % 100 != 0 else "")
    if n < 1000000:
        return number_to_words(n // 1000) + " Thousand" + (", " + number_to_words(n % 1000) if n % 1000 != 0 else "")
    return str(n)


def generate_primes(limit):
    """Generate all primes up to a limit using Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]


# ============================================================
# SCIENTIFIC FUNCTIONS
# ============================================================

def deg_to_rad(deg):
    return math.radians(deg)

def rad_to_deg(rad):
    return math.degrees(rad)

def sin_deg(x):
    return math.sin(math.radians(x))

def cos_deg(x):
    return math.cos(math.radians(x))

def tan_deg(x):
    return math.tan(math.radians(x))

def log_base(x, base=10):
    if x <= 0:
        return "Undefined (x must be > 0)"
    return math.log(x, base)

def ln(x):
    if x <= 0:
        return "Undefined (x must be > 0)"
    return math.log(x)

def nCr(n, r):
    """Combinations: n! / (r! * (n-r)!)"""
    if r > n or r < 0:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    """Permutations: n! / (n-r)!"""
    if r > n or r < 0:
        return 0
    return factorial(n) // factorial(n - r)
