# Computor-v1

## Overview
Computor-v1 is a sophisticated command-line equation solver implemented in Python. It's designed to solve polynomial equations up to the second degree, providing both decimal and fractional solutions when applicable.

## Features

### Equation Solving Capabilities
- **Constant Equations**: Handles equations with no variables
- **Linear Equations**: Solves equations in the form `ax + b = 0`
- **Quadratic Equations**: Solves equations in the form `ax² + bx + c = 0`

### Advanced Output
- Displays reduced form of equations
- Shows polynomial degree
- Provides solutions in both decimal and fractional form (when applicable)
- Calculates and displays discriminant for quadratic equations
- Color-coded output for better readability

### Input Flexibility
- Accepts various equation formats
- Handles coefficients with decimal points
- Supports both positive and negative numbers
- Processes equations with or without spaces

## Installation

### Prerequisites
- Python 3.x

### Setup
1. Clone the repository:

```bash
git clone https://github.com/4yuub/computor-v1.git
```

2. Navigate to the project directory:

```bash
cd computor-v1
```

## Usage

Run the program with an equation as a command-line argument:

```bash
python3 computor.py "equation"
```

### Example Usage:

1. Linear Equation:

```bash
python3 computor.py "2 * X + 1 = 0"
```

2. Quadratic Equation:

```bash
python3 computor.py "2 * X^2 - 4 * X + 2 = 0"
```

## Output Format

The program provides a structured output including:
- Input equation in its original form
- Reduced form of the equation
- Polynomial degree
- For quadratic equations:
  - Coefficients (a, b, c)
  - Discriminant
- Solution(s) in both decimal and fractional form (when applicable)

## Error Handling

The program includes robust error handling for:
- Invalid equation formats
- Equations of degree higher than 2
- Malformed input
- Division by zero
- Other mathematical errors

## Technical Details

The project is structured into several components:
- `EquationSolver`: Main solving logic
- `EquationParser`: Handles equation parsing and validation
- `OutputFormatter`: Manages formatted console output
- `EquationFormatter`: Handles equation string formatting
- `MathUtils`: Contains mathematical utility functions

## Limitations

- Only handles polynomial equations up to degree 2
- Does not solve complex number solutions
- Requires equations to be in a standard format
