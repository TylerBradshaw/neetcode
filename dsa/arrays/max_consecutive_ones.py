"""
You are given a binary array nums, return the maximum number of consecutive 1's in the array.
"""
from typing import List

class Solution:
    def find_max_consecutive_ones(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


def test_find_max_consecutive_ones():
    solution = Solution()

    assert solution.find_max_consecutive_ones([1, 1, 0, 1, 1, 1]) == 3
    assert solution.find_max_consecutive_ones([1, 0, 1, 1, 0, 1]) == 2
    assert solution.find_max_consecutive_ones([0, 0, 0]) == 0
    assert solution.find_max_consecutive_ones([1, 1, 1, 1]) == 4
    assert solution.find_max_consecutive_ones([1]) == 1
    assert solution.find_max_consecutive_ones([0]) == 0

    print("passed")


if __name__ == "__main__":
    test_find_max_consecutive_ones()