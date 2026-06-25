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
print("\n✅ All tests passed!")

