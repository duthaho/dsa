# Hash Map

## Overview
A hash map (also known as hash table or dictionary) is a data structure that implements an associative array abstract data type, mapping keys to values. It uses a hash function to compute an index into an array of buckets or slots.

## Key Concepts

### Hash Function
- Converts a key into an array index
- Should distribute keys uniformly across the array
- Common methods: division method, multiplication method

### Collision Handling
1. **Chaining**: Store multiple elements at the same index using linked lists
2. **Open Addressing**: Find another open slot in the array
    - Linear probing
    - Quadratic probing
    - Double hashing

## Time Complexity
- **Average Case**:
  - Insert: O(1)
  - Delete: O(1)
  - Search: O(1)
- **Worst Case**: O(n) when many collisions occur

## Space Complexity
O(n) where n is the number of key-value pairs

## Common Operations

```python
# Python Dictionary (Hash Map)
hash_map = {}

# Insert/Update
hash_map["key"] = "value"

# Search/Access
value = hash_map.get("key")

# Delete
del hash_map["key"]

# Check existence
if "key" in hash_map:
     pass

# Iterate
for key, value in hash_map.items():
     pass
```

## Common Use Cases
- Counting frequency of elements
- Storing key-value pairs for quick lookup
- Caching/memoization
- Detecting duplicates
- Two-sum and related problems

## Advantages
- Fast lookups, insertions, and deletions
- Flexible key types
- Dynamic sizing

## Disadvantages
- No ordering of elements
- Extra space for hash table structure
- Hash collisions can degrade performance

## Practice Problems
1. Two Sum
2. Group Anagrams
3. Valid Anagram
4. Subarray Sum Equals K
5. Longest Consecutive Sequence
