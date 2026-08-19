"""
You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""
from typing import List

class Solution:
    def get_concatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for _ in range(2):
            for num in nums:
                ans.append(num)

        return ans

# print(Solution().getConcatenation([1,2,3]))

user_input = input("Enter list of numbers, separated by commas:")
nums = [int(value.strip()) for value in user_input.strip("[]").split(",") if value.strip()]
solution = Solution()
k = solution.get_concatenation(nums)
print(k)