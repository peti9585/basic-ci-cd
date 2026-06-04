from flask import Flask, request

app = Flask(__name__)

numbers = []

@app.route("/getnumbers")
def get_numbers():
    return numbers

@app.route("/addnumber", methods=["POST"])
def add_number():
    numbers.append(request.json.get("number"))
    return "Number added successfully", 200


