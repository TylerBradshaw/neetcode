"""
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.dummy = ListNode(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.dummy.next
        for _ in range(index):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy.next
        self.dummy.next = new_node
        self.size += 1

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.dummy

        while curr.next:
            curr = curr.next

        curr.next = new_node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        curr = self.dummy

        for _ in range(index):
            curr = curr.next

        curr.next = curr.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        values = []
        curr = self.dummy.next

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values

def test_linked_list():
    ll = LinkedList()

    ll.insertHead(1)
    ll.insertTail(2)
    ll.insertHead(0)

    assert ll.get(0) == 0
    assert ll.get(1) == 1
    assert ll.get(2) == 2
    assert ll.get(3) == -1

    assert ll.getValues() == [0, 1, 2]

    assert ll.remove(1) is True
    assert ll.getValues() == [0, 2]

    assert ll.remove(10) is False

    print("All tests passed!")


if __name__ == "__main__":
    test_linked_list()