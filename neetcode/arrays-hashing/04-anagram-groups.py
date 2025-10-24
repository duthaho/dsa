"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

Recommended Time & Space Complexity
You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.
"""

# LeetCode Problem Link: https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(m * n) where m is the number of strings and n is the length of the longest string
        Space Complexity: O(m) for storing the grouped anagrams
        """
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())

    def groupAnagramsCount(self, strs: List[str]) -> List[List[str]]:
        """
        Alternative approach using character count as key.
        Time Complexity: O(m * n) where m is the number of strings and n is the length of the longest string
        Space Complexity: O(m) for storing the grouped anagrams
        """
        anagram_map = defaultdict(list)
        for s in strs:
            count = [0] * 26  # Since the problem states only lowercase English letters
            for char in s:
                count[ord(char) - ord("a")] += 1
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())


if __name__ == "__main__":
    solution = Solution()
    print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
    # Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
    print(solution.groupAnagrams(["x"]))
    # Output: [["x"]]
    print(solution.groupAnagrams([""]))
    # Output: [[""]]
