from dataclasses import dataclass
from typing import Optional, Tuple, Union, Dict
import re
import sys
from enum import Enum

from utils.equation_formatter import EquationFormatter

class EquationType(Enum):
    CONSTANT = "constant"
    LINEAR = "linear"
    QUADRATIC = "quadratic"

@dataclass
class Solution:
    values: Optional[Tuple[float, ...]]
    count: int
    equation_type: EquationType
    reduced_form: str
    degree: int
    fractions: Optional[Tuple[Tuple[float, float], ...]] = None
    coefficients: Dict[int, float] = None
    discriminant: Optional[float] = None
    original_form: str = ""

class EquationParser:
    # Similar pattern to the original program
    EQUATION_PATTERN = r"(((^[+-]?)|[+-])(([0-9]+(\.[0-9]+)?(\*X(\^[0-9]+)?)?)|(([0-9]+(\.[0-9]+)?\*)?X(\^[0-9]+)?)))+$"
    
    @staticmethod
    def parse(equation_str: str) -> dict[int, float]:
        # Remove spaces and split by =
        parts = equation_str.replace(" ", "").split("=")
        if len(parts) != 2:
            raise ValueError("Equation must contain exactly one '='")
            
        if not all(re.match(EquationParser.EQUATION_PATTERN, part) for part in parts):
            raise ValueError("Invalid equation format")
            
        # Move everything to left side
        left_side = EquationParser._parse_expression(parts[0])
        right_side = EquationParser._parse_expression(parts[1])
        
        # Combine terms
        for degree, coeff in right_side.items():
            left_side[degree] = left_side.get(degree, 0) - coeff
            
        # Remove zero coefficients
        return {k: round(v, 6) for k, v in left_side.items() if abs(v) > 1e-10}
    
    @staticmethod
    def _parse_expression(expr: str) -> dict[int, float]:
        terms = {}
        if not expr:
            return terms
            
        # Split into terms
        parts = []
        current = ""
        for char in expr:
            if char in "+-" and current:
                parts.append(current)
                current = char
            else:
                current += char
        if current:
            parts.append(current)
            
        # Parse each term
        for term in parts:
            coeff = 1.0
            degree = 0
            
            if "*" in term:
                coeff_str, var_part = term.split("*")
                coeff = float(coeff_str)
            elif "X" not in term:
                coeff = float(term)
            else:
                if term[0] == "-":
                    coeff = -1.0
                    term = term[1:]
                var_part = term
                
            if "X" in term:
                if "^" in term:
                    degree = int(term.split("^")[1])
                else:
                    degree = 1
                    
            terms[degree] = terms.get(degree, 0) + coeff
            
        return terms

class EquationSolver:
    def __init__(self, equation_str: str):
        self.original_equation = equation_str
        self.coefficients = EquationParser.parse(equation_str)
        self.degree = max(self.coefficients.keys()) if self.coefficients else 0

    def solve(self) -> Solution:
        # Add this check before other solution logic
        if all(coeff == 0 for coeff in self.coefficients.values()):
            solution = Solution(
                values=None,
                count=float('inf'),  # Indicate infinite solutions
                equation_type=EquationType.CONSTANT,
                reduced_form="0 = 0",
                degree=0,
                original_form=self.original_equation,
                coefficients=self.coefficients,
                fractions=None
            )
            return solution
        
        # Create solution with initial values
        solution = Solution(
            values=[],
            count=0,
            equation_type=None,
            reduced_form=EquationFormatter.format_reduced_form(self.coefficients),
            degree=self.degree
        )
        
        # Add additional information
        solution.original_form = self.original_equation
        solution.coefficients = self.coefficients

        # Determine equation type and solve
        if self.degree > 2:
            raise ValueError("Cannot solve equations of degree > 2")
        elif self.degree == 2:
            solution.equation_type = EquationType.QUADRATIC
            self._solve_quadratic(solution)
        elif self.degree == 1:
            solution.equation_type = EquationType.LINEAR
            self._solve_linear(solution)
        else:
            solution.equation_type = EquationType.CONSTANT
            self._solve_constant(solution)

        return solution  # Make sure to return the solution!

    def _solve_quadratic(self, solution: Solution):
        a = solution.coefficients.get(2, 0)
        b = solution.coefficients.get(1, 0)
        c = solution.coefficients.get(0, 0)
        
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            solution.values = None
            solution.count = 0
            solution.discriminant = discriminant
        elif discriminant == 0:
            x = -b / (2*a)
            solution.values = (round(x, 6),)
            solution.count = 1
            solution.fractions = ((-b, 2*a),)
            solution.discriminant = discriminant
        else:
            sqrt_discriminant = discriminant**0.5
            x1 = (-b - sqrt_discriminant) / (2*a)
            x2 = (-b + sqrt_discriminant) / (2*a)
            solution.values = (round(x1, 6), round(x2, 6))
            solution.count = 2
            solution.fractions = ((-b - sqrt_discriminant, 2*a), (-b + sqrt_discriminant, 2*a))
            solution.discriminant = discriminant

    def _solve_linear(self, solution: Solution):
        a = solution.coefficients.get(1, 0)
        b = solution.coefficients.get(0, 0)
        x = -b / a
        solution.values = (round(x, 6),)
        solution.count = 1
        solution.fractions = ((-b, a),)

    def _solve_constant(self, solution: Solution):
        """
        Solve constant equations (equations with no variables).
        Example: 5 = 0 or 0 = 0
        """
        constant_term = solution.coefficients.get(0, 0)
        
        if constant_term == 0:
            # Case: 0 = 0
            solution.count = float('inf')
            solution.values = None  # All real numbers are solutions
        else:
            # Case: c = 0 (where c ≠ 0)
            solution.count = 0
            solution.values = None  # No solutions
