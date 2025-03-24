from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
clients = {}

@app.route('/')
def accueil():
    return 'Serveur actif.'

@app.route('/connect', methods=['POST'])
def connect_client():
    ip_client = request.remote_addr
    client_id = str(uuid.uuid4())[:8]
    clients[client_id] = ip_client
    print(f"[CONNEXION] Nouveau client connecté : ID={client_id}, IP={ip_client}")
    return jsonify({"id": client_id})

@app.route('/poke', methods=['POST'])
def poke_client():
    data = request.json
    from_id = data.get('from_id')
    to_id = data.get('to_id')
    print(f"[POKE] De {from_id} vers {to_id}")
    return jsonify({"status": "Poke envoyé"})

@app.route('/clients')
def liste_clients():
    return jsonify(clients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
