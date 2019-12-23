import unittest
import Cezar


class TestCezar(unittest.TestCase):

    def test_kodowanie(self):
        self.assertEqual(Cezar.cezar('abc', 3), 'def')

    def test_odkodowywanie(self):
        self.assertEqual(Cezar.cezar('def', -3), 'abc')

    def test_1(self):
        self.assertEqual(3, 3)