import hashlib
class SecretHashClass():

    def hashData(self, data):
        return hashlib.sha256(data).hexdigest()

    def verifyData(self, vdata):
        if self.hashData(vdata) == self.data:
            return True
        return False
