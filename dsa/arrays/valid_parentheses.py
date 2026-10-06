"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""

class Solution:
    def is_valid(self, s: str) -> bool:
        if len(s) % 2:
            return False

        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in close_to_open:
                if not stack or stack.pop() != close_to_open[c]:
                    return False
            else:
                stack.append(c)

        return not stack