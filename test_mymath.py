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
print("\n✅ All tests passed!")
