from flask import Flask, jsonify,request, abort, redirect, url_for, Response
from REST.Control import Control
from REST.CustomReponse import RedirectResponse
control = Control()
app = Flask(__name__)


@app.route('/shorten', methods=['POST'])
def postRequest():
    if not request.json or not 'url' in request.json:
        abort(400)
    data = control.postRequest(request.json.get('url', ""))
    return jsonify(data)

@app.route('/<string:url>', methods=['GET'])
def getRequest(url):
    res = control.getRequest(url)
    if res == None:
        abort(404)
    else:
        response = RedirectResponse(res)
        return response

if __name__ == '__main__':
    app.run(debug=True)