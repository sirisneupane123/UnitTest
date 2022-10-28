import unittest

class NegativeTestCase(unittest.TestCase) :
    def test(self):
        a= 1
        b= 2

        message = "not equal"

        self.assertEqual(a,b,message)

    def test2(self):
        a = "jack"
        b = "jill"

        message = "not equal"

        self.assertEqual(a, b, message)

if __name__ == '__main__':
    unittest.main()