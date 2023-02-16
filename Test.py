import unittest

from algorithim import find_max_min

class MyTest(unittest.TestCase):
    def test_find_max_min(self):
        # passing my test data
        mat1 = [[70,80,10,90],[10,50,44,30],[100,60,20, 50]]
        mat2 = [[5,16,20],[9,11,18],[15,16,17]]

        # runing my method
        first_test = find_max_min(mat1)
        second_test = find_max_min(mat2)

        # unit test
        self.assertEqual(first_test, 50,'should be 50')
        self.assertEqual(second_test, 17,'should be 17')

if __name__ == '__main__':
    unittest.main()
