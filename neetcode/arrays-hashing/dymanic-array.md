# Dynamic Array

## Overview
A dynamic array is a resizable array data structure that automatically grows when elements are added beyond its current capacity.

## Key Characteristics
- **Random Access**: O(1) time to access elements by index
- **Automatic Resizing**: Grows when capacity is reached
- **Contiguous Memory**: Elements stored in adjacent memory locations

## Time Complexity
| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Access    | O(1)        | O(1)       |
| Search    | O(n)        | O(n)       |
| Insert (end) | O(1)     | O(n)*      |
| Insert (middle) | O(n)  | O(n)       |
| Delete (end) | O(1)     | O(1)       |
| Delete (middle) | O(n)  | O(n)       |

*Amortized O(1) due to resizing

## Space Complexity
O(n)

## How It Works
1. Initial array created with default capacity (e.g., 10)
2. When full, new array allocated (typically 2x size)
3. Old elements copied to new array
4. Old array deallocated

## Implementation Example (Python-like pseudocode)
```python
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.array = [None] * self.capacity
    
    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1
    
    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
```

## Common Use Cases
- ArrayList (Java)
- vector (C++)
- list (Python)
- Array (JavaScript)

## Pros and Cons
**Pros:**
- Fast random access
- Cache-friendly
- Simple to use

**Cons:**
- Resizing overhead
- Wasted space when not full
- Expensive insertions/deletions in middle
