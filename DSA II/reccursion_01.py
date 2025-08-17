# =============================================================================
# RECURSIVE FUNCTIONS COLLECTION
# =============================================================================


# 1. COUNT OCCURRENCES OF AN ELEMENT
# =============================================================================
def count_occurrences(lst, target):
    """
    Count how many times target appears in lst using recursion.

    Args:
        lst: List to search in
        target: Element to count

    Returns:
        Integer count of occurrences
    """
    if not lst:  # Base case: empty list
        return 0
    # Recursive case: check first element + count in rest of list
    return (lst[0] == target) + count_occurrences(lst[1:], target)


# Test the function
print("=== COUNT OCCURRENCES ===")
test_list = [1, 2, 3, 2, 2, 4, 2]
print(f"count_occurrences({test_list}, 2) = {count_occurrences(test_list, 2)}")
print(f"count_occurrences({test_list}, 5) = {count_occurrences(test_list, 5)}")


# 2. FIND MINIMUM IN A LIST
# =============================================================================
def find_min(lst):
    """
    Find the smallest number in a non-empty list using recursion.

    Args:
        lst: Non-empty list of numbers

    Returns:
        Minimum value in the list
    """
    if len(lst) == 1:  # Base case: single element
        return lst[0]
    # Recursive case: compare first element with min of rest
    return min(lst[0], find_min(lst[1:]))


# Test the function
print("\n=== FIND MINIMUM ===")
test_nums = [5, 2, 8, 1, 9, 3]
print(f"find_min({test_nums}) = {find_min(test_nums)}")


# 3. REVERSE A LINKED LIST
# =============================================================================
class ListNode:
    """Simple linked list node class"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """String representation for printing"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result) + " -> None"


def reverse_list(head):
    """
    Reverse a singly linked list recursively.

    Args:
        head: Head node of the linked list

    Returns:
        New head of the reversed list
    """
    if not head or not head.next:  # Base case: empty or single node
        return head

    # Recursively reverse the rest of the list
    new_head = reverse_list(head.next)

    # Reverse the current connection
    head.next.next = head
    head.next = None

    return new_head


# Test the function
print("\n=== REVERSE LINKED LIST ===")
# Create: 1 -> 2 -> 3 -> None
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

print(f"Original: {node1}")
reversed_head = reverse_list(node1)
print(f"Reversed: {reversed_head}")


# 4. REPLACE CHARACTERS IN A STRING
# =============================================================================
def replace_char(s, old, new):
    """
    Replace all occurrences of 'old' character with 'new' character recursively.

    Args:
        s: Input string
        old: Character to replace
        new: Replacement character

    Returns:
        New string with replacements made
    """
    if not s:  # Base case: empty string
        return ""

    # Choose replacement or keep original character
    first = new if s[0] == old else s[0]

    # Recursive case: process first char + recurse on rest
    return first + replace_char(s[1:], old, new)


# Test the function
print("\n=== REPLACE CHARACTERS ===")
test_string = "banana"
print(
    f'replace_char("{test_string}", "a", "o") = "{replace_char(test_string, "a", "o")}"'
)


# 5. BINARY SEARCH (RECURSIVE)
# =============================================================================
def binary_search(arr, target, low, high):
    """
    Recursive binary search to find target in sorted array.

    Args:
        arr: Sorted array to search
        target: Value to find
        low: Lower bound index
        high: Upper bound index

    Returns:
        Index of target if found, -1 otherwise
    """
    if low > high:  # Base case: target not found
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:  # Base case: found target
        return mid
    elif arr[mid] > target:  # Search left half
        return binary_search(arr, target, low, mid - 1)
    else:  # Search right half
        return binary_search(arr, target, mid + 1, high)


# Test the function
print("\n=== BINARY SEARCH ===")
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(f"Array: {sorted_array}")
print(f"binary_search(arr, 7, 0, 9) = {binary_search(sorted_array, 7, 0, 9)}")
print(f"binary_search(arr, 12, 0, 9) = {binary_search(sorted_array, 12, 0, 9)}")


# 6. MULTIPLY TWO INTEGERS IN O(log b)
# =============================================================================
def multiply(a, b):
    """
    Multiply two integers using only addition and recursion in O(log b) time.

    Args:
        a: First integer
        b: Second integer (non-negative)

    Returns:
        Product a * b
    """
    if b == 0:  # Base case: anything times 0 is 0
        return 0

    # Recursive case: divide b by 2
    half = multiply(a, b // 2)

    # If b is even: a*b = (a*(b/2)) + (a*(b/2))
    # If b is odd: a*b = (a*(b/2)) + (a*(b/2)) + a
    return half + half if b % 2 == 0 else half + half + a


# Test the function
print("\n=== FAST MULTIPLICATION ===")
print(f"multiply(7, 8) = {multiply(7, 8)}")
print(f"multiply(13, 5) = {multiply(13, 5)}")


# 7. CHECK IF ARRAY IS SORTED
# =============================================================================
def is_sorted(arr):
    """
    Check recursively if an array is sorted in non-decreasing order.

    Args:
        arr: Array to check

    Returns:
        True if sorted, False otherwise
    """
    if len(arr) < 2:  # Base case: empty or single element is sorted
        return True

    # Check first two elements and recurse on rest
    return arr[0] <= arr[1] and is_sorted(arr[1:])


# Test the function
print("\n=== CHECK IF SORTED ===")
sorted_arr = [1, 2, 3, 4, 5]
unsorted_arr = [1, 3, 2, 4, 5]
print(f"is_sorted({sorted_arr}) = {is_sorted(sorted_arr)}")
print(f"is_sorted({unsorted_arr}) = {is_sorted(unsorted_arr)}")


# 8. GENERATE BINARY STRINGS WITHOUT CONSECUTIVE 1s
# =============================================================================
def generate_binary(n):
    """
    Generate all binary strings of length n with no consecutive 1s.

    Args:
        n: Length of binary strings to generate
    """

    def backtrack(n, last, path):
        if n == 0:  # Base case: complete string
            print(path)
            return

        # Always can add 0
        backtrack(n - 1, 0, path + "0")

        # Can add 1 only if last character was 0
        if last == 0:
            backtrack(n - 1, 1, path + "1")

    print(f"\n=== BINARY STRINGS OF LENGTH {n} (NO CONSECUTIVE 1s) ===")
    backtrack(n, 0, "")


# Test the function
generate_binary(4)


# 9. COUNT UNIQUE PATHS IN A GRID
# =============================================================================
def count_paths(m, n):
    """
    Count paths from top-left to bottom-right in m×n grid.
    Can only move right or down.

    Args:
        m: Number of rows
        n: Number of columns

    Returns:
        Number of unique paths
    """
    if m == 1 or n == 1:  # Base case: single row or column
        return 1

    # Recursive case: paths from moving down + paths from moving right
    return count_paths(m - 1, n) + count_paths(m, n - 1)


# Test the function
print("\n=== COUNT GRID PATHS ===")
print(f"count_paths(3, 3) = {count_paths(3, 3)}")
print(f"count_paths(2, 4) = {count_paths(2, 4)}")


# 10. SUBSET SUM EQUALS K
# =============================================================================
def is_subset_sum(nums, k):
    """
    Check if there exists a subset that sums to k.

    Args:
        nums: List of integers
        k: Target sum

    Returns:
        True if subset exists, False otherwise
    """

    def helper(i, total):
        if total == k:  # Base case: found target sum
            return True
        if i >= len(nums):  # Base case: no more elements
            return False

        # Try including current element OR excluding it
        return helper(i + 1, total + nums[i]) or helper(i + 1, total)

    return helper(0, 0)


# Test the function
print("\n=== SUBSET SUM ===")
test_nums = [3, 34, 4, 12, 5, 2]
target = 9
print(f"nums = {test_nums}")
print(f"is_subset_sum(nums, {target}) = {is_subset_sum(test_nums, target)}")
print(f"is_subset_sum(nums, 50) = {is_subset_sum(test_nums, 50)}")


# 11. GENERATE BALANCED PARENTHESES
# =============================================================================
def generate_parentheses(n):
    """
    Generate all combinations of well-formed parentheses with n pairs.

    Args:
        n: Number of parentheses pairs

    Returns:
        List of all valid parentheses combinations
    """
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:  # Base case: complete string
            result.append(current)
            return

        # Add opening parenthesis if we haven't used all n
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)

        # Add closing parenthesis if it won't make string invalid
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


# Test the function
print("\n=== BALANCED PARENTHESES ===")
n = 3
result = generate_parentheses(n)
print(f"generate_parentheses({n}):")
for combo in result:
    print(f'  "{combo}"')

print(f"\nTotal combinations: {len(result)}")


# =============================================================================
# SUMMARY
# =============================================================================
print("\n" + "=" * 60)
print("RECURSION PATTERNS DEMONSTRATED:")
print("=" * 60)
print("1. Linear recursion (count, find_min, replace_char)")
print("2. Divide & conquer (binary_search, multiply)")
print("3. Tree recursion (count_paths, subset_sum)")
print("4. Backtracking (binary_strings, parentheses)")
print("5. Linked list recursion (reverse_list)")
print("6. Validation recursion (is_sorted)")
print("=" * 60)
