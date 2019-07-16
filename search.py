import sys
from contextlib import suppress
import json
from flask import Flask, request, jsonify


with open("index.json") as index_file, open("translations.json") as translations_file:
    index = json.load(index_file)
    translations = json.load(translations_file)

app = Flask(__name__)


@app.route("/search/")
def search():
    words = request.args.get("q", "").lower().split()
    lang = request.args.get("lang", "fr")
    result = {}
    for msgid in index.get(words[0], []):
        msgid_lower = msgid.lower()
        if all(word in msgid_lower.split() for word in words):
            with suppress(KeyError):
                result[msgid] = translations[msgid][lang]
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
