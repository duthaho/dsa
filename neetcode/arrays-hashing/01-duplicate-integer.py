"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
"""

# LeetCode Problem Link: https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) in the worst case when all elements are unique
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 3]))  # Output: True
    print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False
