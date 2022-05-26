from flask import Flask
from flask import jsonify
from flask import request

from DataService import DataService

app = Flask(__name__)


@app.route("/agw/api", methods=['GET'])
def getRelatedWords():
    if(not request.is_json):
        return jsonify({"ERROR": "This API only accepts json as body input"})

    content = request.get_json()

    print(content)
    if not "words" in content:
        return jsonify({"error": "No 'words' variable found. Please call with an array of words"})
    words = content["words"]

    return jsonify(DataService.getRelatedWords(words))