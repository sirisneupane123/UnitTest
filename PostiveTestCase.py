import unittest


def sum(a, b):
    return a + b


class PositiveTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(sum(2, 5), 7)

    def test2(self):
        self.assertEqual(sum(1,1),2)


if __name__ == '__main__':
    unittest.main()
