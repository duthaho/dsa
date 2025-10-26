# Hash Map (Hash Table / Dictionary)

## Overview
A hash map is a data structure that implements an associative array, mapping unique keys to values. It uses a hash function to compute an index (hash code) into an array of buckets or slots, from which the desired value can be found. Hash maps provide average O(1) time complexity for insertions, deletions, and lookups, making them one of the most efficient data structures for key-value storage.

## Key Characteristics
- **Key-Value Storage**: Maps unique keys to values
- **Fast Lookups**: O(1) average time for search, insert, and delete
- **Unordered**: No guaranteed order of elements (in most implementations)
- **Dynamic Sizing**: Automatically resizes when load factor exceeds threshold
- **Unique Keys**: Each key can appear at most once

## How Hash Maps Work

### 1. Hash Function
Converts a key into an array index:

```python
def hash_function(key, array_size):
    """
    Simple hash function example
    """
    # Method 1: Division method
    hash_code = hash(key)
    index = hash_code % array_size
    return index

# Example
key = "apple"
array_size = 10
index = hash("apple") % 10  # Returns index 0-9
```

### 2. Basic Structure
```
Hash Map with capacity 8:

Keys → Hash Function → Indices → Buckets

"apple"  → hash % 8 → 3 → [("apple", 5)]
"banana" → hash % 8 → 7 → [("banana", 3)]
"cherry" → hash % 8 → 3 → [("apple", 5), ("cherry", 8)]  # Collision!
```

### 3. Visual Example
```
Index  Bucket (Chaining)
  0    → []
  1    → [("grape", 10)]
  2    → []
  3    → [("apple", 5), ("cherry", 8)]  # Collision handled by chaining
  4    → [("date", 15)]
  5    → []
  6    → []
  7    → [("banana", 3)]
```

## Time Complexity

| Operation | Average Case | Worst Case | Notes |
|-----------|-------------|------------|-------|
| Insert    | O(1)        | O(n)       | O(n) when all keys collide |
| Delete    | O(1)        | O(n)       | Same as insert |
| Search    | O(1)        | O(n)       | Same as insert |
| Access    | O(1)        | O(n)       | Get value by key |
| Iteration | O(n)        | O(n)       | Visit all key-value pairs |

## Space Complexity
- **O(n)** where n is the number of key-value pairs
- **Additional overhead**: Buckets array and metadata (~1.5-2x actual elements)

## Hash Functions

### Properties of Good Hash Functions
1. **Deterministic**: Same key always produces same hash
2. **Uniform Distribution**: Keys spread evenly across array
3. **Fast Computation**: O(1) time to compute
4. **Avalanche Effect**: Small key change → large hash change

### Common Hash Function Methods

#### 1. Division Method
```python
def division_hash(key: int, table_size: int) -> int:
    """
    Simple but effective for integer keys.
    Time: O(1)
    """
    return key % table_size

# Example
print(division_hash(42, 10))  # 2
print(division_hash(157, 10))  # 7
```

#### 2. Multiplication Method
```python
def multiplication_hash(key: int, table_size: int) -> int:
    """
    Better distribution than division method.
    Time: O(1)
    """
    A = 0.6180339887  # (sqrt(5) - 1) / 2 (golden ratio)
    return int(table_size * ((key * A) % 1))

# Example
print(multiplication_hash(42, 10))  # 9
print(multiplication_hash(157, 10))  # 8
```

#### 3. String Hashing (Polynomial Rolling Hash)
```python
def string_hash(s: str, table_size: int) -> int:
    """
    Hash function for strings using polynomial method.
    Time: O(len(s))
    """
    hash_value = 0
    prime = 31  # Common prime for string hashing
    
    for char in s:
        hash_value = (hash_value * prime + ord(char)) % table_size
    
    return hash_value

# Example
print(string_hash("hello", 100))  # Some index 0-99
print(string_hash("world", 100))  # Different index
```

#### 4. Python's Built-in hash()
```python
# Python uses different hash functions for different types

# Integers
print(hash(42))        # Identity for small integers
print(hash(123456))    # Computed hash for large integers

# Strings
print(hash("hello"))   # SipHash algorithm (randomized per session)
print(hash("world"))

# Tuples (immutable)
print(hash((1, 2, 3)))  # Can be hashed

# Lists (mutable) - Cannot be hashed
try:
    print(hash([1, 2, 3]))
except TypeError as e:
    print(f"Error: {e}")  # unhashable type: 'list'
```

## Collision Resolution

### 1. Chaining (Separate Chaining)

Most common method: Each bucket contains a linked list of entries.

```python
from typing import List, Optional, Tuple

class HashMapChaining:
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size = 0
        self.buckets: List[List[Tuple[str, int]]] = [[] for _ in range(capacity)]
    
    def _hash(self, key: str) -> int:
        """Compute hash index for key."""
        return hash(key) % self.capacity
    
    def put(self, key: str, value: int) -> None:
        """
        Insert or update key-value pair.
        Time: O(1) average, O(n) worst case
        Space: O(1)
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Update if key exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Insert new key-value pair
        bucket.append((key, value))
        self.size += 1
        
        # Resize if load factor > 0.75
        if self.size / self.capacity > 0.75:
            self._resize()
    
    def get(self, key: str) -> Optional[int]:
        """
        Get value by key.
        Time: O(1) average, O(n) worst case
        Space: O(1)
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return None
    
    def remove(self, key: str) -> bool:
        """
        Remove key-value pair.
        Time: O(1) average, O(n) worst case
        Space: O(1)
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True
        
        return False
    
    def _resize(self) -> None:
        """
        Double the capacity and rehash all entries.
        Time: O(n)
        Space: O(n)
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        # Rehash all entries
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)


# Usage
if __name__ == "__main__":
    hm = HashMapChaining()
    hm.put("apple", 5)
    hm.put("banana", 3)
    hm.put("cherry", 8)
    
    print(hm.get("apple"))   # 5
    print(hm.get("banana"))  # 3
    print(hm.remove("apple"))  # True
    print(hm.get("apple"))   # None
```

### 2. Open Addressing (Linear Probing)

Store all entries in the array itself. When collision occurs, probe for next empty slot.

```python
from typing import Optional, Tuple

class HashMapOpenAddressing:
    def __init__(self, capacity: int = 8):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.DELETED = object()  # Sentinel for deleted entries
    
    def _hash(self, key: str) -> int:
        """Compute initial hash index."""
        return hash(key) % self.capacity
    
    def _probe(self, index: int, i: int) -> int:
        """
        Linear probing: try next slot.
        Could also use quadratic probing or double hashing.
        """
        return (index + i) % self.capacity
    
    def put(self, key: str, value: int) -> None:
        """
        Time: O(1) average, O(n) worst case
        Space: O(1)
        """
        if self.size >= self.capacity * 0.75:
            self._resize()
        
        index = self._hash(key)
        
        for i in range(self.capacity):
            probe_index = self._probe(index, i)
            
            # Empty slot or deleted slot
            if self.keys[probe_index] is None or self.keys[probe_index] is self.DELETED:
                self.keys[probe_index] = key
                self.values[probe_index] = value
                self.size += 1
                return
            
            # Update existing key
            if self.keys[probe_index] == key:
                self.values[probe_index] = value
                return
        
        raise Exception("Hash table is full")
    
    def get(self, key: str) -> Optional[int]:
        """
        Time: O(1) average, O(n) worst case
        Space: O(1)
        """
        index = self._hash(key)
        
        for i in range(self.capacity):
            probe_index = self._probe(index, i)
            
            # Key found
            if self.keys[probe_index] == key:
                return self.values[probe_index]
            
            # Empty slot means key doesn't exist
            if self.keys[probe_index] is None:
                return None
        
        return None
    
    def remove(self, key: str) -> bool:
        """
        Mark as deleted rather than setting to None.
        Time: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        
        for i in range(self.capacity):
            probe_index = self._probe(index, i)
            
            if self.keys[probe_index] == key:
                self.keys[probe_index] = self.DELETED
                self.values[probe_index] = None
                self.size -= 1
                return True
            
            if self.keys[probe_index] is None:
                return False
        
        return False
    
    def _resize(self) -> None:
        """Rehash all entries into larger table."""
        old_keys = self.keys
        old_values = self.values
        
        self.capacity *= 2
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.size = 0
        
        for i in range(len(old_keys)):
            if old_keys[i] is not None and old_keys[i] is not self.DELETED:
                self.put(old_keys[i], old_values[i])
```

## Load Factor and Resizing

### Load Factor
```
load_factor = number_of_entries / table_capacity

Typical thresholds:
- Chaining: Resize at 0.75 (75% full)
- Open Addressing: Resize at 0.5-0.7 (50-70% full)
```

### Why Resize?
```python
# Performance degrades with high load factor

# Low load factor (0.5): Avg 1.5 probes per operation
# Medium load factor (0.75): Avg 2-3 probes per operation  
# High load factor (0.9): Avg 10+ probes per operation
```

## Python Dictionary Implementation

### Built-in dict Operations
```python
from typing import Dict

# Creation
hash_map: Dict[str, int] = {}
hash_map = dict()
hash_map = {"apple": 5, "banana": 3}

# Insert/Update - O(1)
hash_map["cherry"] = 8
hash_map["apple"] = 10  # Update existing

# Access - O(1)
value = hash_map["apple"]  # Raises KeyError if not found
value = hash_map.get("apple")  # Returns None if not found
value = hash_map.get("grape", 0)  # Returns 0 if not found

# Delete - O(1)
del hash_map["apple"]
value = hash_map.pop("banana")  # Returns value and removes
value = hash_map.pop("missing", -1)  # Returns -1 if not found

# Check existence - O(1)
if "cherry" in hash_map:
    print("Found")

# Size - O(1)
size = len(hash_map)

# Clear - O(n)
hash_map.clear()
```

### Iteration Patterns
```python
hash_map = {"a": 1, "b": 2, "c": 3}

# Iterate over keys - O(n)
for key in hash_map:
    print(key)

for key in hash_map.keys():
    print(key)

# Iterate over values - O(n)
for value in hash_map.values():
    print(value)

# Iterate over key-value pairs - O(n)
for key, value in hash_map.items():
    print(f"{key}: {value}")
```

### Advanced Operations
```python
from collections import defaultdict, Counter

# defaultdict - auto-initialize missing keys
freq = defaultdict(int)
freq["a"] += 1  # No KeyError, defaults to 0

grouped = defaultdict(list)
grouped["fruits"].append("apple")  # No KeyError, defaults to []

# Counter - specialized for counting
from collections import Counter
arr = [1, 2, 2, 3, 3, 3]
count = Counter(arr)  # Counter({3: 3, 2: 2, 1: 1})
print(count[2])  # 2
print(count.most_common(2))  # [(3, 3), (2, 2)]

# Update/merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)  # dict1 = {"a": 1, "b": 3, "c": 4}

# Python 3.9+ merge operator
merged = dict1 | dict2
```

## Common Patterns and Use Cases

### 1. Frequency Counting
```python
from typing import List
from collections import Counter

def count_frequencies(arr: List[int]) -> dict:
    """
    Count frequency of each element.
    Time: O(n)
    Space: O(n)
    """
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Or use Counter
def count_with_counter(arr: List[int]) -> Counter:
    """Time: O(n), Space: O(n)"""
    return Counter(arr)

# Example
arr = [1, 2, 2, 3, 3, 3]
print(count_frequencies(arr))  # {1: 1, 2: 2, 3: 3}
```

### 2. Two Sum Pattern
```python
from typing import List, Optional

def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    """
    Find two numbers that add up to target.
    Time: O(n)
    Space: O(n)
    """
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return None

# Example
nums = [2, 7, 11, 15]
print(two_sum(nums, 9))  # [0, 1]
```

### 3. Grouping/Categorizing
```python
from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams.
    Time: O(n * k log k) where k is max string length
    Space: O(n * k)
    """
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))  # Anagrams have same sorted form
        groups[key].append(s)
    
    return list(groups.values())

# Example
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

### 4. Caching/Memoization
```python
from typing import Dict

def fibonacci_memo(n: int, cache: Dict[int, int] = None) -> int:
    """
    Fibonacci with memoization.
    Time: O(n) with memoization vs O(2^n) without
    Space: O(n)
    """
    if cache is None:
        cache = {}
    
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    cache[n] = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)
    return cache[n]

# Example
print(fibonacci_memo(10))  # 55
```

### 5. Detecting Duplicates
```python
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains duplicates.
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Or simply
def contains_duplicate_set(nums: List[int]) -> bool:
    """Time: O(n), Space: O(n)"""
    return len(nums) != len(set(nums))
```

### 6. Character/Substring Patterns
```python
from collections import defaultdict

def find_anagrams(s: str, p: str) -> List[int]:
    """
    Find all start indices of p's anagrams in s.
    Time: O(n)
    Space: O(1) - at most 26 characters
    """
    if len(p) > len(s):
        return []
    
    result = []
    p_count = Counter(p)
    window_count = Counter()
    
    # Initialize first window
    for i in range(len(p)):
        window_count[s[i]] += 1
    
    if window_count == p_count:
        result.append(0)
    
    # Slide window
    for i in range(len(p), len(s)):
        # Add new character
        window_count[s[i]] += 1
        
        # Remove old character
        left_char = s[i - len(p)]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
        
        if window_count == p_count:
            result.append(i - len(p) + 1)
    
    return result
```

## Comparison with Other Data Structures

| Feature | Hash Map | Array | Binary Search Tree | Linked List |
|---------|----------|-------|-------------------|-------------|
| Search by key | O(1)* | O(n) | O(log n) | O(n) |
| Insert | O(1)* | O(n) | O(log n) | O(1)** |
| Delete | O(1)* | O(n) | O(log n) | O(1)** |
| Ordered | No | Yes (by index) | Yes | No |
| Memory overhead | Medium | Low | High | High |
| Cache performance | Good | Excellent | Poor | Poor |
| Range queries | No | Yes | Yes | No |
| Min/Max | O(n) | O(n) | O(log n) | O(n) |

*Average case | **After finding position

## Pros and Cons

### Pros
- ✅ **Fast lookups**: O(1) average time for search/insert/delete
- ✅ **Flexible keys**: Can use strings, numbers, tuples as keys
- ✅ **Easy to use**: Simple API and intuitive operations
- ✅ **Dynamic sizing**: Automatically grows as needed
- ✅ **Versatile**: Counting, grouping, caching, and more

### Cons
- ❌ **No ordering**: Elements not stored in any particular order
- ❌ **Space overhead**: Extra memory for buckets and structure
- ❌ **Hash collisions**: Can degrade to O(n) in worst case
- ❌ **No range queries**: Can't efficiently find all keys in range
- ❌ **Keys must be hashable**: Mutable objects (lists, dicts) can't be keys

## Practice Problems

### Easy
1. **Two Sum** - LeetCode 1
2. **Valid Anagram** - LeetCode 242
3. **Contains Duplicate** - LeetCode 217
4. **Jewels and Stones** - LeetCode 771
5. **Single Number** - LeetCode 136

### Medium
6. **Group Anagrams** - LeetCode 49
7. **Top K Frequent Elements** - LeetCode 347
8. **Subarray Sum Equals K** - LeetCode 560
9. **Longest Consecutive Sequence** - LeetCode 128
10. **Encode and Decode TinyURL** - LeetCode 535
11. **Design HashMap** - LeetCode 706
12. **Product of Array Except Self** - LeetCode 238
13. **Valid Sudoku** - LeetCode 36

### Hard
14. **LRU Cache** - LeetCode 146
15. **First Missing Positive** - LeetCode 41
16. **Substring with Concatenation of All Words** - LeetCode 30

## Key Takeaways

1. **Average O(1) is Powerful**: Hash maps enable many algorithms to achieve linear time
2. **Hash Function Quality Matters**: Poor hash function → many collisions → poor performance
3. **Load Factor Affects Performance**: Keep load factor reasonable (0.5-0.75)
4. **Choose Right Collision Method**: Chaining for general use, open addressing for cache efficiency
5. **Understand Trade-offs**: Fast access but no ordering; space overhead for speed

## Interview Tips

1. **Clarify key types**: What kinds of keys will be used?
2. **Consider space complexity**: Hash map uses O(n) extra space
3. **Watch for duplicates**: Hash maps naturally handle duplicates
4. **Think about Counter**: Often simpler than manual counting
5. **defaultdict is your friend**: Avoid KeyError with default values
6. **Set operations**: For membership testing, use sets (hash set)

## Additional Resources

- [Hash Table - Wikipedia](https://en.wikipedia.org/wiki/Hash_table)
- [Python dict Implementation](https://github.com/python/cpython/blob/main/Objects/dictobject.c)
- [Hash Table Visualization](https://www.cs.usfca.edu/~galles/visualization/OpenHash.html)
- [Load Factor and Performance](https://en.wikipedia.org/wiki/Hash_table#Load_factor)
