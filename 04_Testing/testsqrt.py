import unittest
import sqrt

class SqrtTests(unittest.TestCase):
    def test_correct1(self):
        b=sqrt.sqrt(0)
        self.assertEqual(b,0)

    def test_negative1(self): 
        with self.assertRaises(ValueError):
            b=sqrt.sqrt(-4)

