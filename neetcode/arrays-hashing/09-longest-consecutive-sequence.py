"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
"""

# LeetCode Problem Link: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for storing the set of numbers
        """
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Only start counting if 'num' is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count the length of the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([2, 20, 4, 10, 3, 4, 5]))  # Output: 4
    print(solution.longestConsecutive([0, 3, 2, 5, 4, 6, 1, 1]))  # Output: 7
