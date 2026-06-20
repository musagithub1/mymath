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

# Average of a list
print(mymath.average([10, 20, 30]))  # 20.0
```

## Available Functions

| Function | Description | Example |
|---|---|---|
| `add(a, b)` | Add two numbers | `mymath.add(5, 3)` → `8.0` |
| `multiply(a, b)` | Multiply two numbers | `mymath.multiply(4, 2)` → `8.0` |
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
