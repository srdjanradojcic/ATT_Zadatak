import unittest
from REST.Control import Response
class RequestsTest(unittest.TestCase):

    def setUp(self):
        self.response = Response()

    def testpostRequestTestNewLink(self):
        new_link = 'www.google.com'
        data = {
            'url': new_link,
            'new_link': "www.localhost:5000/" + '191347bfe55d0ca9a574db77bc8648275ce258461450e793528e0cc6d2dcf8f5'
        }
        self.assertEqual(self.response.postRequest(new_link), data)

    def testPostRequestTestOldLink(self):
        old_link = 'www.google.rs'
        data = {
            'url': old_link,
            'new_link': "www.localhost:5000/" + '7f8acd75476ef25ec0238cd9cc545a24077d6676e47eca9a79da4b3d31839670'
        }
        self.assertEqual(self.response.postRequest(old_link), data)

    def testGetRequestLinkExists(self):
        hash_url = '7f8acd75476ef25ec0238cd9cc545a24077d6676e47eca9a79da4b3d31839670'
        self.assertEqual(self.response.getRequest(hash_url), 'www.google.rs')

    def testGetRequestLinkDoesntExists(self):
        hash_ulr = '0000000000000000000000000000000000000000000000000000000000000000'
        self.assertEqual(self.response.getRequest(hash_ulr), None)