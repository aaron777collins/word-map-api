from flask import Flask
from flask import jsonify
from flask import request

from DataService import DataService

app = Flask(__name__)


@app.route("/agw/api", methods=['POST'])
def getRelatedWords():
    if(not request.is_json):
        return jsonify({"ERROR": "This API only accepts json as body input"})

    content = request.get_json()

    print(content)
    if not "words" in content:
        return jsonify({"error": "No 'words' variable found. Please call with an array of words"})
    words = content["words"]

    return jsonify(DataService.getRelatedWords(words))

if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=55556)
    app.run(host="0.0.0.0", port=55556, ssl_context='adhoc')
    