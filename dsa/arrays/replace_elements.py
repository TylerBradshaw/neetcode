"""
You are given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Constraints:

1 <= arr.length <= 10,000
1 <= arr[i] <= 100,000
"""
from typing import List



class Solution:
    def replace_elements(self, arr: List[int]) -> List[int]:

        right_max = -1
        for i in range(len(arr) -1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr

user_input = input("Enter list of numbers, separated by commas:")
arr = [int(value.strip()) for value in user_input.strip("[]").split(",") if value.strip()]
solution = Solution()
k = solution.replace_elements(arr)
print(k)






