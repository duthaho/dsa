# Static Array

## Overview
A static array is a fixed-size, contiguous block of memory that stores elements of the same type. Once created, the size cannot be changed. Static arrays are the foundation of array-based data structures and provide the fastest random access to elements.

## Key Characteristics
- **Fixed Size**: Size determined at creation and cannot be changed
- **Random Access**: O(1) time to access elements by index
- **Contiguous Memory**: All elements stored in adjacent memory locations
- **Index-Based**: Elements accessed using zero-based indexing
- **Type Homogeneous**: All elements must be of the same type (in statically-typed languages)
- **Cache-Friendly**: Sequential memory layout maximizes CPU cache efficiency

## Time Complexity
| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Access    | O(1)           | Direct memory address calculation |
| Update    | O(1)           | Direct index assignment |
| Search    | O(n)           | Linear search required |
| Search (sorted) | O(log n) | Binary search possible |
| Insert    | Not supported* | Would require shifting + size change |
| Delete    | Not supported* | Would require shifting + size change |
| Traverse  | O(n)           | Visit each element once |

*Insertions/deletions require creating a new array or using workarounds

## Space Complexity
- **Fixed Space**: O(n) where n is the array size
- **No Overhead**: No metadata beyond the elements themselves
- **Memory Layout**: `size * element_size` bytes (plus small overhead for array object)

## Memory Layout

### Contiguous Memory Structure
```
Array: [10, 20, 30, 40, 50]
Indices: 0   1   2   3   4

Memory addresses (example):
Index 0: 0x1000 → 10
Index 1: 0x1004 → 20  (assuming 4 bytes per int)
Index 2: 0x1008 → 30
Index 3: 0x100C → 40
Index 4: 0x1010 → 50

Address calculation:
address(arr[i]) = base_address + (i * element_size)
```

### Why O(1) Access Works
```python
# Given: arr = [10, 20, 30, 40, 50]
# base_address = 0x1000
# element_size = 4 bytes

# To access arr[3]:
# address = 0x1000 + (3 * 4) = 0x100C
# Direct CPU instruction - no loop needed!
```

## Basic Operations

### 1. Creating Arrays

#### Python (Dynamic by nature, but can be fixed)
```python
# List (acts like dynamic array)
arr = [1, 2, 3, 4, 5]

# Fixed-size with array module
import array
fixed_arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed int

# NumPy array (truly fixed size)
import numpy as np
np_arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
```

#### Other Languages
```java
// Java
int[] arr = new int[5];  // Creates [0, 0, 0, 0, 0]
int[] arr2 = {1, 2, 3, 4, 5};

// C++
int arr[5];  // Uninitialized
int arr2[5] = {1, 2, 3, 4, 5};

// JavaScript (all arrays are dynamic, but can be treated as fixed)
const arr = new Array(5);  // Creates array with length 5
const arr2 = [1, 2, 3, 4, 5];
```

### 2. Accessing Elements
```python
arr = [10, 20, 30, 40, 50]

# Forward indexing (0-based)
first = arr[0]    # 10 - O(1)
third = arr[2]    # 30 - O(1)

# Negative indexing (Python)
last = arr[-1]    # 50 - O(1)
second_last = arr[-2]  # 40 - O(1)

# Out of bounds access
try:
    value = arr[10]  # IndexError
except IndexError as e:
    print(f"Error: {e}")
```

### 3. Updating Elements
```python
arr = [10, 20, 30, 40, 50]

# Update by index - O(1)
arr[0] = 100
arr[2] = 300
print(arr)  # [100, 20, 300, 40, 50]

# Update multiple elements - O(k) where k is count
for i in range(3):
    arr[i] *= 2
print(arr)  # [200, 40, 600, 40, 50]
```

### 4. Searching
```python
from typing import List

def linear_search(arr: List[int], target: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    """
    Requires sorted array.
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))  # 2

sorted_arr = [10, 20, 30, 40, 50]
print(binary_search(sorted_arr, 40))  # 3
```

### 5. Traversal Patterns
```python
arr = [10, 20, 30, 40, 50]

# Forward iteration
for num in arr:
    print(num, end=' ')  # 10 20 30 40 50

# Backward iteration
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=' ')  # 50 40 30 20 10

# With index
for i, num in enumerate(arr):
    print(f"arr[{i}] = {num}")

# Two pointers (common pattern)
left, right = 0, len(arr) - 1
while left < right:
    print(f"Pair: {arr[left]}, {arr[right]}")
    left += 1
    right -= 1
```

## Common Algorithms and Patterns

### 1. Prefix Sum
```python
from typing import List

def build_prefix_sum(arr: List[int]) -> List[int]:
    """
    Build prefix sum array for range sum queries.
    Time: O(n)
    Space: O(n)
    """
    n = len(arr)
    prefix = [0] * (n + 1)
    
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    return prefix

def range_sum(prefix: List[int], left: int, right: int) -> int:
    """
    Get sum of elements from left to right (inclusive).
    Time: O(1)
    """
    return prefix[right + 1] - prefix[left]

# Example
arr = [1, 2, 3, 4, 5]
prefix = build_prefix_sum(arr)
print(range_sum(prefix, 1, 3))  # sum of [2, 3, 4] = 9
```

### 2. Sliding Window
```python
from typing import List

def max_sum_subarray(arr: List[int], k: int) -> int:
    """
    Find maximum sum of k consecutive elements.
    Time: O(n)
    Space: O(1)
    """
    if len(arr) < k:
        return 0
    
    # Compute sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide window: remove left, add right
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(max_sum_subarray(arr, 4))  # 39 (10+23+3+1+0+20)
```

### 3. Two Pointers
```python
from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    """
    Find two numbers that sum to target in sorted array.
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

def reverse_array(arr: List[int]) -> None:
    """
    Reverse array in-place.
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Examples
arr1 = [1, 2, 3, 4, 6]
print(two_sum_sorted(arr1, 6))  # [1, 3] (2 + 4 = 6)

arr2 = [1, 2, 3, 4, 5]
reverse_array(arr2)
print(arr2)  # [5, 4, 3, 2, 1]
```

### 4. Kadane's Algorithm (Maximum Subarray)
```python
from typing import List

def max_subarray_sum(arr: List[int]) -> int:
    """
    Find maximum sum of any contiguous subarray.
    Time: O(n)
    Space: O(1)
    """
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend current subarray or start new one
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(arr))  # 6 (subarray [4, -1, 2, 1])
```

## Workarounds for Fixed Size Limitation

### 1. Creating New Array for "Insertion"
```python
from typing import List

def insert_at_index(arr: List[int], index: int, value: int) -> List[int]:
    """
    Create new array with inserted element.
    Time: O(n)
    Space: O(n)
    """
    new_arr = [0] * (len(arr) + 1)
    
    # Copy elements before index
    for i in range(index):
        new_arr[i] = arr[i]
    
    # Insert new value
    new_arr[index] = value
    
    # Copy elements after index
    for i in range(index, len(arr)):
        new_arr[i + 1] = arr[i]
    
    return new_arr

# Example
arr = [1, 2, 3, 5]
new_arr = insert_at_index(arr, 3, 4)
print(new_arr)  # [1, 2, 3, 4, 5]
```

### 2. Using Sentinel Values for "Deletion"
```python
from typing import List, Optional

def mark_deleted(arr: List[Optional[int]], index: int) -> None:
    """
    Mark element as deleted using None (sentinel value).
    Time: O(1)
    Space: O(1)
    """
    arr[index] = None

def compact_array(arr: List[Optional[int]]) -> List[int]:
    """
    Remove sentinel values and create compacted array.
    Time: O(n)
    Space: O(n)
    """
    return [x for x in arr if x is not None]

# Example
arr = [1, 2, 3, 4, 5]
mark_deleted(arr, 2)
print(arr)  # [1, 2, None, 4, 5]
compacted = compact_array(arr)
print(compacted)  # [1, 2, 4, 5]
```

## Multi-Dimensional Arrays

### 2D Arrays (Matrices)
```python
from typing import List

# Create 2D array (3x4 matrix)
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Access element - O(1)
element = matrix[1][2]  # 7

# Traverse row by row - O(rows * cols)
for row in matrix:
    for val in row:
        print(val, end=' ')

# Traverse column by column - O(rows * cols)
for col in range(len(matrix[0])):
    for row in range(len(matrix)):
        print(matrix[row][col], end=' ')

# Common operations
def transpose(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transpose matrix (swap rows and columns).
    Time: O(rows * cols)
    Space: O(rows * cols)
    """
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result

# Example
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose(matrix)
print(transposed)  # [[1, 4], [2, 5], [3, 6]]
```

## Python-Specific Features

### List Slicing
```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing - O(k) where k is slice length
arr[2:5]        # [2, 3, 4]
arr[:3]         # [0, 1, 2]
arr[7:]         # [7, 8, 9]
arr[:]          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy)

# Step parameter
arr[::2]        # [0, 2, 4, 6, 8] (every 2nd element)
arr[1::2]       # [1, 3, 5, 7, 9] (odd indices)
arr[::-1]       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# Negative indices
arr[-3:]        # [7, 8, 9] (last 3 elements)
arr[:-2]        # [0, 1, 2, 3, 4, 5, 6, 7] (all but last 2)
```

### List Comprehensions
```python
# Create array with comprehension - O(n)
squares = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filter with condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Transform elements
arr = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in arr]
# [2, 4, 6, 8, 10]

# Nested comprehension for 2D array
matrix = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

## Comparison with Other Data Structures

| Feature | Static Array | Dynamic Array | Linked List | Hash Table |
|---------|-------------|---------------|-------------|------------|
| Size | Fixed | Variable | Variable | Variable |
| Random access | O(1) | O(1) | O(n) | O(1)* |
| Memory | Contiguous | Contiguous | Scattered | Scattered |
| Insert at end | N/A | O(1)* | O(1) | O(1)* |
| Insert at start | N/A | O(n) | O(1) | N/A |
| Delete | N/A | O(n) | O(1) | O(1)* |
| Search | O(n) | O(n) | O(n) | O(1)* |
| Memory overhead | None | Low | High | Medium |
| Cache performance | Excellent | Excellent | Poor | Good |
| Use when | Size known, fast access | Size unknown, frequent access | Frequent insertions | Key-value lookups |

*Amortized | **After finding position

## Pros and Cons

### Pros
- ✅ **Fastest random access**: O(1) with no overhead
- ✅ **Memory efficient**: No extra pointers or metadata
- ✅ **Cache-friendly**: Contiguous memory = optimal CPU cache usage
- ✅ **Simple and predictable**: No hidden costs or surprises
- ✅ **Low-level control**: Direct memory access in systems programming

### Cons
- ❌ **Fixed size**: Cannot grow or shrink
- ❌ **No insertions/deletions**: Requires creating new array
- ❌ **Wasted space**: If array larger than needed
- ❌ **Not enough space**: If array smaller than needed
- ❌ **Contiguous memory requirement**: Large arrays may fail to allocate

## Common Use Cases

### 1. Known Size Collections
```python
# Days of week, months, etc.
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
```

### 2. Lookup Tables
```python
# Fibonacci lookup table
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def get_fibonacci(n: int) -> int:
    """O(1) lookup instead of O(2^n) recursive calculation"""
    return fib[n] if n < len(fib) else -1
```

### 3. Fixed-Size Buffers
```python
# Circular buffer for streaming data
class CircularBuffer:
    def __init__(self, size: int):
        self.buffer = [None] * size
        self.size = size
        self.head = 0
    
    def add(self, value):
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.size
```

### 4. Matrix Operations
```python
# Image processing, graph adjacency matrices
def create_identity_matrix(n: int) -> List[List[int]]:
    """Create n×n identity matrix"""
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 1
    return matrix
```

## Practice Problems

### Easy
1. **Running Sum of 1d Array** - LeetCode 1480
2. **Find Pivot Index** - LeetCode 724
3. **Best Time to Buy and Sell Stock** - LeetCode 121
4. **Two Sum** - LeetCode 1 (with sorted array)
5. **Move Zeroes** - LeetCode 283

### Medium
6. **Container With Most Water** - LeetCode 11
7. **3Sum** - LeetCode 15
8. **Product of Array Except Self** - LeetCode 238
9. **Maximum Subarray** - LeetCode 53
10. **Rotate Array** - LeetCode 189
11. **Set Matrix Zeroes** - LeetCode 73
12. **Spiral Matrix** - LeetCode 54

### Hard
13. **Trapping Rain Water** - LeetCode 42
14. **First Missing Positive** - LeetCode 41
15. **Median of Two Sorted Arrays** - LeetCode 4

## Key Takeaways

1. **Fundamental Building Block**: Understanding static arrays is crucial for all array-based structures
2. **Trade Size for Speed**: Fixed size is the cost of O(1) access and minimal overhead
3. **Memory Layout Matters**: Contiguous memory enables both fast access and cache efficiency
4. **Index Arithmetic**: Many optimizations come from clever index manipulation
5. **When to Use**: Best for known-size collections where fast random access is critical

## Interview Tips

1. **Always check bounds**: Prevent index out of range errors
2. **Consider two pointers**: Often more efficient than nested loops
3. **Think about space**: Can you solve in-place (O(1) space)?
4. **Edge cases matter**: Empty array, single element, duplicates
5. **Sorted vs unsorted**: Sorting (O(n log n)) might enable O(log n) searches

## Additional Resources

- [Arrays - GeeksforGeeks](https://www.geeksforgeeks.org/array-data-structure/)
- [Array Visualization](https://www.cs.usfca.edu/~galles/visualization/Array.html)
- [Memory Layout and Cache Performance](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf)
- [Python List Implementation](https://github.com/python/cpython/blob/main/Objects/listobject.c)
