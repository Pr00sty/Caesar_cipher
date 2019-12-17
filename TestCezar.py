import unittest
import Cezar


class TestCezar(unittest.TestCase):

    def TestKodowanie(self):
        self.assertEqual(Cezar.cezar('abc', 3), 'def')

    def TestOdkodowywanie(self):
        self.assertEqual(Cezar.cezar('def', -3), 'abc')

    def Testaaa(self):
        self.assertEqual(3, 3)