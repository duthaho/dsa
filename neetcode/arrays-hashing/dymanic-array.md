# Dynamic Array

## Overview
A dynamic array is a resizable array data structure that automatically grows when elements are added beyond its current capacity. Unlike static arrays with fixed size, dynamic arrays provide the flexibility of adding elements without worrying about capacity limitations while maintaining O(1) random access.

## Key Characteristics
- **Random Access**: O(1) time to access elements by index
- **Automatic Resizing**: Grows when capacity is reached (typically doubles in size)
- **Contiguous Memory**: Elements stored in adjacent memory locations
- **Amortized Constant Time Append**: Despite occasional O(n) resize, average insertion is O(1)
- **Cache-Friendly**: Sequential memory layout improves cache performance

## Time Complexity
| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| Access    | O(1)        | O(1)       | Direct index lookup |
| Search    | O(n)        | O(n)       | Must check each element |
| Insert (end) | O(1)*    | O(n)       | *Amortized O(1) |
| Insert (middle) | O(n)  | O(n)       | Must shift elements |
| Delete (end) | O(1)     | O(1)       | Simple decrement |
| Delete (middle) | O(n)  | O(n)       | Must shift elements |
| Resize    | O(n)        | O(n)       | Copy all elements |

## Space Complexity
- **Used Space**: O(n) where n is the number of elements
- **Total Allocated**: O(capacity) - may be larger than n
- **Typical Overhead**: capacity is usually 1.5x to 2x the actual size

## How Dynamic Arrays Work

### 1. Initial State
```
Capacity: 2, Size: 0
[_, _]
```

### 2. Adding Elements
```python
# Add first element
arr.append(10)
Capacity: 2, Size: 1
[10, _]

# Add second element
arr.append(20)
Capacity: 2, Size: 2
[10, 20]  # Now at full capacity
```

### 3. Resizing Process
```python
# Add third element - triggers resize
arr.append(30)

# Step 1: Allocate new array (2x capacity)
New Capacity: 4
[_, _, _, _]

# Step 2: Copy existing elements
[10, 20, _, _]

# Step 3: Add new element
[10, 20, 30, _]
Capacity: 4, Size: 3
```

## Resizing Strategies

### Doubling Strategy (Most Common)
```
Initial: 1 → 2 → 4 → 8 → 16 → 32 → 64 → ...
Growth Factor: 2x
```

**Pros:**
- Amortized O(1) insertion
- Fewer resizes needed
- Simple to implement

**Cons:**
- Can waste up to 50% of memory
- Large allocations as array grows

### Growth Factor of 1.5x (Python)
```
Initial: 8 → 12 → 18 → 27 → 40 → 60 → ...
Growth Factor: ~1.5x
```

**Pros:**
- Better memory reuse
- Less wasted space
- Still maintains amortized O(1)

**Cons:**
- Slightly more resizes than 2x

## Amortized Analysis

### Why Append is O(1) Amortized

Consider appending n elements to an initially empty array:
1. Resize at sizes: 1, 2, 4, 8, 16, ..., n
2. Copy costs: 1 + 2 + 4 + 8 + ... + n/2 = n - 1
3. Total operations: n appends + (n-1) copies = 2n - 1
4. Average cost per operation: (2n - 1) / n ≈ 2 = O(1)

```python
# Example: Adding 8 elements
Operations:
1. Add elem 0: [e0] - cost 1
2. Add elem 1: [e0,e1] - cost 1 (resize: copy 1)
3. Add elem 2: [e0,e1,e2,_] - cost 3 (resize: copy 2)
4. Add elem 3: [e0,e1,e2,e3] - cost 1
5. Add elem 4: [e0,e1,e2,e3,e4,_,_,_] - cost 5 (resize: copy 4)
6. Add elem 5: [e0,e1,e2,e3,e4,e5,_,_] - cost 1
7. Add elem 6: [e0,e1,e2,e3,e4,e5,e6,_] - cost 1
8. Add elem 7: [e0,e1,e2,e3,e4,e5,e6,e7] - cost 1

Total cost: 1+2+3+1+5+1+1+1 = 15
Average: 15/8 ≈ 1.875 = O(1)
```

## Implementation Example

### Basic Dynamic Array Implementation
```python
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity
    
    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def append(self, value):
        """
        Time: O(1) amortized
        Space: O(1)
        """
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """
        Time: O(n) - must shift elements
        Space: O(1)
        """
        if not 0 <= index <= self.size:
            raise IndexError("Index out of range")
        
        if self.size == self.capacity:
            self._resize()
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        
        self.array[index] = value
        self.size += 1
    
    def pop(self, index=-1):
        """
        Time: O(n) for arbitrary index, O(1) for end
        Space: O(1)
        """
        if self.size == 0:
            raise IndexError("Pop from empty array")
        
        if index < 0:
            index = self.size + index
        
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        
        value = self.array[index]
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.size -= 1
        return value
    
    def _resize(self):
        """
        Time: O(n) - must copy all elements
        Space: O(n) - new array allocation
        """
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
    
    def __str__(self):
        return f"[{', '.join(str(self.array[i]) for i in range(self.size))}]


# Usage example
if __name__ == "__main__":
    arr = DynamicArray()
    
    # Append elements
    for i in range(5):
        arr.append(i * 10)
    print(arr)  # [0, 10, 20, 30, 40]
    
    # Insert in middle
    arr.insert(2, 15)
    print(arr)  # [0, 10, 15, 20, 30, 40]
    
    # Pop from end
    arr.pop()
    print(arr)  # [0, 10, 15, 20, 30]
```

## Python List Implementation Details

Python's `list` is a dynamic array with these characteristics:

### Growth Pattern
```python
# Python 3.x growth formula (approximate)
new_capacity = (old_capacity >> 1) + (old_capacity < 9 ? 3 : 6) + old_capacity

# Actual capacities observed:
# 0 → 4 → 8 → 16 → 25 → 35 → 46 → 58 → 72 → 88 → ...
```

### Memory Layout
```python
import sys

arr = []
print(sys.getsizeof(arr))  # 56 bytes (empty list overhead)

arr.append(1)
print(sys.getsizeof(arr))  # 88 bytes (space for 4 elements)

for i in range(10):
    arr.append(i)
    print(f"Length: {len(arr)}, Memory: {sys.getsizeof(arr)} bytes")
```

### Common Python List Operations
```python
from typing import List

# O(1) operations
arr = [1, 2, 3]
arr.append(4)           # Add to end
last = arr.pop()        # Remove from end
value = arr[0]          # Access by index
arr[0] = 10            # Update by index

# O(n) operations
arr.insert(0, 0)        # Insert at beginning (shift all)
arr.pop(0)              # Remove from beginning (shift all)
arr.remove(2)           # Remove by value (search + shift)
reversed_arr = arr[::-1]  # Reverse (create new array)
3 in arr                # Search for value

# O(n log n) operations
arr.sort()              # Sort in-place (Timsort)
sorted_arr = sorted(arr)  # Create sorted copy
```

## Common Use Cases

### 1. Sequential Data Storage
```python
# Store results from computation
results = []
for i in range(1000):
    results.append(compute(i))
```

### 2. Stack Implementation
```python
stack = []
stack.append(1)  # Push - O(1)
stack.append(2)
top = stack.pop()  # Pop - O(1)
```

### 3. Building Output Incrementally
```python
def get_positive_numbers(nums: List[int]) -> List[int]:
    result = []
    for num in nums:
        if num > 0:
            result.append(num)
    return result
```

## Comparison with Other Data Structures

| Feature | Dynamic Array | Linked List | Hash Table |
|---------|--------------|-------------|------------|
| Access by index | O(1) | O(n) | N/A |
| Insert at end | O(1)* | O(1) | O(1)* |
| Insert at beginning | O(n) | O(1) | N/A |
| Insert in middle | O(n) | O(1)** | N/A |
| Delete from end | O(1) | O(n)*** | O(1)* |
| Search | O(n) | O(n) | O(1)* |
| Memory overhead | Low | High | Medium |
| Cache performance | Excellent | Poor | Good |

*Amortized | **After finding position | ***Without tail pointer

## Pros and Cons

### Pros
- ✅ **Fast random access**: O(1) to get any element
- ✅ **Cache-friendly**: Contiguous memory improves performance
- ✅ **Simple to use**: Intuitive indexing and iteration
- ✅ **Memory efficient**: No pointers between elements
- ✅ **Fast iteration**: Sequential memory access

### Cons
- ❌ **Resizing overhead**: Occasional O(n) cost when growing
- ❌ **Wasted space**: Capacity typically exceeds size
- ❌ **Expensive insertions/deletions in middle**: Must shift elements
- ❌ **Fixed memory block**: Large arrays need contiguous memory
- ❌ **Insert at front is O(n)**: Poor performance for queue operations

## Practice Problems

### Easy
1. **Concatenation of Array** - LeetCode 1929
2. **Remove Duplicates from Sorted Array** - LeetCode 26
3. **Remove Element** - LeetCode 27
4. **Merge Sorted Array** - LeetCode 88

### Medium
5. **Product of Array Except Self** - LeetCode 238
6. **Insert Delete GetRandom O(1)** - LeetCode 380
7. **Rotate Array** - LeetCode 189
8. **3Sum** - LeetCode 15

### Hard
9. **First Missing Positive** - LeetCode 41
10. **Median of Two Sorted Arrays** - LeetCode 4

## Key Takeaways

1. **Amortized Analysis is Critical**: Understanding why append is O(1) amortized is fundamental
2. **Trade-offs Matter**: Fast access vs. expensive insertions/deletions
3. **Growth Factor Affects Performance**: 2x vs 1.5x has implications for memory and speed
4. **Python Lists are Optimized**: Built-in implementation is highly efficient
5. **Know When to Use**: Best for index-based access and appending; consider other structures for frequent insertions/deletions

## Additional Resources

- [Python Time Complexity Wiki](https://wiki.python.org/moin/TimeComplexity)
- [Amortized Analysis (MIT OpenCourseWare)](https://ocw.mit.edu/courses/6-046j-introduction-to-algorithms-sma-5503-fall-2005/)
- [Dynamic Array Visualization](https://www.cs.usfca.edu/~galles/visualization/DynamicArray.html)
