"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x: Record a new score of x.

'+': Record a new score that is the sum of the previous two scores.

'D': Record a new score that is the double of the previous score.

'C': Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.
"""
from typing import List

class Solution:
    def calculate_points(self, operations: List[str]) -> int:
        x = []
        for i in operations:
            if i == '+':
                # add previous 2 scores
            if i == 'D':
                # double prev score
            if i == 'C':
                # remove prev score
            else:
                # score (make int)