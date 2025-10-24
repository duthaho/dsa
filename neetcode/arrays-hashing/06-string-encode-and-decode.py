"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

Recommended Time & Space Complexity
You should aim for a solution with O(m) time for each encode() and decode() call and O(m+n) space, where m is the sum of lengths of all the strings and n is the number of strings.
"""

# LeetCode Problem Link: https://leetcode.com/problems/encode-and-decode-strings/

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.

        Time Complexity: O(m) where m is the total length of all strings in strs
        Space Complexity: O(m) for the encoded string
        """
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string to a list of strings.

        Time Complexity: O(m) where m is the length of the encoded string s
        Space Complexity: O(n) where n is the number of decoded strings
        """
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_strs.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decoded_strs


if __name__ == "__main__":
    solution = Solution()
    encoded = solution.encode(["neet", "code", "love", "you"])
    print(f"Encoded: {encoded}")
    decoded = solution.decode(encoded)
    print(f"Decoded: {decoded}")
