import main
import unittest


class Test(unittest.TestCase):
    def test_is_included(self):
        """
        Testing main.is_included(a, b)
        """
        # Case 1 : a is included in b
        a = (-1, 5)
        b = (-5, 10)
        self.assertTrue(main.is_included(a, b))

        # Case 2 : a equals b
        a = (0, 5)
        b = a
        self.assertTrue(main.is_included(a, b))

        # Case 3 : a is not included in b (no overlap)
        a = (12, 15)
        b = (9, 11)
        self.assertFalse(main.is_included(a, b))

        # Case 4 : a is not included in b (overlap)
        a = (11, 15)
        b = (9, 11)
        self.assertFalse(main.is_included(a, b))

        # Case 5 :  a is not included in b (b is included in a)
        a = (-5, 10)
        b = (-1, 5)
        self.assertFalse(main.is_included(a, b))

        # Case 6 : a[0] == a[1] and is included in b
        a = (0, 0)
        b = (-1, 2)
        self.assertTrue(main.is_included(a, b))


if __name__ == '__main__':
    unittest.main()
