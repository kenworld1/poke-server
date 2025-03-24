from flask import Flask, request, jsonify
import random

app = Flask(__name__)
clients = {}

@app.route('/connect', methods=['POST'])
def connect():
    client_ip = request.remote_addr
    client_id = random.randint(1000, 9999)
    clients[client_id] = request.remote_addr
    print(f"Nouveau client connecté ID {client_id}, IP : {clients[client_id]}")
    return jsonify({"id": client_id}), 200

@app.route('/clients', methods=['GET'])
def list_clients():
    return jsonify(clients)

@app.route('/poke/<int:id>', methods=['GET'])
def poke(id):
    if id in clients:
        ip = clients[id]
        print(f"Poke envoyé à l'ID {id} (IP: {ip})")
        return jsonify({'result': 'ok'}), 200
    return jsonify({"error": "ID introuvable"}), 404

@app.route('/command', methods=['POST'])
def console_command():
    data = request.json
    cmd = data.get('cmd')
    if cmd.startswith("poke "):
        _, id = cmd.split()
        return poke(int(id))
    elif cmd == "clients":
        return jsonify(clients)
    else:
        return jsonify({"erreur": "Commande inconnue"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
