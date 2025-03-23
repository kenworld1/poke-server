from flask import Flask, request, jsonify
app = Flask(__name__)

pokes = []

@app.route('/')
def index():
    return "Poke server actif!"

@app.route('/poke', methods=['POST'])
def poke():
    data = request.json
    pokes.append({"from": data["from"], "to": data["to"]})
    return jsonify({"status": "ok"})

@app.route('/get_pokes/<username>', methods=['GET'])
def get_pokes(username):
    user_pokes = [poke for poke in pokes if poke["to"] == username]
    for poke in user_pokes:
        pokes.remove(poke)
    return jsonify(user_pokes)
