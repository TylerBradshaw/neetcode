"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
Each function should run in O(1) time.
"""

class MinStack:

    def __init__(self):
    # list
    def push(self, val: int) -> None:
    # append

    def pop(self) -> None:
    # pop

    def top(self) -> int:
    # list[-1]

    def getMin(self) -> int:
    # while stack: track min and pop to temp; while temp: pop back to stack