import unittest


def sum(a, b):  # defining the function to be tested
    return a + b

class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(2, 5), 7)


if __name__ == '__main__':
    unittest.main()