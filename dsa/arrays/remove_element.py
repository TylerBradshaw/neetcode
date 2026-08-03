"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


user_input = input("Enter list of numbers, comma separated: ")
nums = [int(value.strip()) for value in user_input.strip("[]").split(",") if value.strip()]
val = int(input("Enter val to remove: "))

expected_nums = sorted(number for number in nums if number != val)

solution = Solution()
k = solution.removeElement(nums, val)

assert k == len(expected_nums)

nums[:k] = sorted(nums[:k])

for i in range(k):
    assert nums[i] == expected_nums[i]

display_nums = nums[:k] + ["_"] * (len(nums) - k)

print(f"k = {k}")
print(f"nums = {display_nums}")
print("Passed")