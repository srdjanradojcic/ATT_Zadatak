import unittest
from Data.Driver import Driver
from Hash.Hash import SecretHashClass
class DataTests(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.hashedGoogle = '7f8acd75476ef25ec0238cd9cc545a24077d6676e47eca9a79da4b3d31839670'

    def testIsNewLink(self):
        self.assertTrue(self.driver.isNewLink('www.google.com'))
        self.assertFalse(self.driver.isNewLink('www.google.rs'))

    def testgetID(self):
        self.assertEqual(self.driver.getUrlFromId(1), "www.google.rs")

    def testgetUrl(self):
        self.assertEqual(self.driver.getIdFromUrl("www.google.rs"), 1)

    def testgetShort(self):
        self.assertEqual(self.driver.getHasedUrlFromId(1), self.hashedGoogle)

    def testgetIDHashed(self):
        self.assertEqual(self.driver.getIdFromHashedLink(self.hashedGoogle), 1)

    def testUpdate(self):
        self.driver.updateUrl('www.google.com')
        self.assertEqual(self.driver.getUrlFromId(3), 'www.google.com')
        self.assertEqual(self.driver.getIdFromUrl('www.google.com') ,3)
        self.assertEqual(self.driver.getHasedUrlFromId(3), '191347bfe55d0ca9a574db77bc8648275ce258461450e793528e0cc6d2dcf8f5')
        self.assertEqual(self.driver.getIdFromHashedLink('191347bfe55d0ca9a574db77bc8648275ce258461450e793528e0cc6d2dcf8f5'), 3)
