from flask import Response
class RedirectResponse(Response):

    def __init__(self, url):
        html = '<!DOCTYPE HTML PUBLIC>\n<title>Redirecting...</title>\n'
        Response.__init__(self, response = html, status=301, mimetype='text/html')
        self.headers['Location'] = url