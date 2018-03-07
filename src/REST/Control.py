from flask import Response
class Control():

    def __init__(self):
        from Data.Driver import Driver
        self.driver = Driver()

    def postRequest(self, url):
        if self.driver.isNewLink(url):
            return self.newLink(url)
        else:
            return self.oldLink(url)

    def newLink(self, url):
        self.driver.updateUrl(url)
        id = self.driver.getIdFromUrl(url)
        return self.driver.retiveUrl(id)

    def oldLink(self, url):
        id = self.driver.getIdFromUrl(url)
        return self.driver.retiveUrl(id)

    def getRequest(self, short_url):
        try:
            id = self.driver.getIdFromHashedLink(short_url)
            return self.driver.getUrlFromId(id)
        except Exception:
            return None

