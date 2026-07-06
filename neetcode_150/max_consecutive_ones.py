from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
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

    assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
    assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
    assert solution.findMaxConsecutiveOnes([0, 0, 0]) == 0
    assert solution.findMaxConsecutiveOnes([1, 1, 1, 1]) == 4
    assert solution.findMaxConsecutiveOnes([1]) == 1
    assert solution.findMaxConsecutiveOnes([0]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_find_max_consecutive_ones()