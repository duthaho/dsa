"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
"""

# LeetCode Problem Link: https://leetcode.com/problems/product-of-array-except-self/


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(n) where n is the length of nums
        Space Complexity: O(1) excluding the output array
        """
        n = len(nums)
        output = [1] * n

        # Calculate left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Calculate right products and multiply with left products
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 4, 6]))  # Output: [48, 24, 12, 8]
    print(solution.productExceptSelf([-1, 0, 1, 2, 3]))  # Output: [0, -6, 0, 0, 0]
