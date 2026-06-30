"""
test_mymath.py
--------------
A simple test script to verify that our C++ library works from Python.

Run this AFTER you have installed the library with:
    pip install .

Then run:
    python test_mymath.py
"""

import mymath

# ============================================================
# Test 1: add
# ============================================================
result = mymath.add(5, 3)
print(f"add(5, 3) = {result}")        # Expected: 8.0
assert result == 8.0, f"Expected 8.0, got {result}"

# ============================================================
# Test 2: multiply
# ============================================================
result = mymath.multiply(4, 2)
print(f"multiply(4, 2) = {result}")    # Expected: 8.0
assert result == 8.0, f"Expected 8.0, got {result}"

# ============================================================
# Test 3: average
# ============================================================
result = mymath.average([10, 20, 30])
print(f"average([10, 20, 30]) = {result}")  # Expected: 20.0
assert result == 20.0, f"Expected 20.0, got {result}"

# ============================================================
# Test 4: add with floats
# ============================================================
result = mymath.add(1.5, 2.5)
print(f"add(1.5, 2.5) = {result}")     # Expected: 4.0
assert result == 4.0, f"Expected 4.0, got {result}"

# ============================================================
# Test 5: average with a single element
# ============================================================
result = mymath.average([42])
print(f"average([42]) = {result}")      # Expected: 42.0
assert result == 42.0, f"Expected 42.0, got {result}"

# ============================================================
# Test 6: average with empty list should raise an error
# ============================================================
try:
    mymath.average([])
    print("ERROR: average([]) should have raised an exception!")
except RuntimeError as e:
    print(f"average([]) correctly raised: {e}")

# ============================================================
# Test 7: subtract
# ============================================================
result = mymath.subtract(10, 3)
print(f"subtract(10, 3) = {result}")     # Expected: 7.0
assert result == 7.0, f"Expected 7.0, got {result}"

# ============================================================
# Test 8: subtract with negative result
# ============================================================
result = mymath.subtract(3, 10)
print(f"subtract(3, 10) = {result}")     # Expected: -7.0
assert result == -7.0, f"Expected -7.0, got {result}"

# ============================================================
# Test 9: power
# ============================================================
result = mymath.power(2, 10)
print(f"power(2, 10) = {result}")        # Expected: 1024.0
assert result == 1024.0, f"Expected 1024.0, got {result}"

# ============================================================
# Test 10: power with fractional exponent
# ============================================================
result = mymath.power(9, 0.5)
print(f"power(9, 0.5) = {result}")       # Expected: 3.0
assert result == 3.0, f"Expected 3.0, got {result}"

# ============================================================
# Test 11: factorial
# ============================================================
result = mymath.factorial(5)
print(f"factorial(5) = {result}")        # Expected: 120.0
assert result == 120.0, f"Expected 120.0, got {result}"

# ============================================================
# Test 12: factorial of 0
# ============================================================
result = mymath.factorial(0)
print(f"factorial(0) = {result}")        # Expected: 1.0
assert result == 1.0, f"Expected 1.0, got {result}"

# ============================================================
# Test 13: factorial of negative should raise an error
# ============================================================
try:
    mymath.factorial(-1)
    print("ERROR: factorial(-1) should have raised an exception!")
except RuntimeError as e:
    print(f"factorial(-1) correctly raised: {e}")

# ============================================================
# Test 14: divide
# ============================================================
result = mymath.divide(10, 2)
print(f"divide(10, 2) = {result}")        # Expected: 5.0
assert result == 5.0, f"Expected 5.0, got {result}"

# ============================================================
# Test 15: divide by zero should raise an error
# ============================================================
try:
    mymath.divide(5, 0)
    print("ERROR: divide(5, 0) should have raised an exception!")
except RuntimeError as e:
    print(f"divide(5, 0) correctly raised: {e}")

# ============================================================
# Test 16: square_root
# ============================================================
result = mymath.square_root(16)
print(f"square_root(16) = {result}")      # Expected: 4.0
assert result == 4.0, f"Expected 4.0, got {result}"

# ============================================================
# Test 17: square_root of negative should raise an error
# ============================================================
try:
    mymath.square_root(-4)
    print("ERROR: square_root(-4) should have raised an exception!")
except RuntimeError as e:
    print(f"square_root(-4) correctly raised: {e}")

# ============================================================
# Test 18: gcd
# ============================================================
result = mymath.gcd(54, 24)
print(f"gcd(54, 24) = {result}")          # Expected: 6
assert result == 6, f"Expected 6, got {result}"

# ============================================================
# Test 19: gcd with negative numbers
# ============================================================
result = mymath.gcd(-48, 18)
print(f"gcd(-48, 18) = {result}")         # Expected: 6
assert result == 6, f"Expected 6, got {result}"

# ============================================================
# Test 20: gcd with zero
# ============================================================
result = mymath.gcd(0, 5)
print(f"gcd(0, 5) = {result}")            # Expected: 5
assert result == 5, f"Expected 5, got {result}"

# ============================================================
# Test 21: lcm
# ============================================================
result = mymath.lcm(12, 18)
print(f"lcm(12, 18) = {result}")          # Expected: 36
assert result == 36, f"Expected 36, got {result}"

# ============================================================
# Test 22: lcm with zero
# ============================================================
result = mymath.lcm(0, 5)
print(f"lcm(0, 5) = {result}")            # Expected: 0
assert result == 0, f"Expected 0, got {result}"

# ============================================================
# Test 23: is_prime
# ============================================================
assert mymath.is_prime(2) == True, "Expected 2 to be prime"
assert mymath.is_prime(17) == True, "Expected 17 to be prime"
assert mymath.is_prime(4) == False, "Expected 4 not to be prime"
assert mymath.is_prime(1) == False, "Expected 1 not to be prime"
assert mymath.is_prime(-7) == False, "Expected -7 not to be prime"
print("is_prime tests passed!")

# ============================================================
# Test 24: logarithm
# ============================================================
result = mymath.logarithm(100, 10)
print(f"logarithm(100, 10) = {result}")    # Expected: 2.0
assert abs(result - 2.0) < 1e-9, f"Expected 2.0, got {result}"

# ============================================================
# Test 25: logarithm with natural base
# ============================================================
import math
result = mymath.logarithm(math.e, math.e)
print(f"logarithm(e, e) = {result}")      # Expected: 1.0
assert abs(result - 1.0) < 1e-9, f"Expected 1.0, got {result}"

# ============================================================
# Test 26: logarithm with negative argument should raise error
# ============================================================
try:
    mymath.logarithm(-10, 10)
    print("ERROR: logarithm(-10, 10) should have raised an exception!")
except RuntimeError as e:
    print(f"logarithm(-10, 10) correctly raised: {e}")

# ============================================================
# Test 27: logarithm with invalid base should raise error
# ============================================================
try:
    mymath.logarithm(10, 1)
    print("ERROR: logarithm(10, 1) should have raised an exception!")
except RuntimeError as e:
    print(f"logarithm(10, 1) correctly raised: {e}")

# ============================================================
# Test 28: variance
# ============================================================
result = mymath.variance([2, 4, 4, 4, 5, 5, 7, 9])
print(f"variance([2, 4, 4, 4, 5, 5, 7, 9]) = {result}")  # Expected: 4.0 (mean = 5, variance = 32 / 8 = 4.0)
assert abs(result - 4.0) < 1e-9, f"Expected 4.0, got {result}"

# ============================================================
# Test 29: variance empty list error
# ============================================================
try:
    mymath.variance([])
    print("ERROR: variance([]) should have raised an exception!")
except RuntimeError as e:
    print(f"variance([]) correctly raised: {e}")

# ============================================================
# Test 30: standard_deviation
# ============================================================
result = mymath.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])
print(f"standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]) = {result}")  # Expected: 2.0
assert abs(result - 2.0) < 1e-9, f"Expected 2.0, got {result}"

# ============================================================
# Test 31: standard_deviation empty list error
# ============================================================
try:
    mymath.standard_deviation([])
    print("ERROR: standard_deviation([]) should have raised an exception!")
except RuntimeError as e:
    print(f"standard_deviation([]) correctly raised: {e}")

# ============================================================
# Test 32: fibonacci
# ============================================================
assert mymath.fibonacci(0) == 0, f"Expected 0, got {mymath.fibonacci(0)}"
assert mymath.fibonacci(1) == 1, f"Expected 1, got {mymath.fibonacci(1)}"
assert mymath.fibonacci(10) == 55, f"Expected 55, got {mymath.fibonacci(10)}"
print("fibonacci basic tests passed!")

# ============================================================
# Test 33: fibonacci negative index error
# ============================================================
try:
    mymath.fibonacci(-5)
    print("ERROR: fibonacci(-5) should have raised an exception!")
except RuntimeError as e:
    print(f"fibonacci(-5) correctly raised: {e}")

# ============================================================
# Test 34: sine
# ============================================================
import math
result = mymath.sine(math.pi / 2)
print(f"sine(pi/2) = {result}")          # Expected: 1.0
assert abs(result - 1.0) < 1e-9, f"Expected 1.0, got {result}"

# ============================================================
# Test 35: cosine
# ============================================================
result = mymath.cosine(math.pi)
print(f"cosine(pi) = {result}")          # Expected: -1.0
assert abs(result - (-1.0)) < 1e-9, f"Expected -1.0, got {result}"

# ============================================================
# Test 36: tangent
# ============================================================
result = mymath.tangent(math.pi / 4)
print(f"tangent(pi/4) = {result}")        # Expected: 1.0
assert abs(result - 1.0) < 1e-9, f"Expected 1.0, got {result}"

# ============================================================
# Test 37: degrees_to_radians
# ============================================================
result = mymath.degrees_to_radians(180.0)
print(f"degrees_to_radians(180.0) = {result}")  # Expected: pi (~3.14159265)
assert abs(result - math.pi) < 1e-9, f"Expected {math.pi}, got {result}"

# ============================================================
# Test 38: radians_to_degrees
# ============================================================
result = mymath.radians_to_degrees(math.pi / 2.0)
print(f"radians_to_degrees(pi/2) = {result}")  # Expected: 90.0
assert abs(result - 90.0) < 1e-9, f"Expected 90.0, got {result}"

# ============================================================
# Test 39: median
# ============================================================
result1 = mymath.median([1, 3, 3, 6, 7, 8, 9])
print(f"median([1, 3, 3, 6, 7, 8, 9]) = {result1}")  # Expected: 6.0
assert result1 == 6.0, f"Expected 6.0, got {result1}"

result2 = mymath.median([1, 2, 3, 4, 5, 6, 8, 9])
print(f"median([1, 2, 3, 4, 5, 6, 8, 9]) = {result2}")  # Expected: 4.5
assert result2 == 4.5, f"Expected 4.5, got {result2}"

# ============================================================
# Test 40: median empty list error
# ============================================================
try:
    mymath.median([])
    print("ERROR: median([]) should have raised an exception!")
except RuntimeError as e:
    print(f"median([]) correctly raised: {e}")

# ============================================================
# Test 41: sinh
# ============================================================
result = mymath.sinh(0.0)
print(f"sinh(0.0) = {result}")          # Expected: 0.0
assert abs(result - 0.0) < 1e-9, f"Expected 0.0, got {result}"
assert abs(mymath.sinh(1.0) - math.sinh(1.0)) < 1e-9, "Expected sinh(1.0) to match math.sinh(1.0)"

# ============================================================
# Test 42: cosh
# ============================================================
result = mymath.cosh(0.0)
print(f"cosh(0.0) = {result}")          # Expected: 1.0
assert abs(result - 1.0) < 1e-9, f"Expected 1.0, got {result}"
assert abs(mymath.cosh(1.0) - math.cosh(1.0)) < 1e-9, "Expected cosh(1.0) to match math.cosh(1.0)"

# ============================================================
# Test 43: tanh
# ============================================================
result = mymath.tanh(0.0)
print(f"tanh(0.0) = {result}")          # Expected: 0.0
assert abs(result - 0.0) < 1e-9, f"Expected 0.0, got {result}"
assert abs(mymath.tanh(1.0) - math.tanh(1.0)) < 1e-9, "Expected tanh(1.0) to match math.tanh(1.0)"

# ============================================================
# Test 44: hypot
# ============================================================
result = mymath.hypot(3.0, 4.0)
print(f"hypot(3.0, 4.0) = {result}")      # Expected: 5.0
assert abs(result - 5.0) < 1e-9, f"Expected 5.0, got {result}"

# ============================================================
print("\n✅ All tests passed!")

