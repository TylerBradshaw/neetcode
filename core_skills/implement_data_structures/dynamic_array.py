"""
Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
int get(int i) will return the element at index i. Assume that index i is valid.
void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
void pushback(int n) will push the element n to the end of the array.
int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
void resize() will double the capacity of the array.
int getSize() will return the number of elements in the array.
int getCapacity() will return the capacity of the array.
If we call pushback(int n) but the array is full, we should resize() the array first.
"""
import unittest

class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.data = [0] * capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.data[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.data[self.size] = n
        self.size +=1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Pop from empty array")

        self.size -= 1
        return self.data[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [0] * self.capacity

        for i in range(self.size):
            new_arr[i] = self.data[i]

        self.data = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


class TestDynamicArray(unittest.TestCase):

    def test_initial_state(self):
        data = DynamicArray(4)

        self.assertEqual(data.getSize(), 0)
        self.assertEqual(data.getCapacity(), 4)

    def test_pushback(self):
        data = DynamicArray(2)

        data.pushback(10)
        data.pushback(20)

        self.assertEqual(data.getSize(), 2)
        self.assertEqual(data.get(0), 10)
        self.assertEqual(data.get(1), 20)

    def test_set(self):
        data = DynamicArray(2)

        data.pushback(10)
        data.set(0, 99)

        self.assertEqual(data.get(0), 99)

    def test_resize(self):
        data = DynamicArray(2)

        data.pushback(1)
        data.pushback(2)


        data.pushback(3)

        self.assertEqual(data.getCapacity(), 4)
        self.assertEqual(data.getSize(), 3)

        self.assertEqual(data.get(0), 1)
        self.assertEqual(data.get(1), 2)
        self.assertEqual(data.get(2), 3)

    def test_popback(self):
        data = DynamicArray(2)

        data.pushback(5)
        data.pushback(10)

        value = data.popback()

        self.assertEqual(value, 10)
        self.assertEqual(data.getSize(), 1)
        self.assertEqual(data.get(0), 5)

    def test_popback_empty(self):
        data = DynamicArray(2)

        with self.assertRaises(IndexError):
            data.popback()

    def test_get_out_of_bounds(self):
        data = DynamicArray(2)

        with self.assertRaises(IndexError):
            data.get(0)

        data.pushback(1)

        with self.assertRaises(IndexError):
            data.get(1)

        with self.assertRaises(IndexError):
            data.get(-1)

    def test_set_out_of_bounds(self):
        data = DynamicArray(2)

        with self.assertRaises(IndexError):
            data.set(0, 1)

        data.pushback(5)

        with self.assertRaises(IndexError):
            data.set(1, 10)

        with self.assertRaises(IndexError):
            data.set(-1, 10)

    def test_multiple_resizes(self):
        data = DynamicArray(1)

        for i in range(100):
            data.pushback(i)

        self.assertEqual(data.getSize(), 100)

        for i in range(100):
            self.assertEqual(data.get(i), i)


if __name__ == "__main__":
    unittest.main()
