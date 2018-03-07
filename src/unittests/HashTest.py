import unittest
from Hash.Hash import SecretHashClass
class HashTests(unittest.TestCase):

    def setUp(self):
        self.hasho = SecretHashClass('www.google.rs')
        self.hashedGoogle = '7f8acd75476ef25ec0238cd9cc545a24077d6676e47eca9a79da4b3d31839670'

    def testHashing(self):

        self.assertEqual(self.hasho.hashData('www.google.rs').lower(), self.hashedGoogle.lower())
