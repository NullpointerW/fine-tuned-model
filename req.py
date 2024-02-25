import json

from flask import Flask, request
from flask_cors import CORS

import fine_tuned

app = Flask(__name__)
CORS(app)
template = '{"messages": [{"role": "user", "content": ""},{"role": "assistant", "content": ""}]}'


@app.route('/ft', methods=['POST'])
def api():
    data = request.get_json()
    if not data or not data.get("qa"):
        return 'jsonData can not be empty', 400
    fine_tuned.tuned(data.get("qa"), data.get("id"))
    return "ok", 200


@app.route('/modtoken', methods=['GET'])
def api_get():
    t = request.args.get("token")
    return 'ok', 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
