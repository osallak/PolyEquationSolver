from typing import Dict
from .math_utils import format_fraction

class EquationFormatter:
    @staticmethod
    def format_term(coefficient: float, degree: int) -> str:
        """Format a single term of the equation."""
        if degree == 0:
            return f"{coefficient:g}"
        
        if abs(coefficient) == 1:
            coeff_str = "-" if coefficient < 0 else ""
        else:
            coeff_str = f"{coefficient:g}"
            
        if degree == 1:
            return f"{coeff_str}X"
        return f"{coeff_str}X^{degree}"

    @staticmethod
    def format_reduced_form(coefficients: Dict[int, float]) -> str:
        """Format the reduced form of the equation."""
        if not coefficients:
            return "0 = 0"
            
        terms = []
        for degree in sorted(coefficients.keys(), reverse=True):
            coeff = coefficients[degree]
            if coeff == 0:
                continue
                
            if terms and coeff > 0:
                terms.append("+ ")
            elif terms and coeff < 0:
                terms.append("- ")
            elif coeff < 0:
                terms.append("-")
                
            term = EquationFormatter.format_term(abs(coeff), degree)
            terms.append(term)
            
        return " ".join(terms) + " = 0"

    @staticmethod
    def format_solution(value: float, fraction: tuple[float, float] = None) -> str:
        """Format a solution with both decimal and fractional forms."""
        if fraction:
            num, den = fraction
            # Only show fraction if:
            # 1. Numbers are small enough to be readable
            # 2. It's not already a whole number (den != 1)
            # 3. The fraction is meaningful (not just n/1)
            if abs(num) < 100 and abs(den) < 100 and den != 1 and num % den != 0:
                frac_str = format_fraction(num, den)
                return f"{value:g} (or {frac_str})"
        return f"{value:g}" 