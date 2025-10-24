# Static Array

## Overview
A static array is a fixed-size, contiguous block of memory that stores elements of the same data type. The size is determined at compile time or initialization and cannot be changed.

## Key Characteristics
- **Fixed Size**: Cannot grow or shrink after creation
- **Contiguous Memory**: Elements stored in adjacent memory locations
- **Random Access**: O(1) time to access any element by index
- **Cache Friendly**: Sequential memory layout improves performance

## Time Complexity
| Operation | Time Complexity |
|-----------|----------------|
| Access    | O(1)          |
| Search    | O(n)          |
| Insert    | O(n)          |
| Delete    | O(n)          |

## Common Operations

### Reading/Writing
```python
arr = [1, 2, 3, 4, 5]
value = arr[2]      # O(1) - Access
arr[2] = 10         # O(1) - Update
```

### Traversal
```python
for i in range(len(arr)):
    print(arr[i])   # O(n) - Linear scan
```

## Advantages
- Fast access by index
- Memory efficient (no overhead)
- Predictable memory usage

## Disadvantages
- Fixed size limitation
- Insertion/deletion requires shifting elements
- Wasted space if not fully utilized

## Practice Problems
1. Two Sum
2. Remove Duplicates from Sorted Array
3. Best Time to Buy and Sell Stock
