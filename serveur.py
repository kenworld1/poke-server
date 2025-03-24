from flask import Flask, request, jsonify

app = Flask(__name__)
clients = {}
pokes_en_attente = {}

@app.route("/connect", methods=["POST"])
def connect():
    client_ip = request.remote_addr
    client_id = request.json["id"]
    clients[client_id] = client_ip
    pokes_en_attente[client_id] = False
    print(f"Nouveau client connecté: {client_id} -> {client_ip}")
    return jsonify({"status": "ok"})

@app.route("/poke/<client_id>", methods=["POST"])
def poke(client_id):
    if client_id in pokes_en_attente:
        pokes_en_attente[client_id] = True
        print(f"Poke envoyé à {client_id}")
        return jsonify({"status": "poke envoyé"})
    return jsonify({"status": "client non trouvé"}), 404

@app.route("/check_poke/<client_id>", methods=["GET"])
def check_poke(client_id):
    if client_id in pokes_en_attente and pokes_en_attente[client_id]:
        pokes_en_attente[client_id] = False
        return jsonify({"poke": True})
    return jsonify({"poke": False})

@app.route("/clients", methods=["GET"])
def clients_list():
    return jsonify(clients)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
