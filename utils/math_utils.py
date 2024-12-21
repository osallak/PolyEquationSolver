def gcd(a: float, b: float) -> float:
    """Calculate Greatest Common Divisor using Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator: float, denominator: float) -> tuple[float, float]:
    """Simplify a fraction to its lowest terms."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
        
    divisor = gcd(numerator, denominator)
    return numerator/divisor, denominator/divisor

def sqrt(n: float, precision: float = 1e-10) -> float:
    """Calculate square root using Newton's method."""
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    if n == 0:
        return 0
        
    x = n
    while True:
        root = 0.5 * (x + n/x)
        if abs(root - x) < precision:
            return root
        x = root

def format_fraction(numerator: float, denominator: float) -> str:
    """Format a fraction as a string with proper signs."""
    num, den = simplify_fraction(numerator, denominator)
    if den == 1:
        return f"{int(num)}"
    elif den < 0:
        return f"{int(-num)}/{int(-den)}"
    else:
        return f"{int(num)}/{int(den)}" 