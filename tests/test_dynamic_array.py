import unittest

from data_structures.dynamic_array import DynamicArray



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