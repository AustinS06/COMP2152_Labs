# Week 05 Lab: Recursion & Functions - Complete Version
# COMP2152 - Python Programming

print("=" * 60)
print("WEEK 05 LAB: RECURSION & FUNCTIONS")
print("=" * 60)

# ============================================================
# Question 1: Fibonacci Number (LeetCode #509)
# Difficulty: Easy
# Concepts: Recursion, Base Cases, Recursive Case
# ============================================================

"""
PROBLEM STATEMENT:
The Fibonacci numbers form a sequence where:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1

Given n, calculate F(n).

Examples:
Input: n = 0 → Output: 0
Input: n = 1 → Output: 1
Input: n = 2 → Output: 1
Input: n = 3 → Output: 2
Input: n = 4 → Output: 3
Input: n = 10 → Output: 55
"""

print("\n" + "=" * 50)
print("Question 1: Fibonacci Number (#509)")
print("=" * 50)


def fib(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Base cases:
        If n == 0 → return 0
        If n == 1 → return 1

    Recursive case:
        Return fib(n - 1) + fib(n - 2)

    Every recursive function must:
        1. Have a base case
        2. Move toward the base case
    """

    # Base Case 1
    if n == 0:
        return 0

    # Base Case 2
    if n == 1:
        return 1

    # Recursive Case
    return fib(n - 1) + fib(n - 2)


# Test Fibonacci from 0 to 10
print("Fibonacci Sequence (F(0) to F(10)):")
print("-" * 30)
for i in range(11):
    print("F(" + str(i) + ") = " + str(fib(i)))

print("\nAdditional Test Cases:")
print("F(15) =", fib(15))
print("F(20) =", fib(20))


# ============================================================
# Question 2: FizzBuzz (LeetCode #412)
# Difficulty: Easy
# Concepts: Functions, Conditionals, List Building
# ============================================================

"""
PROBLEM STATEMENT:
Given an integer n, return a list of strings from 1 to n:

Divisible by 3 → "Fizz"
Divisible by 5 → "Buzz"
Divisible by BOTH 3 and 5 → "FizzBuzz"
Otherwise → number as string

IMPORTANT:
Check divisible by BOTH first!
"""

print("\n" + "=" * 50)
print("Question 2: FizzBuzz (#412)")
print("=" * 50)


def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):

        # MUST check both first!
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")

        elif i % 3 == 0:
            result.append("Fizz")

        elif i % 5 == 0:
            result.append("Buzz")

        else:
            result.append(str(i))

    return result


# Test Cases
print("\nTest Case 1: n = 3")
print(fizz_buzz(3))

print("\nTest Case 2: n = 5")
print(fizz_buzz(5))

print("\nTest Case 3: n = 15")
print(fizz_buzz(15))

print("\nTest Case 4: n = 1")
print(fizz_buzz(1))


# ============================================================
# Question 3: Binary Search (LeetCode #704)
# Difficulty: Easy
# Concepts: Divide & Conquer, Iteration & Recursion
# Time Complexity: O(log n)
# ============================================================

"""
PROBLEM STATEMENT:
Given a sorted array nums and a target value:

Return index if found
Return -1 if not found

Must run in O(log n) time.

Binary Search eliminates half of remaining elements each step.
Array MUST be sorted!
"""

print("\n" + "=" * 50)
print("Question 3: Binary Search (#704)")
print("=" * 50)


# ---------------------------
# Part A: Iterative Version
# ---------------------------

def binary_search_iterative(nums, target):

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif target < nums[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1


# ---------------------------
# Part B: Recursive Version
# ---------------------------

def binary_search_recursive(nums, target, left, right):

    # Base Case
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    elif target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)

    else:
        return binary_search_recursive(nums, target, mid + 1, right)


def search_recursive(nums, target):
    if len(nums) == 0:
        return -1
    return binary_search_recursive(nums, target, 0, len(nums) - 1)


# Test Cases
test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 3),
    ([], 5),
]

print("\n--- Iterative Results ---")
for nums, target in test_cases:
    print(nums, "target:", target, "→", binary_search_iterative(nums, target))

print("\n--- Recursive Results ---")
for nums, target in test_cases:
    print(nums, "target:", target, "→", search_recursive(nums, target))


# ============================================================
# Verification
# ============================================================

print("\n" + "=" * 50)
print("Verification: Both Methods Should Match")
print("=" * 50)

nums = [-1, 0, 3, 5, 9, 12]

for target in [-1, 0, 3, 5, 9, 12, 2, 100]:
    iter_result = binary_search_iterative(nums, target)
    rec_result = search_recursive(nums, target)

    status = "PASS" if iter_result == rec_result else "FAIL"

    print("Target", target,
          "Iterative =", iter_result,
          "Recursive =", rec_result,
          status)


print("\n" + "=" * 60)
print("LAB COMPLETE ✅")
print("=" * 60)

print("""
Key Concepts Practiced:

1. RECURSION
   - Base cases stop recursion
   - Recursive case moves toward base case
   - Call stack builds up and unwinds

2. FIZZBUZZ
   - Conditional logic order matters
   - List building
   - Modulo operator

3. BINARY SEARCH
   - Divide & Conquer
   - O(log n) time complexity
   - Sorted array required
   - Iterative vs Recursive approaches

From Grokking Algorithms:
- Chapter 1: Binary Search
- Chapter 3: Recursion
""")
