import flask

app = flask.Flask("overbookking-backend")


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


@app.route("/predict", methods=["POST"])
def handle_json():
    data = flask.request.json
    user_info = data["userInfo"]
    print(user_info)
    return flask.jsonify({"passChance": 1, "missChance": 0})
