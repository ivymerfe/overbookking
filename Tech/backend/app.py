import flask
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("../model/flight_miss_prediction/checkpoint-500")

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
    inputs = tokenizer(user_info, return_tensors="pt")
    logits = model(**inputs).logits
    output = logits[0].softmax(dim=0).tolist()
    return flask.jsonify({"passChance": output[0], "missChance": output[1]})
