/*
 * mymath.cpp
 * ----------
 * This is the C++ source file that contains the actual math functions.
 * These functions run as compiled C++ code (fast!), but Python users
 * can call them thanks to pybind11.
 *
 * pybind11 acts as a bridge: it takes our C++ functions and makes them
 * available as a normal Python module.
 */

#include <pybind11/pybind11.h>  // Core pybind11 header
#include <pybind11/stl.h>       // Lets us use std::vector <-> Python list conversion
#include <vector>               // C++ dynamic array (similar to Python list)
#include <numeric>              // For std::accumulate (to sum numbers)
#include <stdexcept>            // For std::runtime_error (to raise errors)
#include <cmath>                // For std::pow (exponentiation)

// ============================================================
// Function 1: add
// Takes two numbers and returns their sum.
// ============================================================
double add(double a, double b) {
    return a + b;
}

// ============================================================
// Function 2: multiply
// Takes two numbers and returns their product.
// ============================================================
double multiply(double a, double b) {
    return a * b;
}

// ============================================================
// Function 3: average
// Takes a list of numbers and returns the average (mean).
// In C++, a Python list of numbers becomes a std::vector<double>.
// pybind11 handles this conversion automatically for us.
// ============================================================
double average(const std::vector<double>& numbers) {
    if (numbers.empty()) {
        throw std::runtime_error("Cannot compute average of an empty list");
    }
    double sum = std::accumulate(numbers.begin(), numbers.end(), 0.0);
    return sum / static_cast<double>(numbers.size());
}

// ============================================================
// Function 4: subtract
// Takes two numbers and returns their difference.
// ============================================================
double subtract(double a, double b) {
    return a - b;
}

// ============================================================
// Function 5: power
// Raises base to the given exponent using std::pow.
// ============================================================
double power(double base, double exponent) {
    return std::pow(base, exponent);
}

// ============================================================
// Function 6: factorial
// Computes the factorial of a non-negative integer.
// Returns a double to handle large results (up to ~170!).
// Throws an error for negative inputs.
// ============================================================
double factorial(int n) {
    if (n < 0) {
        throw std::runtime_error("Cannot compute factorial of a negative number");
    }
    double result = 1.0;
    for (int i = 2; i <= n; ++i) {
        result *= i;
    }
    return result;
}

// ============================================================
// Function 7: divide
// Divides a by b. Throws an error if b is zero.
// ============================================================
double divide(double a, double b) {
    if (b == 0.0) {
        throw std::runtime_error("Division by zero is not allowed");
    }
    return a / b;
}

// ============================================================
// Function 8: square_root
// Computes the square root of a non-negative number.
// Throws an error for negative inputs.
// ============================================================
double square_root(double x) {
    if (x < 0.0) {
        throw std::runtime_error("Cannot compute square root of a negative number");
    }
    return std::sqrt(x);
}

// ============================================================
// Function 9: gcd
// Computes the greatest common divisor of two integers.
// ============================================================
int gcd(int a, int b) {
    a = std::abs(a);
    b = std::abs(b);
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// ============================================================
// Function 10: lcm
// Computes the least common multiple of two integers.
// ============================================================
int lcm(int a, int b) {
    if (a == 0 || b == 0) {
        return 0;
    }
    a = std::abs(a);
    b = std::abs(b);
    int g = gcd(a, b);
    return (a / g) * b;
}

// ============================================================
// Function 11: is_prime
// Checks if an integer is a prime number.
// ============================================================
bool is_prime(int n) {
    if (n <= 1) {
        return false;
    }
    if (n <= 3) {
        return true;
    }
    if (n % 2 == 0 || n % 3 == 0) {
        return false;
    }
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

// ============================================================
// Function 12: logarithm
// Computes the logarithm of x with respect to base.
// Throws an error for non-positive values of x or invalid bases.
// ============================================================
double logarithm(double x, double base) {
    if (x <= 0.0) {
        throw std::runtime_error("Logarithm argument must be positive");
    }
    if (base <= 0.0 || base == 1.0) {
        throw std::runtime_error("Logarithm base must be positive and not equal to 1");
    }
    return std::log(x) / std::log(base);
}

// ============================================================
// PYBIND11_MODULE: This is the magic part!
// It tells pybind11 to create a Python module called "mymath"
// and register our C++ functions so Python can use them.
//
// "m" is the module object — we attach functions to it.
// ============================================================
PYBIND11_MODULE(mymath, m) {
    // A short description shown when you do: help(mymath)
    m.doc() = "A simple math library written in C++ with pybind11";

    // Register each function with:
    //   - its Python name (string)
    //   - a pointer to the C++ function
    //   - a docstring (shown in help())
    //   - named arguments (so users can write add(a=5, b=3))

    m.def("add", &add,
          "Add two numbers and return the result.",
          pybind11::arg("a"), pybind11::arg("b"));

    m.def("multiply", &multiply,
          "Multiply two numbers and return the result.",
          pybind11::arg("a"), pybind11::arg("b"));

    m.def("average", &average,
          "Compute the average (mean) of a list of numbers.",
          pybind11::arg("numbers"));

    m.def("subtract", &subtract,
          "Subtract b from a and return the result.",
          pybind11::arg("a"), pybind11::arg("b"));

    m.def("power", &power,
          "Raise base to the given exponent and return the result.",
          pybind11::arg("base"), pybind11::arg("exponent"));

    m.def("factorial", &factorial,
          "Compute the factorial of a non-negative integer.",
          pybind11::arg("n"));

    m.def("divide", &divide,
          "Divide a by b and return the result. Throws an error if b is zero.",
          pybind11::arg("a"), pybind11::arg("b"));

    m.def("square_root", &square_root,
          "Compute the square root of a non-negative number.",
          pybind11::arg("x"));

    m.def("gcd", &gcd,
          "Compute the greatest common divisor of two integers.",
          pybind11::arg("a"), pybind11::arg("b"));

    m.def("lcm", &lcm,
          "Compute the least common multiple of two integers.",
          pybind11::arg("a"), pybind11::arg("b"));

    m.def("is_prime", &is_prime,
          "Check if an integer is a prime number.",
          pybind11::arg("n"));

    m.def("logarithm", &logarithm,
          "Compute the logarithm of x with respect to base.",
          pybind11::arg("x"), pybind11::arg("base"));
}
