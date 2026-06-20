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
}
