"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.
"""

# LeetCode Problem Link: https://leetcode.com/problems/top-k-frequent-elements/


from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for storing the frequency map
        """
        frequency_map = Counter(nums)
        # Sort the elements based on frequency and get the top k elements
        most_common = frequency_map.most_common(k)
        return [element for element, _ in most_common]
    
    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        """
        Alternative approach using bucket sort.
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(n) for storing the frequency map and buckets
        """
        frequency_map = Counter(nums)
        max_freq = max(frequency_map.values())
        
        # Create buckets where index represents frequency
        buckets = [[] for _ in range(max_freq + 1)]
        for num, freq in frequency_map.items():
            buckets[freq].append(num)
        
        result = []
        # Collect top k frequent elements from the buckets
        for freq in range(max_freq, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))  # Output: [2, 3]
    print(solution.topKFrequent([7, 7], 1))  # Output: [7]
