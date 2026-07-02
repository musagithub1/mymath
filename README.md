# mymath

A simple Python math library written in C++ using [pybind11](https://github.com/pybind/pybind11). Functions run as fast compiled C++ code, but you use them like normal Python.

## Installation

```bash
pip install git+https://github.com/musagithub1/mymath.git
```

> **Note:** You need a C++ compiler installed on your system.
> - **Linux:** `sudo apt install build-essential`
> - **macOS:** `xcode-select --install`
> - **Windows:** Install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

## Usage

```python
import mymath

# Add two numbers
print(mymath.add(5, 3))            # 8.0

# Multiply two numbers
print(mymath.multiply(4, 2))       # 8.0

# Subtract two numbers
print(mymath.subtract(10, 3))      # 7.0

# Divide two numbers
print(mymath.divide(10, 2))        # 5.0

# Raise to a power
print(mymath.power(2, 10))         # 1024.0

# Square root
print(mymath.square_root(16))      # 4.0

# Factorial
print(mymath.factorial(5))         # 120.0

# Greatest common divisor
print(mymath.gcd(54, 24))          # 6

# Least common multiple
print(mymath.lcm(12, 18))          # 36

# Prime check
print(mymath.is_prime(17))         # True

# Logarithm
print(mymath.logarithm(100, 10))   # 2.0

# Variance of a list
print(mymath.variance([2, 4, 4, 4, 5, 5, 7, 9]))  # 4.0

# Standard deviation of a list
print(mymath.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]))  # 2.0

# Fibonacci number
print(mymath.fibonacci(10))        # 55

# Sine
print(mymath.sine(1.570796))       # ~1.0

# Cosine
print(mymath.cosine(3.141592))     # ~-1.0

# Tangent
print(mymath.tangent(0.785398))     # ~1.0

# Hyperbolic Sine
print(mymath.sinh(0.0))            # 0.0

# Hyperbolic Cosine
print(mymath.cosh(0.0))            # 1.0

# Hyperbolic Tangent
print(mymath.tanh(0.0))            # 0.0

# Hypotenuse
print(mymath.hypot(3.0, 4.0))      # 5.0

# Percentage
print(mymath.percentage(20.0, 50.0))  # 40.0

# Average of a list
print(mymath.average([10, 20, 30]))  # 20.0
```

## Available Functions

| Function | Description | Example |
|---|---|---|
| `add(a, b)` | Add two numbers | `mymath.add(5, 3)` → `8.0` |
| `subtract(a, b)` | Subtract two numbers | `mymath.subtract(10, 3)` → `7.0` |
| `multiply(a, b)` | Multiply two numbers | `mymath.multiply(4, 2)` → `8.0` |
| `divide(a, b)` | Divide two numbers | `mymath.divide(10, 2)` → `5.0` |
| `power(base, exponent)` | Raise base to exponent | `mymath.power(2, 10)` → `1024.0` |
| `square_root(x)` | Square root of a non-negative number | `mymath.square_root(16)` → `4.0` |
| `factorial(n)` | Factorial of a non-negative integer | `mymath.factorial(5)` → `120.0` |
| `gcd(a, b)` | Greatest common divisor of two integers | `mymath.gcd(54, 24)` → `6` |
| `lcm(a, b)` | Least common multiple of two integers | `mymath.lcm(12, 18)` → `36` |
| `is_prime(n)` | Check if an integer is a prime number | `mymath.is_prime(17)` → `True` |
| `logarithm(x, base)` | Logarithm of x with respect to base | `mymath.logarithm(100, 10)` → `2.0` |
| `variance(numbers)` | Population variance of a list of numbers | `mymath.variance([2, 4, 4, 4, 5, 5, 7, 9])` → `4.0` |
| `standard_deviation(numbers)` | Population standard deviation of a list | `mymath.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])` → `2.0` |
| `fibonacci(n)` | Compute the n-th Fibonacci number | `mymath.fibonacci(10)` → `55` |
| `sine(x)` | Compute the sine of an angle in radians | `mymath.sine(1.570796)` → `1.0` |
| `cosine(x)` | Compute the cosine of an angle in radians | `mymath.cosine(3.141592)` → `-1.0` |
| `tangent(x)` | Compute the tangent of an angle in radians | `mymath.tangent(0.785398)` → `1.0` |
| `sinh(x)` | Compute the hyperbolic sine of a number | `mymath.sinh(0.0)` → `0.0` |
| `cosh(x)` | Compute the hyperbolic cosine of a number | `mymath.cosh(0.0)` → `1.0` |
| `tanh(x)` | Compute the hyperbolic tangent of a number | `mymath.tanh(0.0)` → `0.0` |
| `hypot(x, y)` | Compute the hypotenuse of a right-angled triangle | `mymath.hypot(3.0, 4.0)` → `5.0` |
| `percentage(part, total)` | Compute the percentage of a part relative to a total | `mymath.percentage(20.0, 50.0)` → `40.0` |
| `average(numbers)` | Mean of a list of numbers | `mymath.average([10, 20, 30])` → `20.0` |

## How It Works

This library uses **pybind11** to bridge C++ and Python:

1. Math functions are written in C++ (`src/mymath.cpp`)
2. pybind11 wraps them into a Python module
3. `pip install` compiles the C++ and installs the module
4. You `import mymath` like any normal Python package

## Project Structure

```
mymath/
├── src/
│   └── mymath.cpp        # C++ source code
├── setup.py               # Build configuration
├── pyproject.toml          # Build dependencies
├── test_mymath.py          # Test script
├── LICENSE                 # MIT License
└── README.md               # This file
```

## Development

```bash
# Clone the repo
git clone https://github.com/musagithub1/mymath.git
cd mymath

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode
pip install .

# Run tests
python test_mymath.py
```

## License

MIT License — see [LICENSE](LICENSE) for details.

## Author

**Mussa Khan** — [GitHub](https://github.com/musagithub1)
