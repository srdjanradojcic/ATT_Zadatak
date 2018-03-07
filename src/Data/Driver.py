from flask import jsonify
from Data import *
from Short import *
from Hash.Hash import SecretHashClass
class Driver():

    def getLastId(self):
        if len(short_links) == len(links):
            return len(short_links)
        raise Exception("Data is not valid")

    def getUrlFromId(self, id):
        if id < 0:
            raise Exception("Id is not valid")
        for link in links:
            if link['id'] == id:
                return link['url']
        # TODO Maybe this exception revels too much
        raise Exception("There is no url that matchs id")

    def getIdFromUrl(self, url):
        for link in links:
            if link['url'] == url:
                return link['id']
        raise Exception('There is no matching id from given url')

    def getHasedUrlFromId(self, id):
        for short_link in short_links:
            if short_link['id'] == id:
                return short_link['short_link']
        raise Exception('There is no such link')

    def getIdFromHashedLink(self, hashed_url):
        for short_link in short_links:
            if short_link['short_link'] == hashed_url:
                return short_link['id']
        raise Exception("There is no matching id")

    def isNewLink(self, url):
        for link in links:
            if link['url'] == url:
                return False
        return True

    def updateUrl(self, url):
        secretHash = SecretHashClass()
        data = secretHash.hashData(url)
        id = self.getLastId() + 1
        short = {
            'short_link': data,
            'id': id
        }
        short_links.append(short)
        link = {
            'id':id ,
            'url' : url
        }
        links.append(link)

    def retiveUrl(self, id):
        data = {
            'url': self.getUrlFromId(id),
            'new_link': "localhost:5000/" + self.getHasedUrlFromId(id)
        }

        return data