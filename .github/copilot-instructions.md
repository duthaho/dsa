# Copilot Instructions for DSA Practice Repository

## Repository Purpose
This is a **data structures and algorithms practice repository** organized by problem categories from NeetCode. Each solution is a self-contained Python file with LeetCode problem links, examples, and complexity analysis.

## File Organization Pattern
- Structure: `neetcode/<category>/<##-problem-name>.py`
- Markdown guides: `<category>/<data-structure-name>.md` (e.g., `hash-map.md`, `static-array.md`)
- Numbering: Files use zero-padded prefixes (`01-`, `02-`) indicating problem sequence

## Code Style Conventions

### File Structure (mandatory for all solutions)
```python
"""
Problem statement with examples, constraints, and recommended complexity.
Include LeetCode problem link at the top of the docstring.
"""

# LeetCode Problem Link: https://leetcode.com/problems/<problem-slug>/

from typing import List  # Import type hints as needed
from collections import Counter, defaultdict  # Common imports


class Solution:
    def methodName(self, params) -> ReturnType:
        """
        Time Complexity: O(n) where n is...
        Space Complexity: O(n) for...
        """
        # Implementation here
        pass
    
    def methodNameAlternative(self, params) -> ReturnType:
        """
        Alternative approach description.
        Time Complexity: ...
        Space Complexity: ...
        """
        # Alternative implementation
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.methodName(test_input))  # Output: expected_output
```

### Critical Patterns
1. **Always include complexity analysis** in method docstrings
2. **Provide multiple solutions** when applicable (e.g., `groupAnagrams()` and `groupAnagramsCount()`)
3. **Use type hints** from `typing` module (`List[int]`, `List[str]`, etc.)
4. **Executable test cases** in `if __name__ == "__main__"` block with expected outputs
5. **Problem constraints** must be documented in module docstring

### Common Imports by Pattern
- Hash maps/counting: `from collections import Counter, defaultdict`
- Arrays/lists: `from typing import List`
- Keep imports minimal and relevant to the specific problem

## Solution Approach Patterns

### Hash Map Problems
- Prefer `Counter` for frequency counting (`02-is-anagram.py`, `05-top-k-elements-in-list.py`)
- Use `defaultdict(list)` for grouping (`04-anagram-groups.py`)
- Use `set()` for membership checking (`01-duplicate-integer.py`, `09-longest-consecutive-sequence.py`)

### Optimization Techniques
- **Bucket sort** for O(n) frequency problems (see `topKFrequentBucketSort` in `05-top-k-elements-in-list.py`)
- **Character counting arrays** (`[0] * 26`) for anagram problems (see `groupAnagramsCount` in `04-anagram-groups.py`)
- **Set lookups** to avoid nested loops (see `09-longest-consecutive-sequence.py` - checks `num - 1` to find sequence starts)

## Markdown Documentation
- Data structure guides explain: overview, time/space complexity tables, common operations, practice problems
- Include code examples in markdown guides for common patterns
- Use tables for complexity comparisons (see `static-array.md`, `hash-map.md`)

## Testing
- Solutions are tested inline via `if __name__ == "__main__"` blocks
- Include multiple test cases covering edge cases from problem statement
- Print statements should show both input context and expected output

## When Adding New Problems
1. Follow the naming pattern: `##-descriptive-problem-name.py`
2. Include full problem statement, examples, constraints, and LeetCode link
3. Document time/space complexity for ALL solution methods
4. Provide test cases with expected outputs
5. Consider adding alternative solutions with different trade-offs
