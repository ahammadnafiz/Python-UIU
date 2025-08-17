#!/usr/bin/env python3
"""
Complete Recursive Programming Solutions
All problems solved in one comprehensive Python script
"""

# ================================
# COMMON PROBLEMS
# ================================


def factorial(n):
    """Calculate factorial of n recursively"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def power(x, y):
    """Calculate x^y recursively where y is non-negative"""
    if y == 0:
        return 1
    return x * power(x, y - 1)


def fibonacci(n):
    """Calculate nth Fibonacci number recursively"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_palindrome_string(s):
    """Check if string is palindrome (case insensitive, ignore spaces)"""
    cleaned = "".join(s.split()).lower()

    def check_palindrome(text, start, end):
        if start >= end:
            return True
        if text[start] != text[end]:
            return False
        return check_palindrome(text, start + 1, end - 1)

    return check_palindrome(cleaned, 0, len(cleaned) - 1)


# ================================
# NUMBERS
# ================================


def print_even_numbers_range(start, end):
    """Print even numbers in given range recursively"""
    if start > end:
        return
    if start % 2 == 0:
        print(start, end=" ")
    print_even_numbers_range(start + 1, end)


# ================================
# 1D ARRAY PROBLEMS
# ================================


def print_array(arr, index=0):
    """Print array in given order"""
    if index >= len(arr):
        return
    print(arr[index], end=" ")
    print_array(arr, index + 1)


def print_array_reverse(arr, index=None):
    """Print array in reverse order"""
    if index is None:
        index = len(arr) - 1
    if index < 0:
        return
    print(arr[index], end=" ")
    print_array_reverse(arr, index - 1)


def array_sum(arr, index=0):
    """Find sum of array elements"""
    if index >= len(arr):
        return 0
    return arr[index] + array_sum(arr, index + 1)


def array_product(arr, index=0):
    """Find product of array elements"""
    if index >= len(arr):
        return 1
    return arr[index] * array_product(arr, index + 1)


def array_max(arr, index=0):
    """Find maximum element in array"""
    if index >= len(arr):
        return float("-inf")
    return max(arr[index], array_max(arr, index + 1))


def array_min(arr, index=0):
    """Find minimum element in array"""
    if index >= len(arr):
        return float("inf")
    return min(arr[index], array_min(arr, index + 1))


def array_average(arr):
    """Find average of array elements"""

    def sum_helper(arr, index=0):
        if index >= len(arr):
            return 0
        return arr[index] + sum_helper(arr, index + 1)

    return sum_helper(arr) / len(arr) if len(arr) > 0 else 0


def print_odd_numbers(arr, index=0):
    """Print odd numbers from array"""
    if index >= len(arr):
        return
    if arr[index] % 2 == 1:
        print(arr[index], end=" ")
    print_odd_numbers(arr, index + 1)


def print_even_numbers_array(arr, index=0):
    """Print even numbers from array"""
    if index >= len(arr):
        return
    if arr[index] % 2 == 0:
        print(arr[index], end=" ")
    print_even_numbers_array(arr, index + 1)


def is_prime(n, divisor=2):
    """Check if number is prime recursively"""
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)


def print_prime_numbers(arr, index=0):
    """Print prime numbers from array"""
    if index >= len(arr):
        return
    if is_prime(arr[index]):
        print(arr[index], end=" ")
    print_prime_numbers(arr, index + 1)


def count_odd_numbers(arr, index=0):
    """Count odd numbers in array"""
    if index >= len(arr):
        return 0
    if arr[index] % 2 == 1:
        return 1 + count_odd_numbers(arr, index + 1)
    else:
        return count_odd_numbers(arr, index + 1)


def count_even_numbers(arr, index=0):
    """Count even numbers in array"""
    if index >= len(arr):
        return 0
    if arr[index] % 2 == 0:
        return 1 + count_even_numbers(arr, index + 1)
    else:
        return count_even_numbers(arr, index + 1)


def count_prime_numbers(arr, index=0):
    """Count prime numbers in array"""
    if index >= len(arr):
        return 0
    if is_prime(arr[index]):
        return 1 + count_prime_numbers(arr, index + 1)
    else:
        return count_prime_numbers(arr, index + 1)


# ================================
# 2D ARRAY PROBLEMS
# ================================


def max_2d_array(arr, row=0, col=0):
    """Find maximum in 2D array"""
    if row >= len(arr):
        return float("-inf")
    if col >= len(arr[row]):
        return max_2d_array(arr, row + 1, 0)
    current = arr[row][col]
    rest_max = max_2d_array(arr, row, col + 1)
    return max(current, rest_max)


def count_prime_2d(arr, row=0, col=0):
    """Count prime numbers in 2D array"""
    if row >= len(arr):
        return 0
    if col >= len(arr[row]):
        return count_prime_2d(arr, row + 1, 0)
    count = 1 if is_prime(arr[row][col]) else 0
    return count + count_prime_2d(arr, row, col + 1)


# ================================
# SERIES PROBLEMS
# ================================


def sum_series_1(n):
    """Sum series: 1+2+3+..."""
    if n <= 0:
        return 0
    return n + sum_series_1(n - 1)


def sum_series_2(n):
    """Sum series: 1²+2²+3²+..."""
    if n <= 0:
        return 0
    return n * n + sum_series_2(n - 1)


def sum_series_3(n):
    """Sum series: 1*3+2*5+3*7+4*9+..."""
    if n <= 0:
        return 0
    return n * (2 * n + 1) + sum_series_3(n - 1)


def sum_series_4(n):
    """Sum series: 2*3+4*5+8*7+16*9+..."""
    if n <= 0:
        return 0
    return (2**n) * (2 * n + 1) + sum_series_4(n - 1)


def sum_series_5(n):
    """Sum series: 2*3*4+4*5*3+8*7*2+16*9*1+..."""
    if n <= 0:
        return 0
    return (2**n) * (2 * n + 1) * (5 - n) + sum_series_5(n - 1)


def print_series_1(n):
    """Print series: 1+2+3+..."""
    if n <= 0:
        return
    print_series_1(n - 1)
    if n > 1:
        print("+", end="")
    print(n, end="")


def print_series_2(n):
    """Print series: 1²+2²+3²+..."""
    if n <= 0:
        return
    print_series_2(n - 1)
    if n > 1:
        print("+", end="")
    print(f"{n}²", end="")


def print_series_3(n):
    """Print series: 1*3+2*5+3*7+4*9+..."""
    if n <= 0:
        return
    print_series_3(n - 1)
    if n > 1:
        print("+", end="")
    print(f"{n}*{2*n+1}", end="")


def print_series_4(n):
    """Print series: 2*3+4*5+8*7+16*9+..."""
    if n <= 0:
        return
    print_series_4(n - 1)
    if n > 1:
        print("+", end="")
    print(f"{2**n}*{2*n+1}", end="")


def print_series_5(n):
    """Print series: 2*3*4+4*5*3+8*7*2+16*9*1+..."""
    if n <= 0:
        return
    print_series_5(n - 1)
    if n > 1:
        print("+", end="")
    print(f"{2**n}*{2*n+1}*{5-n}", end="")


# ================================
# GCD/LCM PROBLEMS
# ================================


def gcd(x, y):
    """Find GCD using Euclidean algorithm"""
    if y == 0:
        return x
    return gcd(y, x % y)


def gcd_subtraction(x, y):
    """Find GCD using subtraction method"""
    if x == y:
        return x
    if x > y:
        return gcd_subtraction(x - y, y)
    else:
        return gcd_subtraction(x, y - x)


def lcm(x, y):
    """Find LCM using GCD"""
    return (x * y) // gcd(x, y)


def lcm_recursive(x, y, multiple=None):
    """Find LCM using recursive multiplication"""
    if multiple is None:
        multiple = max(x, y)
    if multiple % x == 0 and multiple % y == 0:
        return multiple
    return lcm_recursive(x, y, multiple + max(x, y))


# ================================
# DIGIT PROBLEMS
# ================================


def count_digits(n):
    """Count number of digits"""
    if n == 0:
        return 1
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def sum_of_digits(n):
    """Find sum of digits"""
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


def is_number_palindrome(n):
    """Check if number is palindrome"""

    def reverse_number(num, reversed_num=0):
        if num == 0:
            return reversed_num
        return reverse_number(num // 10, reversed_num * 10 + num % 10)

    return n == reverse_number(n)


# ================================
# SUBSET PROBLEMS
# ================================


def print_all_subsets(arr, index=0, current_subset=[]):
    """Print all subsets of a set"""
    if index == len(arr):
        print(current_subset)
        return
    # Include current element
    print_all_subsets(arr, index + 1, current_subset + [arr[index]])
    # Exclude current element
    print_all_subsets(arr, index + 1, current_subset)


def print_subsequences(s, index=0, current=""):
    """Print all subsequences of a string"""
    if index == len(s):
        print(f"'{current}'")
        return
    # Include current character
    print_subsequences(s, index + 1, current + s[index])
    # Exclude current character
    print_subsequences(s, index + 1, current)


# ================================
# MISCELLANEOUS PROBLEMS
# ================================


def binary_search(arr, target, left=0, right=None):
    """Binary search in sorted array"""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)


def are_parentheses_balanced(s, index=0, count=0):
    """Check if parentheses are balanced"""
    if index == len(s):
        return count == 0
    if count < 0:
        return False
    if s[index] == "(":
        count += 1
    elif s[index] == ")":
        count -= 1
    return are_parentheses_balanced(s, index + 1, count)


def dfs_recursive(graph, node, visited=None):
    """DFS traversal of graph"""
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


class TreeNode:
    """Binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """Inorder traversal: left, root, right"""
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)


def preorder_traversal(root):
    """Preorder traversal: root, left, right"""
    if root is None:
        return
    print(root.val, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


def postorder_traversal(root):
    """Postorder traversal: left, right, root"""
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=" ")


def print_path_to_root(root, target, path=[]):
    """Print path from node to root"""
    if root is None:
        return False
    path.append(root.val)
    if root.val == target:
        print(" -> ".join(map(str, path)))
        return True
    if print_path_to_root(root.left, target, path) or print_path_to_root(
        root.right, target, path
    ):
        return True
    path.pop()
    return False


def tower_of_hanoi(n, source="A", destination="C", auxiliary="B"):
    """Solve Tower of Hanoi problem"""
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# ================================
# MAIN FUNCTION AND TESTS
# ================================


def main():
    """Test all functions"""

    print("=" * 50)
    print("RECURSIVE PROGRAMMING SOLUTIONS - TEST RESULTS")
    print("=" * 50)

    # Common Problems
    print("\n1. COMMON PROBLEMS")
    print("-" * 30)
    print(f"Factorial of 5: {factorial(5)}")
    print(f"2^3 = {power(2, 3)}")
    print(f"6th Fibonacci number: {fibonacci(6)}")
    print(f"Is 'Evil olive' palindrome? {is_palindrome_string('Evil olive')}")
    print(f"Is 'Too bad' palindrome? {is_palindrome_string('Too bad')}")

    # Numbers
    print("\n2. NUMBERS")
    print("-" * 30)
    print("Even numbers from 1 to 10:")
    print_even_numbers_range(1, 10)
    print()

    # 1D Array Problems
    print("\n3. 1D ARRAY PROBLEMS")
    print("-" * 30)
    test_array = [1, 2, 3, 4, 5]
    print(f"Original array: {test_array}")
    print("Array in order: ", end="")
    print_array(test_array)
    print()
    print("Array in reverse: ", end="")
    print_array_reverse(test_array)
    print()
    print(f"Sum: {array_sum(test_array)}")
    print(f"Product: {array_product(test_array)}")
    print(f"Maximum: {array_max(test_array)}")
    print(f"Minimum: {array_min(test_array)}")
    print(f"Average: {array_average(test_array)}")

    mixed_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(f"\nMixed array: {mixed_array}")
    print("Odd numbers: ", end="")
    print_odd_numbers(mixed_array)
    print()
    print("Even numbers: ", end="")
    print_even_numbers_array(mixed_array)
    print()
    print("Prime numbers: ", end="")
    print_prime_numbers(mixed_array)
    print()
    print(f"Odd count: {count_odd_numbers(mixed_array)}")
    print(f"Even count: {count_even_numbers(mixed_array)}")
    print(f"Prime count: {count_prime_numbers(mixed_array)}")

    # 2D Array Problems
    print("\n4. 2D ARRAY PROBLEMS")
    print("-" * 30)
    array_2d = [[1, 2, 3], [4, 9, 6], [7, 8, 2]]
    print(f"2D Array: {array_2d}")
    print(f"Maximum: {max_2d_array(array_2d)}")

    prime_2d = [[2, 3, 4], [5, 6, 7], [8, 9, 11]]
    print(f"Prime 2D Array: {prime_2d}")
    print(f"Prime count: {count_prime_2d(prime_2d)}")

    # Series Problems
    print("\n5. SERIES PROBLEMS")
    print("-" * 30)
    n = 4
    print(f"Series 1 (n={n}): ", end="")
    print_series_1(n)
    print(f" = {sum_series_1(n)}")

    print(f"Series 2 (n={n}): ", end="")
    print_series_2(n)
    print(f" = {sum_series_2(n)}")

    print(f"Series 3 (n={n}): ", end="")
    print_series_3(n)
    print(f" = {sum_series_3(n)}")

    print(f"Series 4 (n={n}): ", end="")
    print_series_4(n)
    print(f" = {sum_series_4(n)}")

    print(f"Series 5 (n={n}): ", end="")
    print_series_5(n)
    print(f" = {sum_series_5(n)}")

    # GCD/LCM
    print("\n6. GCD/LCM PROBLEMS")
    print("-" * 30)
    print(f"GCD of 48 and 18: {gcd(48, 18)}")
    print(f"GCD (subtraction) of 48 and 18: {gcd_subtraction(48, 18)}")
    print(f"LCM of 12 and 18: {lcm(12, 18)}")
    print(f"LCM (recursive) of 12 and 18: {lcm_recursive(12, 18)}")

    # Digit Problems
    print("\n7. DIGIT PROBLEMS")
    print("-" * 30)
    test_num = 12345
    print(f"Number: {test_num}")
    print(f"Digit count: {count_digits(test_num)}")
    print(f"Sum of digits: {sum_of_digits(test_num)}")
    print(f"Is 12321 palindrome? {is_number_palindrome(12321)}")
    print(f"Is {test_num} palindrome? {is_number_palindrome(test_num)}")

    # Subset Problems
    print("\n8. SUBSET PROBLEMS")
    print("-" * 30)
    print("All subsets of [1, 2, 3]:")
    print_all_subsets([1, 2, 3])
    print("\nAll subsequences of 'abc':")
    print_subsequences("abc")

    # Miscellaneous
    print("\n9. MISCELLANEOUS PROBLEMS")
    print("-" * 30)
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(
        f"Binary search for {target} in {sorted_array}: Index {binary_search(sorted_array, target)}"
    )

    print(f"Are '((()))' balanced? {are_parentheses_balanced('((()))')}")
    print(f"Are '(())' balanced? {are_parentheses_balanced('(())')}")

    # Graph DFS
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }
    print("DFS traversal from A: ", end="")
    dfs_recursive(graph, "A")
    print()

    # Binary Tree Traversals
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Binary tree traversals:")
    print("Inorder: ", end="")
    inorder_traversal(root)
    print()
    print("Preorder: ", end="")
    preorder_traversal(root)
    print()
    print("Postorder: ", end="")
    postorder_traversal(root)
    print()

    print("Path from 5 to root:")
    print_path_to_root(root, 5)

    # Tower of Hanoi
    print("\n10. TOWER OF HANOI (4 disks)")
    print("-" * 30)
    tower_of_hanoi(4)

    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED!")
    print("=" * 50)


if __name__ == "__main__":
    main()
