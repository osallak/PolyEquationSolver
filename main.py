#!/usr/bin/env python3
import sys
from equation_solver import EquationSolver, EquationType
from utils.equation_formatter import EquationFormatter
from utils.math_utils import format_fraction
from utils.output_formatter import OutputFormatter

def print_equation_info(solution):
    OutputFormatter.header("Equation Analysis")
    
    if hasattr(solution, 'original_form'):
        OutputFormatter.section("Input Equation", solution.original_form)
    
    OutputFormatter.section("Reduced Form", solution.reduced_form)
    OutputFormatter.section("Polynomial Degree", str(solution.degree))
    
    if solution.equation_type == EquationType.QUADRATIC:
        print()  # Add spacing
        coeffs = solution.coefficients
        OutputFormatter.section("Quadratic Form", "ax² + bx + c = 0")
        OutputFormatter.info("a", f"{coeffs.get(2, 0):g}")
        OutputFormatter.info("b", f"{coeffs.get(1, 0):g}")
        OutputFormatter.info("c", f"{coeffs.get(0, 0):g}")
        
        if hasattr(solution, 'discriminant'):
            OutputFormatter.section("Discriminant", f"{solution.discriminant:g}")

def print_solutions(solution):
    OutputFormatter.header("Solution(s)")
    
    if solution.count == float('inf'):
        OutputFormatter.solution("All real numbers are solutions")
    elif solution.count == 0:
        OutputFormatter.solution("The equation has no real solutions")
    elif solution.count == 1:
        decimal = f"{solution.values[0]:.6f}".rstrip('0').rstrip('.')
        if solution.fractions and solution.fractions[0]:
            fraction = format_fraction(*solution.fractions[0])
            if fraction != decimal:  # Only show fraction if different from decimal
                OutputFormatter.solution(f"x = {decimal} (or {fraction})")
            else:
                OutputFormatter.solution(f"x = {decimal}")
        else:
            OutputFormatter.solution(f"x = {decimal}")
    else:
        for i, (value, fraction) in enumerate(zip(solution.values, solution.fractions), 1):
            decimal = f"{value:.6f}".rstrip('0').rstrip('.')
            if fraction:
                fraction_str = format_fraction(*fraction)
                if fraction_str != decimal:  # Only show fraction if different from decimal
                    OutputFormatter.solution(f"x{i} = {decimal} (or {fraction_str})")
                else:
                    OutputFormatter.solution(f"x{i} = {decimal}")
            else:
                OutputFormatter.solution(f"x{i} = {decimal}")

def main():
    if len(sys.argv) != 2:
        OutputFormatter.error("Usage: python3 computor.py \"equation\"")
        sys.exit(1)

    try:
        equation = sys.argv[1]
        solver = EquationSolver(equation)
        solution = solver.solve()
        
        print_equation_info(solution)
        print_solutions(solution)
        
    except ValueError as e:
        OutputFormatter.error(str(e))
        sys.exit(1)
    except Exception as e:
        OutputFormatter.error(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 